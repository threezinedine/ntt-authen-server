import os
import subprocess
from typing import Any

from .logger import logger


def DetectPythonCommand() -> str:
    """
    Detect the appropriate Python command based on the operating system.

    Returns
    -------
    str
        The Python command to use ('python' or 'python3').
    """
    pythonCommand = "python"

    try:
        RunCommand("python --version", shell=False)
    except:
        pythonCommand = "python3"

    return pythonCommand


def DetectPythonExecutable() -> str:
    """
    Detect the full path to the Python executable.

    Returns
    -------
    str
        The full path to the Python executable.
    """
    if os.name == "nt":
        return os.path.join("venv", "Scripts", "python.exe")
    else:
        return os.path.join("venv", "bin", "python3")


from .constants import PYTHON_COMMAND, PYTHON_EXECUTABLE


def CheckFileModified(filePath: str) -> bool:
    """
    Tool for file caching system.

    Parameters
    ----------
    filePath : str
        The path to the file to check. Relative to the source directory.

    Returns
    -------
    bool
        True if the file has been modified, False otherwise.
    """
    cacheFileStampPath = os.path.join("temp", f"{filePath}.stamp")
    if not os.path.exists(cacheFileStampPath):
        return True

    fileModTime = os.path.getmtime(filePath)
    if fileModTime > os.path.getmtime(cacheFileStampPath):
        return True
    return False


def CacheFileStamp(filePath: str) -> None:
    """
    Try to update the file modification stamp in the cache.

    Parameters
    ----------
    filePath : str
        The path to the file to cache. Relative to the source directory.
    """
    cacheFileStampPath = os.path.join("temp", f"{filePath}.stamp")

    if not os.path.exists("temp"):
        os.makedirs("temp")

    os.makedirs(os.path.dirname(cacheFileStampPath), exist_ok=True)
    with open(cacheFileStampPath, "w") as f:
        f.write("cached")


def RunCommand(
    command: str,
    folder: str | None = None,
    shell: bool = True,
) -> None:
    """
    Run a shell command and return its output.

    Parameters
    ----------
    command : str
        The command to run.
    cwd : str | None
        The working directory to run the command in. If None, uses the current working directory.
        (relative path to source dir).
    shell : bool
        Whether to run the command in a shell.
    """
    logger.info(f"Running command: {command}")
    subprocess.run(
        command, shell=shell, check=True, cwd=folder if folder else os.getcwd()
    )


def InstallNewDependencies(
    dependencies: list[str],
    **kwargs: Any,
) -> None:
    """
    Install new dependencies using pip.

    Parameters
    ----------
    dependencies : list[str]
        A list of dependencies to install.
    """
    folder = "ntt_server"

    logger.info(f"Installing new dependencies: {' '.join(dependencies)}")
    RunCommand(
        f"{PYTHON_EXECUTABLE} -m pip install {' '.join(dependencies)}", folder=folder
    )
    RunCommand(f"{PYTHON_EXECUTABLE} -m pip freeze > requirements.txt", folder=folder)
    CacheFileStamp(os.path.join(folder, "requirements.txt"))


def InstallDependencies(folder: str) -> None:
    """
    Install required dependencies for the project.

    Parameters
    ----------
    folder : str
        The folder where the dependencies should be installed (relative path to source dir).
    """

    requirementsFilePath = os.path.join(folder, "requirements.txt")
    envExist = os.path.exists(os.path.join(folder, "venv"))
    requirementsModified = CheckFileModified(requirementsFilePath)

    if envExist and not requirementsModified:
        logger.info(f"Dependencies already installed in folder: {folder}")
        return

    if not envExist:
        logger.info(f"Creating virtual environment in folder: {folder}")

        logger.info("Installing project dependencies...")
        RunCommand(f"{PYTHON_COMMAND} -m venv venv", folder=folder)

        logger.info("Update the pip package manager...")
        RunCommand(f"{PYTHON_EXECUTABLE} -m pip install --upgrade pip", folder=folder)

    logger.info("Installing required packages from requirements.txt...")
    RunCommand(f"{PYTHON_EXECUTABLE} -m pip install -r requirements.txt", folder=folder)

    logger.info("Dependencies installed successfully.")

    CacheFileStamp(os.path.join(folder, "requirements.txt"))


def RunServer(type: str = "dev", **kwargs: Any) -> None:
    """
    Run the FastAPI development server with auto-reload.

    Parameters
    ----------
    type : str
        'dev' for development server with auto-reload or 'prod' for production server.
    """
    setupCommand = ""

    assert type in ("dev", "prod"), "Invalid server type. Use 'dev' or 'prod'."

    if os.name == "nt":
        setupCommand = f"copy .{type}.env .env"
    else:
        setupCommand = f"cp .{type}.env .env"

    RunCommand(setupCommand, folder="ntt_server")
    RunCommand(f"{PYTHON_EXECUTABLE} server.py", folder="ntt_server")


def RunTests(
    filter: str | None = None,
    **kwargs: Any,
) -> None:
    """
    Run the test suite.

    Parameters
    ----------
    filter : str
        A filter to select specific tests to run.
    """
    command = f"{PYTHON_EXECUTABLE} -m pytest"
    if filter:
        command += f" -k {filter}"

    RunCommand(command, folder="ntt_server")
