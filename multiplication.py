from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MultiplyRequest(BaseModel):
    a: int
    b: int

@app.post("/multiply")
def multiply(request: MultiplyRequest):
    return request.a * request.b
