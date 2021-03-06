"""
Module for formatter logic
"""

from enum import Enum, auto, unique
from typing import List, Dict, Callable


@unique
class Style(Enum):
    """
    Class for styles logic
    """
    HASH_BORDER = auto()
    PLAIN_TEXT = auto()
    AT_SIGN = auto()


class Styles:
    STYLE_MAPPING = {
        style.name.lower(): style
        for style in [
            Style.HASH_BORDER,
            Style.PLAIN_TEXT,
            Style.AT_SIGN,
        ]
    }

    @classmethod
    def get_style_by_name(cls, style_name: str):
        return cls.STYLE_MAPPING.get(style_name)


def show_style(chosen_style: Style, raw_input: str):
    """
    Format raw_input with chosen style
    """
    def show_plain(text: str):
        print(text)

    def show_hashborder(text: str):
        print(f'###\n{text}\n###')

    def show_at_sign(text: str):
        print(f'@@@@ {text} @@@')

    style_table: Dict[Style, Callable] = {
        Style.PLAIN_TEXT: show_plain,
        Style.HASH_BORDER: show_hashborder,
        Style.AT_SIGN: show_at_sign,
    }
    styler: Callable = style_table.get(chosen_style, show_plain)
    styler(raw_input)
