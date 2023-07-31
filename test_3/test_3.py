'''libraries need to create function'''
from datetime import datetime as dt


def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""

    try:
        dt.strptime(time_str, '%H:%M:%S')
    except Exception as exc:
        raise ValueError("Not a valid time") from exc

    list_of_nums = time_str.split(":")
    integer_form = list(map(int, list_of_nums))

    return sum(integer_form)
