# This script takes output from `ProcessData.py` and formats it in tables
# that are easy to process with excel or similar tools

import json

def create_table(statsFile, outputPath):
    """
    Create a table out of player data in JSON files

    @param  statsFile   The JSON file containing the stats to tabulate
    @param  outputPath  The output file to write the table to
    """
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

# create the tables from the data processed in `ProcessData.py`
create_table('PlayerStats.json', 'PlayerStatsTable.txt')
create_table('CaptainStats.json', 'CaptainStatsTable.txt')
