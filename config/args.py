from argparse import ArgumentParser


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

        subparsers.add_parser(
            "run",
            help="Start the development server with auto-reload",
        )

        subparsers.add_parser(
            "test",
            help="Run the test suite (not implemented yet)",
        )

        subparsers.add_parser(
            "install",
            help="Install project dependencies (not implemented yet)",
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
