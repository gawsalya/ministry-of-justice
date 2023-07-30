# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

from courts_functions import fetch_data, filter_by_court_distance, create_table, add_person_matching_court_to_table
import csv
from rich.console import Console

console = Console(record=True)

if __name__ == "__main__":

    courts_table = create_table()
    with open('people.csv', 'r', encoding='utf-8') as queries:
        lines = csv.reader(queries)
        next(lines)
        for query in lines:
            raw_data = fetch_data(query[1])
            court = filter_by_court_distance(raw_data, query[2])
            courts_table = add_person_matching_court_to_table(
                courts_table, query, court)

    console.print(courts_table)
