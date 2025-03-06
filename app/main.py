from fastapi import FastAPI
from app.routers.user_routes import router as user_router
from app.containers import init_container

app = FastAPI()
app.include_router(user_router)


@app.on_event("startup")
async def startup_event():
    await init_container()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
