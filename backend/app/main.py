from fastapi import FastAPI, Request, Header
from fastapi.responses import JSONResponse
from .analyzer import analyze_commit

app = FastAPI()

@app.get("/")
def home():
    return {"message": "✅ LivePatch AI backend is up and running!"}

@app.post("/webhook")
async def webhook_handler(request: Request, content_type: str = Header(None)):
    try:
        if content_type != "application/json":
            return JSONResponse(status_code=400, content={"error": "Unsupported Content-Type"})

        payload = await request.json()

        repo = payload.get("repository", {}).get("full_name", "Unknown repo")
        pusher = payload.get("pusher", {}).get("name", "Unknown user")
        commit_msg = payload.get("head_commit", {}).get("message", "No message")

        result = analyze_commit(repo, pusher, commit_msg)
        print("🧠 Analysis Result:", result)

        return JSONResponse(content={"status": "received", "analysis": result})

    except Exception as e:
        print(f"❌ Error processing webhook: {e}")
        return JSONResponse(status_code=500, content={"error": "Webhook processing failed"})
