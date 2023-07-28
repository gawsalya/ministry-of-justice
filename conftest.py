import pytest


@pytest.fixture
def fake_sample_valid():
    return '03/11/21 08:51:01 INFO    :.main: *************** RSVP Agent started ***************'


@pytest.fixture
def fake_sample_invalid():
    return '01'


@pytest.fixture
def fake_sample_invalid_date():
    return '08:51:01 INFO    :.main: *************** RSVP Agent started ***************'


@pytest.fixture
def fake_sample_invalid_type():
    return '03/11/21 08:51:01 FAKE    :.main: *************** RSVP Agent started ***************'
