import pytest
import requests_mock

from courts_functions import APIError, fetch_data, filter_by_court_distance


def test_raises_404_error(requests_mock):
    """Checks that fetch_data raises the correct error upon a 404 response."""
    requests_mock.get(
        "https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode=fake", status_code=404)

    with pytest.raises(APIError) as error:
        fetch_data("fake")

    assert error.value.message == "Unable to match for given postcode."
    assert error.value.code == 404


def test_raises_500_error(requests_mock):
    """Checks that fetch_data raises the correct error upon a 500 response."""
    requests_mock.get(
        "https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode=fake", status_code=500)

    with pytest.raises(APIError) as error:
        fetch_data("fake")

    assert error.value.message == "Unable to connect to server."
    assert error.value.code == 500


def test_no_matching_type_filter_by_court_distance(example_list):
    '''test to see error raised when no matching data is found'''

    with pytest.raises(IndexError) as error:
        filter_by_court_distance(example_list, 'Family Court')

    assert str(error.value) == 'No court with matching criteria'
