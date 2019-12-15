import sys
from dataclasses import dataclass
from enum import Enum, unique, auto

# Model start


@unique
class TextStyle(Enum):
    PLAIN_TEXT = auto()
    HASHTAG_BORDER = auto()
    AT_SIGN_BORDER = auto()


@dataclass
class UserInput:
    text: str
    # TODO: Maybe better to place inside TerminalFormatter
    style: TextStyle
# Model end

# View start


class AbstractFormatter:
    def __init__(self, user_input: UserInput):
        self.user_input = user_input

    def show(self):
        raise NotImplementedError


class TerminalFormatter(AbstractFormatter):
    def __init__(self, user_input: UserInput):
        super().__init__(user_input)
        self.styles_table = {
            TextStyle.PLAIN_TEXT: self._plain_style,
            TextStyle.HASHTAG_BORDER: self._hashtag_style,
            TextStyle.AT_SIGN_BORDER: self._at_sign_style,
        }

    def _plain_style(self) -> str:
        return self.user_input.text

    def _hashtag_style(self) -> str:
        return f'####\n{self.user_input.text}\n####'

    def _at_sign_style(self) -> str:
        return f'@@@@ {self.user_input.text} @@@@'

    def show(self):
        style_method = self.styles_table.get(
            self.user_input.style,
            TextStyle.PLAIN_TEXT
        )
        print(style_method())
# View end


# Controller start
def style_menu(term_formatter: TerminalFormatter):
    styles = [
        TextStyle.PLAIN_TEXT,
        TextStyle.HASHTAG_BORDER,
        TextStyle.AT_SIGN_BORDER,
    ]
    choise_items: str = '\n'.join(
        f'{i + 1}. {style}' for i, style in enumerate(styles)
    )
    while True:
        choice: str = input(f'Choose style:\n{choise_items}\nType exit to exit\n>')
        if choice.strip().lower() == 'exit':
            print('Exiting the program.')
            return
        try:
            style_index: int = int(choice)
            style_index -= 1
        except ValueError:
            print('Choose a proper style number')
            continue
        if style_index < 0 or style_index >= len(styles):
            print('Wrong style number')
            continue
        #TODO: add property
        term_formatter.user_input.style = styles[style_index]
        term_formatter.show()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Not enough args!')
        sys.exit(1)
    user_input_text = ' '.join(sys.argv[1:])
    user_input = UserInput(user_input_text, TextStyle.PLAIN_TEXT)
    term_formatter = TerminalFormatter(user_input)
    style_menu(term_formatter)
