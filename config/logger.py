import logging


logger = logging.getLogger("Configure")
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "[%(levelname)s] - %(message)s",
)

consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)
