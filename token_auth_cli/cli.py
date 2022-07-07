import logging
import asyncio

from typing import Any

import rich
import click
import aiohttp

from .config import Settings, App
from . import commands

logger = logging.getLogger(__name__)


def _add_session(func):
    async def add_session_wrapper(context, *args, **kwargs):
        api = context.obj.settings.api
        async with aiohttp.ClientSession(api) as session:
            context.obj.session = session
            result = await func(context, *args, **kwargs)
        return result
    return add_session_wrapper


def _run_async_command(func, *args, **kwargs) -> Any:
    func = _add_session(func)
    return asyncio.run(func(*args, **kwargs))


def _filter_and_add(kwargs_dict, **kwargs):
    filtered = {}
    for name, val in kwargs_dict.items():
        if val:
            filtered.update({name: val})
    filtered.update(kwargs)
    return filtered


@click.group()
@click.option("--verbose/--no-verbose",
              help="Show additional information")
@click.option("-d", "--debug/--no-debug",
              help="Show debug information")
@click.option("--api", type=str,
              help="API url.")
@click.option("--api-get-token", type=str,
              help="API url to use when trying to get token.")
@click.option("--api-get", type=str,
              help="API url to check if token valid.")
@click.option("--config", type=click.Path(),
              help="Config file.")
@click.pass_context
def cli_commands(context, **kwargs):
    filtered = _filter_and_add(kwargs)
    settings = Settings(**filtered)
    rich.inspect(settings)
    if not click.confirm("Are these settings correct?", default=False):
        raise click.Abort
    app = App(settings=settings)
    context.obj = app


@cli_commands.command("get")
@click.option("--username", prompt="Username")
@click.password_option("--password", prompt="Password")
@click.pass_context
def get_token(*args, **kwargs):
    """Get token."""
    return _run_async_command(commands.get_token, *args, **kwargs)


def main():
    cli_commands()  # pylint: disable=no-value-for-parameter


if __name__ == "__main__":
    main()
