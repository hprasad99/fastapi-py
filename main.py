from fastapi import FastAPI

app = FastAPI()

students = {
    1 : {
        "name" : "john",
        "age" : 17,
        "class" : "year 12"
    }
}

@app.get("/")
async def root():
    return {"message": "Hello World"}


