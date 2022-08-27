from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/user/{name}")
def read_user_name(name: str):
  return {"name": name}

if __name__ == "__main__":
  uvicorn.run("main:app")
