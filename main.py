from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/status")
async def status():
    return {"message": "LibreYNAB is live!"}


# Budget Model ***************************************************************#
@app.get("/budgets", response_class=HTMLResponse)
async def budget_index(request: Request):
    return templates.TemplateResponse("budget/index.html", {"request": request})
# Budget Model - END *********************************************************#