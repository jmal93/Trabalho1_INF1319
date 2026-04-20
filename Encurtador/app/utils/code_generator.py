from secrets import choice
from string import ascii_letters, digits
from typing import LiteralString


def generate_short_code() -> str:
    characters: LiteralString = ascii_letters + digits
    return ''.join(choice(characters) for _ in range(6))