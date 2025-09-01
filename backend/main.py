from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# -------------------
# Basic routes
# -------------------

@app.get("/")
def read_root():
    return {"message": "Welcome to DuoAstha API"}

@app.get("/religion/{name}")
def read_religion(name: str):
    return {"religion": name, "status": "content loading soon"}



projects = []

class Project(BaseModel):
    id: int
    title: str
    description: str
    status: str

@app.get("/projects")
def get_projects():
    return projects

@app.post("/projects")
def create_project(project: Project):
    projects.append(project.dict())
    return {"message": "Project created", "project": project}

@app.put("/projects/{project_id}")
def update_project(project_id: int, updated: Project):
    for i, proj in enumerate(projects):
        if proj["id"] == project_id:
            projects[i] = updated.dict()
            return {"message": "Project updated", "project": updated}
    raise HTTPException(status_code=404, detail="Project not found")

@app.delete("/projects/{project_id}")
def delete_project(project_id: int):
    for i, proj in enumerate(projects):
        if proj["id"] == project_id:
            projects.pop(i)
            return {"message": "Project deleted"}
    raise HTTPException(status_code=404, detail="Project not found")
