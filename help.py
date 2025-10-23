from config.args import ArgConfig


def main() -> None:
    arg_config = ArgConfig()

    if arg_config.Command == "run":
        print("Usage: run - Start the development server with auto-reload")


if __name__ == "__main__":
    main()
