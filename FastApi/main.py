# first create the virtual environment in the terminal of the folder with the command --> python -m venv venv
# activate the environment by running --> venv/scripts/activate
# install fastapi uvicorn (server) pydantic (data validation library) --> pip install fastapi uvicorn pydantic
# Start a local server for your FastAPI (or ASGI) app by running --> uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Hello():
    return {"message": "Hello World!!"}
