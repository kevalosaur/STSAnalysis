This tool offers a simple way to analyze data from your Slay the Spire (STS) runs.

To use this tool, run `./STSAnalyze characterName analysisToRun [outputCSV]`.

`characterName`: The name of the character to analyze. All four characters in the vanilla game are supported, as well as the following keywords:
- `all`: All four vanilla characters.
- `daily`: Daily runs.
- `modded`: All characters from mods.
- `allmodded`: All four vanilla characters plus all characters from mods.

`analysisToRun`: Which analysis shall be run by the program. This argument may have the following values:
- `cards`: Information on card picks and win rates.
- `relics`: Information on relic picks and win rates.
- `blessings`: Information on Neow blessings and win rates.
- `toughEnemies`: Information on deadliest enemies.
- `floorsReached`: Information on how often each floor has been reached.
- `gold`: Raw data on gold amassed by floor.
- `hp`: Raw data on current HP by floor.

`outputCSV`: Name of the .csv file to which analysis should be outputted. Defaults to `output.csv`.

Settings can be found and changed in `settings.yaml`.