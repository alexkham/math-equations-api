from fastapi import FastAPI
from app.routers import basic

app = FastAPI(title="Equation Solver API")

@app.get("/")
def root():
    return {"message": "Equation Solver is online!Congratulations!Inside the app"}

app.include_router(basic.router, prefix="/equations", tags=["Equation Solver"])
