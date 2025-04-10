# Journals Inerpreter
#
# Save journal entries into a Pandas Dataframe
#
# Jim Olivi 2025
# Old Guy Programmer: www.oldguyprogrammer.com
#

from bs4 import BeautifulSoup
import os

class GetJournalEntries:
    def __init__(self, journalFiles):

        for htmlFile in journalFiles.files:
            # print(os.getcwd() + "/" + htmlFile)
            path = os.getcwd() + "/AppleJournalEntries/Entries/" + htmlFile
            try:
                with open(path, "r", encoding="utf-8") as f:
                    soup = BeautifulSoup(f, 'html.parser')
                    # print(soup.prettify())
            except FileNotFoundError:
                print(htmlFile + ": not found")
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
                entry.update({"journal_date": text})

                # Date captured, now get the title
                journal_title = p1_class.find("div", class_='title')
                if journal_title is None:
                    text = ""
                else:
                    text = journal_title.text
                entry.update({"journal_title": text})

            # Title captured, now get the text
            p2_class = soup.find("p", class_='p2')
            if p2_class is None:
                print("No p2 text found.")
            else:
                text_tuple = []
                text = p2_class.find_all("span")
                for t in text:
                    text_tuple.append(t.text)
                entry.update({"journal_lines": text_tuple})

            print(entry)

        #
        # Get the list of players.
        #

        # players = soup.find_all('a', attrs={'class': 'player-link'})
        # if players is None or len(players) == 0:
        #     tksvcs.error_msg(title='No Players Found', msg='This is probably not a Minor league Baseball team web site.')
        #     return
        #
        # player_first_name_list = [player_name.text.strip().split()[0] for player_name in players]
        # player_last_name_list = [''.join(player_name.text.strip().split()[1:]) for player_name in players]
        # jersey_list = soup.find_all('span', attrs={'class': 'jersey'})
        # jersey_numbers = [number.text for number in jersey_list][:len(player_last_name_list)]
        # ba.player_info = {'First Name': player_first_name_list,
        #                'Last Name': player_last_name_list,
        #                'Jersey Number': jersey_numbers}
        #
        # roster_obj = PandasSvcs(dict=ba.player_info)
        # dr.display_roster(roster_obj)