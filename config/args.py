from argparse import ArgumentParser
from typing import Any


class ArgConfig:
    """
    Configuration class for command-line arguments.
    """

    def __init__(self) -> None:
        parser = ArgumentParser(description="Project Management Utilities")

        subparsers = parser.add_subparsers(
            dest="command",
            required=True,
        )

        runParser = subparsers.add_parser(
            "run",
            help="Start the development server with auto-reload",
        )

        runParser.add_argument(
            "-t",
            "--type",
            default="dev",
            choices=["dev", "prod"],
            help="Type of server to run: 'dev' for development with auto-reload, 'prod' for production",
        )

        testParser = subparsers.add_parser(
            "test",
            help="Run the test suite (not implemented yet)",
        )

        testParser.add_argument("-f", "--filter", default=None)

        installParser = subparsers.add_parser(
            "install",
            help="Install project dependencies (not implemented yet)",
        )

        installParser.add_argument(
            "dependencies",
            nargs="+",
            help="List of dependencies to install",
        )

        subparsers.add_parser(
            "build",
            help="Build the project for production (not implemented yet)",
        )

        self._args = parser.parse_args()

    @property
    def Command(self) -> str:
        """
        Supported commands:
        - run: Start the development server with auto-reload
        - test: Run the test suite (not implemented yet)
        - install: Install project dependencies (not implemented yet)
        - build: Build the project for production (not implemented yet)
        """
        return self._args.command

    def ToDict(self) -> dict[str, Any]:
        return vars(self._args)
