from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


def main():
    import uvicorn

    uvicorn.run("server:app", host="localhost", port=8000, reload=True)


if __name__ == "__main__":
    main()
