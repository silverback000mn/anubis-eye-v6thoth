from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/status")
async def system_status():
    return {
        "project": "anubis-eye-v6thoth",
        "version": "1.0",
        "thoth_online": True,
        "last_update": datetime.now(pytz.timezone('America/Sao_Paulo')).isoformat()
    }
