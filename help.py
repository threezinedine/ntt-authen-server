from config.args import ArgConfig
from config.utils import InstallDependencies, InstallNewDependencies, RunServer


def main() -> None:
    arg_config = ArgConfig()

    InstallDependencies("ntt_server")

    if arg_config.Command == "run":
        RunServer()
    elif arg_config.Command == "install":
        dependencies = arg_config.Dependencies
        assert (
            dependencies is not None
        ), "Dependencies should not be None for install command"
        InstallNewDependencies(dependencies, "ntt_server")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
