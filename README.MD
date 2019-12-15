## Text Formatter

### Задача

Ваша задача - реализовать программу для форматирования / стилизации пользовательского текста.
Первый этап - консольное приложение.
У пользователя должна быть возможность из консоли передать текст вашей программе, например:

```shell
$ text_formatter "Some user text"
```

или

```shell
$ text_formatter Some user text
```

После этого прорамма должна предложить пользователю выбор из нескольких стилей:

```shell
Please Choose style:

1. Plain text.
2. Hashtag border.
3. At sign surround.
>
```

После того как пользователь выбрал стиль, отображается отформатированный вариант его текста,
после чего он может выбрать другой стиль:

```shell
Please Choose style:

1. Plain text.
2. Hashtag border.
3. At sign surround.
> 2

####
Some user text
####


Please Choose style:

1. Plain text.
2. Hashtag border.
3. At sign surround.
> 
```

### Цель

- Познакомиться с патерном проектирования [MVC](https://ru.wikipedia.org/wiki/Model-View-Controller),
попрактиковаться в разботке приложений, используя данный патерн.
- Закрепить знания по разработке консольных приложений с предыдущих сессий.

### Ключевые понятия / инструменты

- `MVC`
- наследование
- `dataclass`
- `staticmethod`/`classmethod`
- `input`
- модуль `enum`
- модуль `typing`
- модуль `sys` (`sys.argv`)
