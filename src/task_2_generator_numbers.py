import re
from collections.abc import Callable


def generator_numbers(text: str):
    '''
    The function parses text and generates numbers from it.

    Args:
        text (str): text with real numbers separated from other text

    Yields:
        float: real numbers from text
    '''
    real_nums_pattern = r'\b\d+\.\d+\b'
    numbers = re.findall(real_nums_pattern, text)

    for number in numbers:
        yield float(number)


def sum_profit(text: str, func: Callable) -> float:
    '''
    The function sums real numbers from text.

    Args:
        text (str): text with real numbers separated by spaces
        func (Callable): function that generates real numbers from text

    Returns:
        float: sum of real numbers from text
    '''
    return sum(func(text))


if __name__ == '__main__':
    text = (
        "Загальний дохід працівника складається з декількох частин: 1000.01 "
        "як основний дохід, доповнений додатковими надходженнями 27.45 і "
        "324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}") # 1351.46
