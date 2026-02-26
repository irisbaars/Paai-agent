from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import os

app = FastAPI()

OWNER_PHONE = os.getenv("PAAI_OWNER_PHONE", "")
PASSPHRASE = os.getenv("PAAI_PASSPHRASE", "Paai good to go")

@app.post("/webhook/whatsapp")
async def whatsapp_webhook(request: Request):
    data = await request.form()
    from_number = data.get("From", "")

    # Only accept messages from you
    if not from_number.endswith(OWNER_PHONE):
        return PlainTextResponse("Ignored", status_code=200)

    body = (data.get("Body") or "").strip().lower()

    if body in ["hi paai", "hello paai"]:
        return PlainTextResponse(
            "👋 Hi, I’m Paai.\n"
            "I’m connected and listening.\n"
            "Actions are disabled until confirmed."
        )

    return PlainTextResponse(
        "👂 Message received.\n"
        "I’ll ask for confirmation before doing anything."
    )
