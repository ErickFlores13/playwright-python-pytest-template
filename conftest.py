import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fixture to initialize Playwright
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

# Fixture to create a browser, context, and page
@pytest.fixture(scope="function")
def page(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()