"""
Command dispatcher
"""
from modules.test import test
from modules.crypto import crypto_ticker

COMMANDS = {
    "\\test": test,
    "\\crypto-ticker": crypto_ticker,
}