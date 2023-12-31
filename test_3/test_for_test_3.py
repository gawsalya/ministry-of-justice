'''libraries required for testing'''
import pytest
from test_3 import sum_current_time


def test_to_check_input_is_string(not_a_string):
    '''test to see error if not a string'''
    with pytest.raises(ValueError):
        sum_current_time(not_a_string)


def test_if_sum_returned_for_correct_time(fake_correct_time):
    '''test to check if the sum is return for the correct time'''
    result = sum_current_time(fake_correct_time)

    assert result == 6
    assert isinstance(fake_correct_time, str) is True


def test_if_error_raised_for_incorrect_time(fake_incorrect_time):
    '''test to see an error is raised if time is not a real time'''
    with pytest.raises(ValueError):
        sum_current_time(fake_incorrect_time)


def test_if_error_if_invalid_format(bad_format):
    '''test to see an error if raised if the date is not in the correct format'''
    with pytest.raises(ValueError):
        sum_current_time(bad_format)
