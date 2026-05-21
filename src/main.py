from fastapi import FastAPI


app = FastAPI()


@app.get("/", tags=["home"])
async def home() -> dict:
    return {"message": "V165161616161", "status": True}
