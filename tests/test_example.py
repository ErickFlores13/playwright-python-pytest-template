import pytest
import os
from utils import utils

def test_ticket_lifecycle(page):
    try:
        # Login and create a ticket
        utils.login(page, os.getenv('USER_AGENTE'), os.getenv('PASSWORD_USERS'))
        ticket = utils.create_ticket(page, 'Test Subject', 'High', 'Test description')
        
        # Verify ticket information
        utils.verify_ticket_information(page, ticket)
    finally:
        # Add cleanup code if necessary
        pass