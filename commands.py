"""
Command dispatcher
"""
from modules.test import TestCommand
from modules.crypto import CryptoPriceCommand
from modules.room305d import Room305dCommand
from modules.tail import TailCommand

COMMANDS = {
    "\\test": TestCommand(),
    "\\crypto-price": CryptoPriceCommand(),
    "\\room305d": Room305dCommand(),
    "\\tail": TailCommand(),
}