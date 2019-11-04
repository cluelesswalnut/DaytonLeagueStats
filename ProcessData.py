# create json with format:
# league name
#  - team name
#   - wins
#   - loses
#   - ties
#   - captians
#   - players

import json

def sumStats(player, playerStatsDict, teamDict):
    if player not in playerStatsDict:
        playerStatsDict[player] = {}
        playerStatsDict[player]['wins'] = 0
        playerStatsDict[player]['loses'] = 0
        playerStatsDict[player]['ties'] = 0
        playerStatsDict[player]['nLeagues'] = 0
        playerStatsDict[player]['eachLeagueWins'] = []
        playerStatsDict[player]['eachLeagueLoses'] = []
        playerStatsDict[player]['eachLeagueTies'] = []
    playerStatsDict[player]['wins'] += int(teamDict['wins'])
    playerStatsDict[player]['loses'] += int(teamDict['loses'])
    playerStatsDict[player]['ties'] += int(teamDict['ties'])
    playerStatsDict[player]['nLeagues'] += 1
    playerStatsDict[player]['eachLeagueWins'].append(int(teamDict['wins']))
    playerStatsDict[player]['eachLeagueLoses'].append(int(teamDict['loses']))
    playerStatsDict[player]['eachLeagueTies'].append(int(teamDict['ties']))

with open('DaytonLeaugeDataFirst.txt', 'r') as inFile:
    data = json.load(inFile)

print(data.keys())

playerStats = {}
captianStats = {}

for leagueKey, leagueValue in data.items():
    for teamKey, teamValue in leagueValue.items():
        captians = teamValue['captians']
        playerList = teamValue['players']
        for player in playerList:
            sumStats(player, playerStats, teamValue)
        for captian in captians:
            sumStats(captian, captianStats, teamValue)

with open('PlayerStats.txt', 'w') as outFile:
    json.dump(playerStats, outFile)

with open('CaptianStats.txt', 'w') as outFile:
    json.dump(captianStats, outFile)