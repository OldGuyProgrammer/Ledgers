# Journals Interpreter
#
# Save journal entries into a Pandas Dataframe
#
# Jim Olivi 2025
# Old Guy Programmer: www.oldguyprogrammer.com
#

from bs4 import BeautifulSoup
import os
import gllobal_data as gd

def get_journal_entries(htmlfile):

    path = os.getcwd() + "/AppleJournalEntries/Entries/" + htmlfile
    try:
        with open(path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, 'html.parser')
            # print(soup.prettify())
    except FileNotFoundError:
        print(htmlfile + ": not found")
        raise Exception("File not found")

    entry = {}
    p1_class = soup.find("p", class_='p1')
    if p1_class is None:
        print("No p1 class found")
    else:
        journal_date = p1_class.find("div", class_='pageHeader')
        if journal_date is None:
            text = ""
        else:
            text = journal_date.text
        entry.update({gd.key1: text})

        # Date captured, now get the title
        journal_title = p1_class.find("div", class_='title')
        if journal_title is None:
            text = ""
        else:
            text = journal_title.text
        entry.update({gd.key2: text})

    # Title captured, now get the text
    p2_class = soup.find("p", class_='p2')
    if p2_class is None:
        print("No p2 text found.")
    else:
        text_tuple = []
        text = p2_class.find_all("span")
        for t in text:
            text_tuple.append(t.text)
        entry.update({gd.key3: text_tuple})

    return entry
