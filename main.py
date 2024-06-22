from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a path operation decorator with the GET method
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Define another endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
