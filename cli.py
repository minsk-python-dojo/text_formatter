import argparse
from typing import List

from formatter import Style, show_style


def show_all_styles():
    all_styles: List[str] = [
        f'{style.value}. {style.name}'.lower() for style in Style.all_styles()
    ]
    print('\n'.join(all_styles))


def handle_arguments(arguments: argparse.Namespace):
    if arguments.show_styles:
        show_all_styles()


def init_argparser():
    parser = argparse.ArgumentParser(
        description='This is parser for the formatter flags')
    parser.add_argument('-a',
                        '--all-styles',
                        action='store_true',
                        dest='show_styles',
                        help='prints all avaliable styles')
    args = parser.parse_args()
    handle_arguments(args)
