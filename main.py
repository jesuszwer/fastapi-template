from fastapi import FastAPI

main_app = FastAPI()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:main_app", host="0.0.0.0", port=3000, reload=True)
