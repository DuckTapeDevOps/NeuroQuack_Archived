import time
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

START = time.time()

health_status = True

def elapsed():
    running = time.time() - START
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}:{int(minutes):02d}:{int(seconds):02d}"

@app.get("/toggle")
async def toggle():
    global health_status
    health_status = not health_status
    return JSONResponse(content={"health_value": health_status})

@app.get("/health")
async def health():
    if health_status:
        return JSONResponse(content={"health": "healthy"})
    else:
        return JSONResponse(content={"health": "unhealthy"}, status_code=500)

@app.get("/")
async def root():
    return f"Hello World (Python)! (up {elapsed()})\n"
