import argparse
from typing import List

from formatter import Styles, show_style


def show_all_styles(db_config):
    all_styles: List[str] = db_config.list()
    print('\n'.join(all_styles))


def chosen_style_exists(chosen_style: str) -> bool:
    return chosen_style in Styles.STYLE_MAPPING


def handle_arguments(parser: argparse.ArgumentParser, db_config):
    arguments = parser.parse_args()
    if arguments.show_styles:
        show_all_styles(db_config)
        return
    if not arguments.chosen_style:
        parser.print_help()
        return
    if not chosen_style_exists(arguments.chosen_style):
        print('chosen style does not exist')
        return
    show_style(Styles.get_style_by_name(arguments.chosen_style),
               arguments.text)


def init_argparser(db_config):
    parser = argparse.ArgumentParser(
        description='This is parser for the formatter flags')
    parser.add_argument('-a',
                        '--all-styles',
                        action='store_true',
                        dest='show_styles',
                        help='prints all avaliable styles')
    parser.add_argument('--style',
                        action='store',
                        dest='chosen_style',
                        help='sets formatting style for text')
    parser.add_argument('text',
                        action='store',
                        help='text for formatting',
                        nargs='?')
    handle_arguments(parser, db_config)
