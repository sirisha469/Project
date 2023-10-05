from fastapi import BackgroundTasks, UploadFile, File, Form, Depends, HTTPException, status

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from app.config import settings
from app import schemas,models, oauth2
from dotenv import dotenv_values

conf_credentials = dotenv_values(".env")

conf = ConnectionConfig(
  MAIL_USERNAME = "your mail",
  MAIL_PASSWORD = "your password", 
  MAIL_FROM= "your mail",
  MAIL_PORT = 587,
  MAIL_SERVER = "smtp.gmail.com",
  MAIL_TLS = True,
  MAIL_SSL = False,
  USE_CREDENTIALS = True
)


async def send_email(email: schemas.EmailSchema, user:models.Signup):

  token_data = {
    "id": user.id
  }
  token = oauth2.create_access_token(token_data)

  template = f"""
    <!DOCTYPE html>
    <html>
      <head>

      </head>
      <body>
        <div style = "display: flex; align-items: center; justify-content: center; flex-direction: column">

          <h3>Account Verification</h3>
          <br>

          <p>Thanks for choosing, please click on the button below to verify your account</p>

          <a style = "margin-top: 1rem; padding: 1rem; border-radius: 0.5rem; font-size: 1rem; text-decoration: none; background: #0275d8; color: white;" href = "http://localhost:8000/verification/?token={token}">Verify your email</a>

          <p>Please kindly ignore this email if you did not register for the web page and nothing will happend. Thanks</p>

        </div>
      </body>
    </html>
  """

  message = MessageSchema(
    subject = "Account Verification Email",
    recipients = email,
    body = template,
    subtype = "html"
  )

  fm = FastMail(conf)
  await fm.send_message(message = message)

