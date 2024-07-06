
from dotenv import load_dotenv
import os

load_dotenv()

def login(page, username, password):
    page.goto(f"{os.getenv('BASE_URL')}/login")
    page.fill("input[name='username']", username)
    page.fill("input[name='password']", password)
    page.click("button[type='submit']")