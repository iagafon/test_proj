from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
async def home():
    return {"msg": "hello world"}


if __name__ == "__main__":
    uvicorn.run("main:app", host= 'localhost', port=8000)