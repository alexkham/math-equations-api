from fastapi import FastAPI
from app.routers import equations ,system, logic ,trigo,polynomials, derivatives ,exponents ,roots ,latex_converter,logarithms

app = FastAPI(title="Math Expression API")

@app.get("/")
def root():
    return {"message": "Equation service is online!"}

app.include_router(equations.router, prefix="/equations", tags=["Equations"])
app.include_router(system.router, prefix="/equations", tags=["Equation Systems"])
app.include_router(logic.router)
app.include_router(trigo.router)
app.include_router(polynomials.router)
app.include_router(derivatives.router)
app.include_router(exponents.router)
app.include_router(roots.router)
app.include_router(latex_converter.router)
app.include_router(logarithms.router)

