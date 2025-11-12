from fastapi import FastAPI
import logging
from app.core import settings

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


def main():
    import uvicorn

    if settings.MODE == "development":
        logging.info("Starting server in development mode")
        uvicorn.run("server:app", host="localhost", port=8000, reload=True)
    else:
        logging.info("Starting server in production mode")
        uvicorn.run("server:app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
