from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    if isinstance(value, str) and isinstance(arg, int):
        return str(value) * arg
    else:
        raise ValueError(
            f'Нельзя умножить {type(value)} на {type(arg)}')


STRONG_WORDS = ["php", "редиска"]


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise ValueError('Нельзя цензурировать не строку')

    for word in STRONG_WORDS:
        value = value.replace(word[1:], '*' * (len(word) - 1))

    return value
