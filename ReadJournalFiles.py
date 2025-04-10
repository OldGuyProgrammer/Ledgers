#
# Journals Inerpreter
#
# Take a Journals program exported data, hopefully in JSON format,
# Parse it into a python dictionary and store it.
#
# Jim Olivi 2024

import json
import os

class ReadJournalFiles:
    def __init__(self, journalFilePath):
        print("Enter ReadJournalFile")

        try:
            self.files = os.listdir(journalFilePath)
        except FileNotFoundError:
            print(journalFilePath + ": not found")
            raise Exception("File not found")
        except PermissionError:
            print(journalFilePath + ": Permission denied")
            raise Exception("Permission denied")
        except OSError:
            print(journalFilePath + ": File not found")
            raise Exception("File not found")
        except:
            print(journalFilePath + ": Unexpected error")
            raise Exception("Unexpected error")


        print("Journal file object created.")
