from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CalculatorRequest(BaseModel):
    a: float
    b: float
    operation: str  # "add", "subtract", "multiply", "divide"

@app.post("/calculator")
def calculator(request: CalculatorRequest):
    a, b, op = request.a, request.b, request.operation.lower()

    if op == "add":
        result = a + b
    elif op == "subtract":
        result = a - b
    elif op == "multiply":
        result = a * b
    elif op == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        result = a / b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation. Use add, subtract, multiply, or divide.")

    return {"operation": op, "a": a, "b": b, "result": result}
