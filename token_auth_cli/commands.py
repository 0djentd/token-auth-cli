import logging
import asyncio

import rich

from aiohttp.client_exceptions import ClientConnectionError

logger = logging.getLogger(__name__)


async def get_token(context, **kwargs):
    repeat = kwargs["repeat"]
    app = context.obj
    request_data = {"username": kwargs["username"],
                    "password": kwargs["password"]}

    async def _try_to_get_token(app, request_data):
        try:
            async with app.session.post(
                    app.settings.api_get_token, json=request_data) as req:
                if req.status != 200:
                    rich.print(f"[red]{req.status}[/red]")
                else:
                    rich.print("[green]OK[/green]")
        except ClientConnectionError as err:
            rich.print(f"[red]{err}[/red]")

    await _try_to_get_token(app, request_data)
    while repeat:
        await asyncio.sleep(kwargs['repeat_interval'])
        await _try_to_get_token(app, request_data)
