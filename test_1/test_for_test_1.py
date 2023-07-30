
from test_1 import is_log_line


def test_line_is_valid(fake_sample_valid):
    result = is_log_line(fake_sample_valid)

    assert result is True


def test_line_is_invalid(fake_sample_invalid):
    result = is_log_line(fake_sample_invalid)

    assert result == None


def test_line_is_invalid_no_date(fake_sample_invalid_date):
    result = is_log_line(fake_sample_invalid_date)

    assert result == None


def test_line_is_invalid_no_error_type(fake_sample_invalid_type):
    result = is_log_line(fake_sample_invalid_type)

    assert result == None
