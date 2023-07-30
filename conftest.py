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


@pytest.fixture
def example_list():
    return [
        {
            "name": "Central London Employment Tribunal",
            "lat": 51.5158158439741,
            "lon": -0.118745425821452,
            "number": None,
            "cci_code": None,
            "magistrate_code": None,
            "slug": "central-london-employment-tribunal",
            "types": [
                "Tribunal"
            ],
            "address": {
                "address_lines": [
                    "Victory House",
                    "30-34 Kingsway"
                ],
                "postcode": "WC2B 6EX",
                "town": "London",
                "type": "Visiting"
            },
            "areas_of_law": [
                {
                    "name": "Employment",
                    "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                    "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                    "external_link_desc": "Information about the Employment Tribunal"
                }
            ],
            "displayed": True,
            "hide_aols": False,
            "dx_number": "141420 Bloomsbury 7",
            "distance": 1.29
        }
    ]
