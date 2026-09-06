from fastapi import FastAPI


app = FastAPI(
    title="GitHub Actions FastAPI Demo",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "FastAPI GitHub Actions Demo"
    }


@app.get("/api/hello")
def hello():
    return {
        "message": "Hello from my DEV branch!",
        "version": "2.0.0"
    }


@app.get("/api/status")
def status():
    return {
        "status": "ok"
    }
