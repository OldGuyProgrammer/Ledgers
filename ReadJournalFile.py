#
# Journals Inerpreter
#
# Take a Journals program exported data, hopefully in JSON format,
# Parse it into a python dictionary and store it.
#
# Jim Olivi 2024

import json

class ReadJournalFile:
    def __init__(self):
        print("Enter ReadJournalFile")

        with (open("Journal.json", "r") as json_file):
            json_data = json.load(json_file)

            for key, value in json_data.items():
                print(key)
                print(value)

        print("Journal file object created.")
