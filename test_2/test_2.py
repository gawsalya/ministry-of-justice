'''libraries required to get information from API and format data'''
import csv
from rich.console import Console
from courts_functions import fetch_data, filter_by_court_distance, create_table, add_person_matching_court_to_table

console = Console(record=True)

if __name__ == "__main__":

    courts_table = create_table()
    with open('people.csv', 'r', encoding='utf-8') as queries:
        lines = csv.reader(queries)
        next(lines)

        for query in lines:
            raw_data = fetch_data(query[1])
            try:
                court = filter_by_court_distance(raw_data, query[2])
            except IndexError:
                court = {"name": "Not found",
                         "dx_number": None, "distance": None}

            courts_table = add_person_matching_court_to_table(
                courts_table, query, court)

    console.print(courts_table)
