
from fastapi import HTTPException
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText



class EmailRequest(BaseModel):
    sender: str
    receiver: str
    subject: str
    body: str

def send_email(receiver_email, subject, body):
    # Your email sending logic here
    smtp_server = 'smtp.zoho.com'  # Update with your SMTP server
    # smtp_port = 465  # Update with your SMTP port
    smtp_port = 587  # Update with your SMTP port
    smtp_username = 'info@iotblitz.com' # Update with
    smtp_password = '8RhMYBfVYxA0'
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'info@iotblitz.com'
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")