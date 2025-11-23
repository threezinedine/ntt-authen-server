import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core import settings, logger, RegisterFileLogger
import argparse

parser = argparse.ArgumentParser(description="Run the FastAPI server.")
parser.add_argument(
    "--verbose",
    "-v",
    action="store_true",
    help="Enable verbose logging",
)
parser.add_argument(
    "--use-log-file",
    "-u",
    action="store_true",
    help="Enable logging to a specified file in the .env file",
)

args = parser.parse_args()

if args.verbose:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

if args.use_log_file:
    RegisterFileLogger(settings.LOG_FILE)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting up the server in {settings.MODE}...")
    yield
    logger.info(f"Shutting down the server...")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


def main():
    import uvicorn

    if settings.MODE == "development":
        uvicorn.run(
            "server:app",
            host="localhost",
            port=8000,
            reload=True,
            log_config=None,
            timeout_graceful_shutdown=5,
        )
    else:
        uvicorn.run(
            "server:app",
            host="0.0.0.0",
            port=8000,
            log_config=None,
            timeout_graceful_shutdown=5,
        )


if __name__ == "__main__":
    main()
