from config.args import ArgConfig
from config.utils import (
    InstallDependencies,
    InstallNewDependencies,
    RunServer,
    RunTests,
    RunMigrations,
    CreateMigrationIfNeeded,
)


def main() -> None:
    arg_config = ArgConfig()

    InstallDependencies("ntt_server")
    CreateMigrationIfNeeded(**arg_config.ToDict())

    if arg_config.Command == "run":
        RunServer(**arg_config.ToDict())
    elif arg_config.Command == "install":
        InstallNewDependencies(**arg_config.ToDict())
    elif arg_config.Command == "test":
        RunTests(**arg_config.ToDict())
    elif arg_config.Command == "migrate":
        RunMigrations(**arg_config.ToDict())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
