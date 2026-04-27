from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

from services.email_service import send_email

app = FastAPI(title="Email Automation Service")


class EmailRequest(BaseModel):
    email: EmailStr
    subject: str
    message: str


@app.get("/")
async def health_check():
    return {"status": "ok", "message": "Email Automation Service is running."}


@app.post("/send-email")
async def api_send_email(payload: EmailRequest):
    try:
        send_email(payload.email, payload.subject, payload.message)
        return {"detail": "E-mail enviado com sucesso."}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
