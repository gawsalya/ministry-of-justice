from requests import get
from rich.table import Table


class APIError(Exception):
    """Describes an error triggered by a failing API call."""

    def __init__(self, message: str, code: int = 500):
        """Creates a new APIError instance."""
        self.message = message
        self.code = code


def fetch_data(postcode: str) -> list:
    """Returns a dict of court data from the API."""
    response = get(
        f"https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode={postcode}", timeout=10)
    if response.status_code == 200:
        return response.json()
    if response.status_code == 404:
        raise APIError("Unable to match for given postcode.", 404)
    if response.status_code == 500:
        raise APIError("Unable to connect to server.", 500)
    return None


def filter_by_court_distance(data: list, court_type) -> dict:
    '''returns the court with the correct type and least distance'''
    correct_type = []
    for court in data:
        if court_type in court['types']:
            correct_type.append(court)

    sorted_by_distance = sorted(
        correct_type, key=lambda court: court['distance'])

    if len(sorted_by_distance) == 0:
        raise IndexError('No court with matching criteria')

    return sorted_by_distance[0]


def create_table() -> Table:
    '''render a list of people and their data'''

    table = Table(title="Individual and Court")
    table.add_column("Name", justify="center")
    table.add_column("Home Postcode", justify="center")
    table.add_column("Desired Court Type", justify="center")
    table.add_column("Nearest Court", justify="center")
    table.add_column("dx_number", justify="center")
    table.add_column("Distance", justify="center")

    return table


def add_person_matching_court_to_table(table, person: str, court: dict) -> Table:

    table.add_row(person[0], person[1], person[2],
                  court['name'], str(court['dx_number']), str(court['distance']))
    return table
