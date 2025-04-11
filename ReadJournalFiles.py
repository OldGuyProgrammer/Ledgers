#
# Journals Inerpreter
#
# Take a Journals program exported data, hopefully in JSON format,
# Parse it into a python dictionary and store it.
#
# Jim Olivi 2024

import os

def read_journal_files(journal_file_path):
    print("Enter ReadJournalFile")

    try:
        return os.listdir(journal_file_path)
    except FileNotFoundError:
        print(journal_file_path + ": not found")
        raise Exception("File not found")
    except PermissionError:
        print(journal_file_path + ": Permission denied")
        raise Exception("Permission denied")
    except OSError:
        print(journal_file_path + ": File not found")
        raise Exception("File not found")
    except:
        print(journal_file_path + ": Unexpected error")
        raise Exception("Unexpected error")

