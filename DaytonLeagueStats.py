import requests
from bs4 import BeautifulSoup

page = requests.get("https://cincyultimate.org/profile/thomas-brewster")
soup = BeautifulSoup(page.content, 'html.parser')

leagues = soup.find_all("table", {"class":"table table-hover"})[1].find_all('a')

leagues = [i['href'] for i in leagues]
leagues = [i for i in leagues if "dayton" in i.lower()]
print(leagues)


page = requests.get("https://cincyultimate.org/leagues/2019-summer-dayton/teams")
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
# print(list(soup.find("div", {"class": "league-teams"}).children)[1].find("p", {"class":"title"}))

for index, teamHtml in enumerate(list(soup.find("div", {"class": "league-teams"}).children)):
    if(index % 2 != 1):
        continue
    name = teamHtml.find("p", {"class":"title"}).contents
    print(name)
    record = teamHtml.find_all("strong", {"class":"text-info"})[1].contents[0].split(" - ")
    print(record)
    captians = [i.contents[1] for i in teamHtml.find_all('a', {"target":"_new"})]
    print(captians)
    teamId = teamHtml.find('a', {"data-team":True})['data-team']
    playerResponse = requests.get('https://cincyultimate.org/leagues/team_players', {'team_id': teamId})
    playerResponse = str(playerResponse.content).replace(r"\\", "")
    playerSoup = BeautifulSoup(playerResponse, 'html.parser')
    playersList = [i.contents[1].contents for i in playerSoup.find_all('a')]
    print(playersList)


response = requests.get('https://cincyultimate.org/leagues/team_players', {'team_id': '1670'})
# print(response.content.prettify())