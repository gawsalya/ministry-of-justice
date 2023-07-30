import pytest

from courts_functions import APIError, fetch_data, filter_by_court_distance


def test_raises_404_error(requests_mock):
    """Checks that fetch_data raises the correct error upon a 404 response."""
    requests_mock.get(
        "https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode={postcode}", status_code=404)
    with pytest.raises(APIError) as error:
        fetch_data("fake")

    assert error.value.message == "Unable to match for given postcode."
    assert error.value.code == 404
