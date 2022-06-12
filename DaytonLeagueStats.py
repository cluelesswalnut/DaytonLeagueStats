# This script scrapes the cincyultimate website and creates json with format:
# { 
#     "league name":
#     {
#         "team name":
#         {
#             wins: int,
#             loses: int,
#             ties: int,
#             captains: [],
#             players: []
#         },
#         more teams...
#     },
#     more leagues...
# }

from bs4 import BeautifulSoup
import json
import requests

# Parse all the leagues this player has been apart of.
ROOT_PLAYER_PROFILE = "https://cincyultimate.org/profile/thomas-brewster-19"

page = requests.get(ROOT_PLAYER_PROFILE)
soup = BeautifulSoup(page.content, 'html.parser')

# The league urls are in the second "table table-hover" on the page
leagues = soup.find_all("table", {"class":"table table-hover"})[1].find_all('a')
# get the urls for each league
leagues = [i['href'] for i in leagues]
# only keep dayton leagues and append '/teams' to access the teams that were part of the league
leagues = [i+'/teams' for i in leagues if "dayton" in i.lower()]

data = {}

for j, league in enumerate(leagues):
    # because we are scraping info from a website the format may be unpredictable and we may run into errors
    # catch the error and move on to the next league
    try:
        # print progress
        print(league)
        print(1.0 * j / len(leagues))

        data[league] = {}
        page = requests.get(league)
        soup = BeautifulSoup(page.content, 'html.parser')
        for index, teamHtml in enumerate(list(soup.find("div", {"class": "league-teams"}).children)):
            # every other html child is a new line, skip it
            if(index % 2 != 1):
                continue

            name = teamHtml.find("p", {"class":"title"}).contents[0]
            data[league][name] = {}

            # the second "text-info" gives the record in the form or 'W - L - T'
            record = teamHtml.find_all("strong", {"class":"text-info"})[1].contents[0].split(" - ")
            data[league][name]['wins'] = record[0]
            data[league][name]['loses'] = record[1]
            data[league][name]['ties'] = record[2]

            # the captains name is the second field in the 'target = "_new"' field
            captains = [i.contents[1] for i in teamHtml.find_all('a', {"target":"_new"})]
            data[league][name]['captains'] = captains

            # the team players is a pop up window. The information needs to be retrieved via a
            # separate request to: "https://cincyultimate.org/leagues/team_players?team_id=<teamId>"
            teamId = teamHtml.find('a', {"data-team":True})['data-team']
            playerResponse = requests.get('https://cincyultimate.org/leagues/team_players', {'team_id': teamId})
            playerResponse = str(playerResponse.content).replace(r"\\", "")
            playerSoup = BeautifulSoup(playerResponse, 'html.parser')

            # the name is embedded in a few layers of content
            playersList = [i.contents[1].contents[0] for i in playerSoup.find_all('a')]
            data[league][name]['players'] = playersList

    except Exception as e:
        print("_____________________FAILED_______________________ on " + league)
        print(str(e))

# output the scraped data to a json file
with open('DaytonLeagueData.json', 'w') as outFile:
    json.dump(data, outFile)