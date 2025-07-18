import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        app="schedule_api.application.application:app", host="0.0.0.0", reload=True
    )
