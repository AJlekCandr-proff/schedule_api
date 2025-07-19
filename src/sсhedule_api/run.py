import uvicorn

from sсhedule_api.application.application import app

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", reload=True)
