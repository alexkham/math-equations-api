from fastapi import FastAPI

# Entry-level app that confirms this FastAPI project is running
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Equation Solver is online! Congratulations!"}
