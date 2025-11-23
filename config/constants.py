from .utils import DetectPythonCommand, DetectPythonExecutable, DetectAlembicExecutable


MIGRATIONS_FOLDER = "migrations"
PYTHON_COMMAND = DetectPythonCommand()
PYTHON_EXECUTABLE = DetectPythonExecutable()
ALEMBIC_EXECUTABLE = DetectAlembicExecutable()
