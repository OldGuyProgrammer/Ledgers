#
# Journals Inerpreter
#
# Take a Journals program exported data.
# Parse it into JSON format
#
# Jim Olivi 2025

from ReadJournalFiles import ReadJournalFiles
from getFiles import GetJournalEntries

print("Start Journals interpreter")
journalFiles = ReadJournalFiles("AppleJournalEntries/Entries")
GetJournalEntries(journalFiles)
print("End Journals Interpreter")