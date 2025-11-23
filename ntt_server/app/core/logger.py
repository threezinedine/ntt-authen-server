import logging
from colorlog import ColoredFormatter


logger = logging.getLogger("ntt_authen_server")


formatter = ColoredFormatter(
    "[%(log_color)s%(levelname)s%(reset)s] - %(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)


def RegisterFileLogger(fileName: str) -> None:
    """Create a file logger.

    Parameters
    ----------
    fileName : str
        The name of the log file.
    """

    fileHandler = logging.FileHandler(fileName)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
