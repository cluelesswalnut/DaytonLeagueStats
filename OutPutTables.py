import json

def createTable(statsFile, outputPath):
    with open(statsFile, 'r') as inFile:
        playerData = json.load(inFile)

    with open(outputPath, 'w') as outFile:
        outFile.write("player\twins\tloses\tties\tLeaguesPlayedIn\twin%\n")
        for player, stats in playerData.items():
            outFile.write(player)
            outFile.write('\t')
            outFile.write(str(stats['wins']))
            outFile.write('\t')
            outFile.write(str(stats['loses']))
            outFile.write('\t')
            outFile.write(str(stats['ties']))
            outFile.write('\t')
            outFile.write(str(stats['nLeagues']))
            outFile.write('\t')
            outFile.write(str(stats['wins']/(stats['loses'] + stats['ties'] + stats['wins'])))
            outFile.write('\n')

# createTable('PlayerStats.txt', 'PlayerStatsTable.txt')
# createTable('CaptianStats.txt', 'CaptianStatsTable.txt')


with open('DaytonLeaugeDataFirst.txt', 'r') as inFile:
    data = json.load(inFile)

with open('DataTable.txt', 'w') as outFile:
    outFile.write('PlayerName' + '\t' + 'League' + '\t' + 'teamName' + '\t' + 'captain1' + '\t' + 'captain2' + '\t' + 'wins' + '\t' + 'loses' + '\t' + 'ties' + '\n')
    for leagueKey, leagueValue in data.items():
        for teamKey, teamValue in leagueValue.items():
            captians = teamValue['captians']
            playerList = teamValue['players']
            for player in playerList:
                print(str(player))
                outFile.write(str(player))
                outFile.write('\t')
                outFile.write(str(leagueKey))
                outFile.write('\t')
                outFile.write(str(teamKey))
                outFile.write('\t')
                outFile.write(captians[0])
                outFile.write('\t')
                outFile.write(captians[1] if len(captians) > 1 else 'None')
                outFile.write('\t')
                outFile.write(str(teamValue['wins']))
                outFile.write('\t')
                outFile.write(str(teamValue['loses']))
                outFile.write('\t')
                outFile.write(str(teamValue['ties']))
                outFile.write('\n')