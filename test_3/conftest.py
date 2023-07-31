'''library for testing'''
import pytest


@pytest.fixture
def fake_correct_time():
    '''fake correct time for testing'''
    return '01:02:03'


@pytest.fixture
def fake_incorrect_time():
    '''fake incorrect time for testing'''
    return '29:30:44'


@pytest.fixture
def bad_format():
    '''poorly formatted time'''
    return '22:00'


@pytest.fixture
def not_a_string():
    '''time as integers'''
    return (120032)
