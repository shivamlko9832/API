from fastapi import FastAPI

app = FastAPI()

@app.get("/addition")
def add(a:int,b:int):
    return a + b

from pydantic import BaseModel

class SubtractRequest(BaseModel):
    a: int
    b: int

@app.post("/subtract")
def subtract(request: SubtractRequest):
    return request.a - request.b



