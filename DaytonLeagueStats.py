# create json with format:
# league name
#  - team name
#   - wins
#   - loses
#   - ties
#   - captians
#   - players

import requests
from bs4 import BeautifulSoup
import json

page = requests.get("https://cincyultimate.org/profile/thomas-brewster")
soup = BeautifulSoup(page.content, 'html.parser')

leagues = soup.find_all("table", {"class":"table table-hover"})[1].find_all('a')

leagues = [i['href'] for i in leagues]
leagues = [i+'/teams' for i in leagues if "dayton" in i.lower()]
del leagues[0]
print(leagues)

data = {}

for index, league in enumerate(leagues):
    try:
        print(league)
        print(1.0 * index / len(leagues))
        data[league] = {}
        page = requests.get(league)
        soup = BeautifulSoup(page.content, 'html.parser')
        for index, teamHtml in enumerate(list(soup.find("div", {"class": "league-teams"}).children)):
            if(index % 2 != 1):
                continue
            name = teamHtml.find("p", {"class":"title"}).contents[0]
            # print(name)
            data[league][name] = {}
            record = teamHtml.find_all("strong", {"class":"text-info"})[1].contents[0].split(" - ")
            # print(record)
            data[league][name]['wins'] = record[0]
            data[league][name]['loses'] = record[1]
            data[league][name]['ties'] = record[2]
            captians = [i.contents[1] for i in teamHtml.find_all('a', {"target":"_new"})]
            # print(captians)
            data[league][name]['captians'] = captians
            teamId = teamHtml.find('a', {"data-team":True})['data-team']
            playerResponse = requests.get('https://cincyultimate.org/leagues/team_players', {'team_id': teamId})
            playerResponse = str(playerResponse.content).replace(r"\\", "")
            playerSoup = BeautifulSoup(playerResponse, 'html.parser')
            playersList = [i.contents[1].contents[0] for i in playerSoup.find_all('a')]
            # print(playersList)
            data[league][name]['players'] = playersList
    except Exception as e:
        print("_____________________FAILED_______________________ on " + league)
        print(str(e))

with open('DaytonLeaugeData.txt', 'w') as outFile:
    json.dump(data, outFile)

test = False
if test:
    import requests
    from bs4 import BeautifulSoup
    page = requests.get("https://cincyultimate.org/leagues/2019-summer-dayton/teams")
    soup = BeautifulSoup(page.content, 'html.parser')

    for index, teamHtml in enumerate(list(soup.find("div", {"class": "league-teams"}).children)):
        if(index % 2 != 1):
            continue
        name = teamHtml.find("p", {"class":"title"}).contents[0]
        print(name)
        # data[leagues]['teams'].append(name)
        record = teamHtml.find_all("strong", {"class":"text-info"})[1].contents[0].split(" - ")
        print(record)
        captians = [i.contents[1] for i in teamHtml.find_all('a', {"target":"_new"})]
        print(captians)
        teamId = teamHtml.find('a', {"data-team":True})['data-team']
        playerResponse = requests.get('https://cincyultimate.org/leagues/team_players', {'team_id': teamId})
        playerResponse = str(playerResponse.content).replace(r"\\", "")
        playerSoup = BeautifulSoup(playerResponse, 'html.parser')
        playersList = [i.contents[1].contents[0] for i in playerSoup.find_all('a')]
        print(playersList)