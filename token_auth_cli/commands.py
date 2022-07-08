import logging
import rich

from . import auth

logger = logging.getLogger(__name__)


async def login(context, **kwargs):
    """Try to login."""
    user = auth.User(username=kwargs['username'], password=kwargs['password'])
    async for token in auth.get_token(context, user, **kwargs):
        rich.print(f"Token: {token}")


async def relogin(contex, **kwargs):
    return


async def tokens_list(context, **kwargs):
    return


async def tokens_remove(context, **kwargs):
    return


async def init(context, **kwargs):
    return
