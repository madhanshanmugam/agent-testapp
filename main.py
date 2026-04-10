from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

@app.get("/items/")
async def read_item(user_id: str = Query(...)):
    if not user_id.strip():
        raise HTTPException(status_code=400, detail="user_id cannot be empty")
    return {"user_id": user_id}
