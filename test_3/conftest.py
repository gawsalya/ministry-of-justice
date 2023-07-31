import pytest


@pytest.fixture
def fake_correct_time():
    return '01:02:03'


@pytest.fixture
def fake_incorrect_time():
    return '29:30:44'


@pytest.fixture
def bad_format():
    return '22:00'


@pytest.fixture
def not_a_string():
    return (120032)
