from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
import pytz

app = FastAPI()

# Configurar arquivos estáticos (CSS, JS, imagens)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/status")
async def status():
    return {
        "project": "anubis-eye-v6thoth",
        "version": "1.0",
        "thoth_online": True,
        "last_update": datetime.now(pytz.timezone('America/Sao_Paulo')).isoformat()
    }
