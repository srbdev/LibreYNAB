from typing import List

from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm.session import Session

from db import crud, models, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/status")
async def status():
    return {"message": "LibreYNAB is live!"}

# Budget Model ***************************************************************#

@app.get("/budgets", response_class=HTMLResponse)
async def read_budgets(request: Request, db: Session = Depends(get_db)):
    budgets = crud.get_budgets(db)
    return templates.TemplateResponse("budget/index.html", {"request": request})

# Budget Model - END *********************************************************#