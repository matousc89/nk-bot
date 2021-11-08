"""
Command dispatcher
"""
from modules.test import TestCommand
from modules.crypto import CryptoPriceCommand

COMMANDS = {
    "\\test": TestCommand(),
    "\\crypto-price": CryptoPriceCommand(),
}