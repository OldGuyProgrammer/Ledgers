#
# Journals Inerpreter
#
# Take a Journals program exported data.
# Parse it into JSON format
#
# Jim Olivi 2025

from ReadJournalFiles import read_journal_files as rjf
from getFiles import get_journal_entries as gje
from pandas_svcs import PandasSvcs

print("Start Journals interpreter")

ps = PandasSvcs()
journalFiles = rjf("AppleJournalEntries/Entries")
for htmlfile in journalFiles:
    entry = gje(htmlfile)
    ps.add_row(entry)

print("End Journals Interpreter")