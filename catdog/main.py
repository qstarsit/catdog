from fastapi import FastAPI

from catdog import routes

app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


app.include_router(routes.router)