from fastapi import FastAPI




app = FastAPI(
    title="OrderFlow API",
    description="Real-Time O rder Management Platform",
    version="1.0",
)


@app.get("/")
def root():
    return {
        "message":"Welcome to OrderFlow",
        "status":"running"
    }



