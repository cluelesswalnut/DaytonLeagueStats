import requests
from bs4 import BeautifulSoup

page = requests.get("https://cincyultimate.org/leagues/2019-fall-dayton/teams")
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

respons = requests.get('https://cincyultimate.org/leagues/team_players', {'team_id': '1670'})
print(respons.content)