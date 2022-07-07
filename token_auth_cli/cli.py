import logging

import rich
import click

from .config import Settings, App
from . import utils, commands

logger = logging.getLogger(__name__)


@click.group()
@click.option("--verbose/--no-verbose",
              help="Show additional information")
@click.option("--debug/--no-debug",
              help="Show debug information")
@click.option("--confirm-settings", type=bool,
              help="Confirm settings before trying to get token.")
@click.option("--show-settings", type=bool,
              help="Show settings before trying to get token.")
@click.option("--api", type=str,
              help="API url.")
@click.option("--api-get-token", type=str,
              help="API url to use when trying to get token.")
@click.option("--api-get", type=str,
              help="API url to check if token valid.")
@click.option("--config",
              type=click.Path(readable=True,
                              file_okay=True, dir_okay=False),
              default=".token_auth_cli_config.toml",
              help="Config file.")
@click.pass_context
def cli_commands(context, **kwargs):
    """CLI commands."""
    filtered = utils.filter_none(kwargs)
    settings = Settings(**filtered)
    if settings.debug:
        logging.basicConfig(level=logging.DEBUG)
    if settings.show_settings:
        rich.inspect(settings)
    if settings.confirm_settings:
        if not click.confirm("Are these settings correct?", default=False):
            raise click.Abort
    app = App(settings=settings)
    context.obj = app
    utils.show_if_debug(kwargs, filtered, settings, app)


@cli_commands.command("get")
@click.option("--username", prompt="Username")
@click.password_option("--password", prompt="Password")
@click.pass_context
def get_token(*args, **kwargs):
    """Get token."""
    return utils.run_async_command(commands.get_token, *args, **kwargs)


def main():
    """Main function"""
    cli_commands()  # pylint: disable=no-value-for-parameter


if __name__ == "__main__":
    main()
