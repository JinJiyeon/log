import uvicorn
import time

if __name__ == "__main__":
    time.sleep(10)
    uvicorn.run("app.app:app", host='0.0.0.0', port=8000, reload=True)