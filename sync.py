from fastapi import FastAPI

app = FastAPI()

status = {"agents": 0, "running": False}

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.post("/start_agents")
async def start_agents():
    status["agents"] += 1
    status["running"] = True
    return status

@app.post("/stop_agents")
async def stop_agents():
    status["agents"] = max(0, status["agents"] - 1)
    if status["agents"] == 0:
        status["running"] = False
    return status

@app.get("/status")
async def get_status():
    return status

@app.get("/")
async def index():
    return {
        "routes": {
            "/healthz": "check health",
            "/start_agents": "start workers",
            "/stop_agents": "stop workers",
            "/status": "status view"
        }
    }
