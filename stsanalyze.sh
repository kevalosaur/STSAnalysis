#!/bin/bash

if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
    echo "Usage: $0 characterName fileToRun [outputCSV]"
    exit 1
fi

characterName=$1

if [ "$2" = "cards" ]; then
    fileToRun = "scripts/cardwinrates.py"
elif [ "$2" = "floorsReached" ]; then
    fileToRun = "scripts/deathfloors.py"
elif [ "$2" = "relics" ]; then
    fileToRun = "scripts/relicwinrates.py"
elif [ "$2" = "toughEnemies" ]; then
    fileToRun = "scripts/toughenemies.py"
elif [ "$2" = "blessings" ]; then
    fileToRun = "scripts/neowwinrates.py"
elif [ "$2" = "gold" ]; then
    fileToRun = "scripts/goldperfloor.py"
elif [ "$2" = "hp" ]; then
    fileToRun = "scripts/hpperfloor.py"
else
    echo Invalid argument.
    echo "Usage: $0 characterName fileToRun [outputCSV]"
    exit 1
fi

outputCSV=${3:-output.csv}

python scripts/formatrundata.py "MAC" "$characterName"

python $fileToRun "$outputCSV"
