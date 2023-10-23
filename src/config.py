from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

SECRET_AUTH = "SECRET_AUTH"

SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

bot_token = '6474248626:AAGU3tZIQ9YQF09viXFUaPPqRlapV_F11OE'
tg_admin_id = 368647149

api_url = "http://127.0.0.1:8000"
