from decimal import Decimal, InvalidOperation
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[Decimal, None, None]:
    text_list = text.split(" ")
    for item in text_list:
        value = try_cast_Decimal(item)

        if value:
            yield value
        else:
            continue


def try_cast_Decimal(str: str) -> None | Decimal:
    try:
        return Decimal(str)
    except InvalidOperation:
        return None


def sum_profit(
    text: str, func: Callable[[str], Generator[Decimal, None, None]]
) -> Decimal:
    sum = Decimal(0)
    for value in func(text):
        sum = sum + value
    return sum
