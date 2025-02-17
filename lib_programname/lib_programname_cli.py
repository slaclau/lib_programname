# STDLIB
import sys
from typing import Optional

# OWN
import cli_exit_tools

# EXT
import click

# CONSTANTS
CLICK_CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

try:
    from . import __init__conf__
    from . import lib_programname
except (ImportError, ModuleNotFoundError):  # pragma: no cover
    # imports for doctest
    import __init__conf__  # type: ignore  # pragma: no cover
    import lib_programname  # type: ignore  # pragma: no cover


def info() -> None:
    """
    >>> info()
    Info for ...

    """
    __init__conf__.print_info()


@click.group(help=__init__conf__.title, context_settings=CLICK_CONTEXT_SETTINGS)
@click.version_option(
    version=__init__conf__.version, prog_name=__init__conf__.shell_command, message=f"{__init__conf__.shell_command} version {__init__conf__.version}"
)
@click.option("--traceback/--no-traceback", is_flag=True, type=bool, default=None, help="return traceback information on cli")
def cli_main(traceback: Optional[bool] = None) -> None:
    if traceback is not None:
        cli_exit_tools.config.traceback = traceback


@cli_main.command("info", context_settings=CLICK_CONTEXT_SETTINGS)  # type: ignore
def cli_info() -> None:
    """get program informations"""
    info()


# entry point if main
if __name__ == "__main__":
    try:
        cli_main()
    except Exception as exc:
        cli_exit_tools.print_exception_message()
        sys.exit(cli_exit_tools.get_system_exit_code(exc))
    finally:
        cli_exit_tools.flush_streams()
