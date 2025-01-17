import logging
from pathlib import Path

import click

from algokit.core.bootstrap import bootstrap_any_including_subdirs, bootstrap_env, bootstrap_npm, bootstrap_poetry

logger = logging.getLogger(__name__)


@click.group(
    "bootstrap", short_help="Bootstrap local dependencies in an AlgoKit project; run from project root directory."
)
def bootstrap_group() -> None:
    """
    Expedited initial setup for any developer by installing and configuring dependencies and other
    key development environment setup activities.
    """


@bootstrap_group.command(
    "all", short_help="Runs all bootstrap sub-commands in the current directory and immediate sub directories."
)
def bootstrap_all() -> None:
    cwd = Path.cwd()
    bootstrap_any_including_subdirs(cwd)
    logger.info(f"Finished bootstrapping {cwd}")


@bootstrap_group.command(
    "env",
    short_help="Copies .env.template file to .env in the current working directory "
    "and prompts for any unspecified values.",
)
def env() -> None:
    bootstrap_env(Path.cwd())


@bootstrap_group.command(
    "poetry",
    short_help="Installs Python Poetry (if not present) and runs `poetry install` in the "
    "current working directory to install Python dependencies.",
)
def poetry() -> None:
    bootstrap_poetry(Path.cwd())


@bootstrap_group.command(
    "npm", short_help="Runs `npm install` in the current working directory to install Node.js dependencies."
)
def npm() -> None:
    bootstrap_npm(Path.cwd())
