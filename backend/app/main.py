from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import get_connection

app = FastAPI(title="OnSite API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/workers")
def list_workers():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, full_name, hourly_rate FROM workers ORDER BY full_name"
            )
            workers = cur.fetchall()
    return {"workers": workers}
