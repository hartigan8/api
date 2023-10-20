from fastapi import FastAPI

app = FastAPI()

@app.post("/assignment/query")
def read_assignment_query(page: int, page_size: int):
    return {"message": "Hello World"}
