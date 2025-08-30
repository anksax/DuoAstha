from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to DuoAstha API"}

@app.get("/religion/{name}")
def read_religion(name: str):
    return {"religion": name, "status": "content loading soon"}
