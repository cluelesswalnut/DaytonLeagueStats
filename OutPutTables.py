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

createTable('PlayerStats.txt', 'PlayerStatsTable.txt')
createTable('CaptianStats.txt', 'CaptianStatsTable.txt')