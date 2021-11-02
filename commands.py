"""
Command dispatcher
"""
from modules.test import test
from modules.crypto import crypto_price

COMMANDS = {
    "\\test": test,
    "\\crypto-price": crypto_price,
}