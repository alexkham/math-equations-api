from fastapi import FastAPI
from app.routers import equations ,system

app = FastAPI(title="Math Expression API")

@app.get("/")
def root():
    return {"message": "Equation service is online!"}

app.include_router(equations.router, prefix="/equations", tags=["Equations"])
app.include_router(system.router, prefix="/equations", tags=["Equation Systems"])
