import uvicorn
from fastapi import FastAPI
from urls import router


app = FastAPI(
    title="Environments Variables - Test",
    description="Example about how to read environments variables from .env file"
)


app.include_router(router, prefix="")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
