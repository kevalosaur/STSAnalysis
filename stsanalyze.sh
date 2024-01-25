#!/bin/bash

if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
    echo "Usage: $0 characterName fileToRun [outputCSV]"
    exit 1
fi

characterName=$1

if [ "$2" = "cards" ]; then
    fileToRun = "cardwinrates.py"
elif [ "$2" = "floorsReached" ]; then
    fileToRun = "deathfloors.py"
elif [ "$2" = "relics" ]; then
    fileToRun = "relicwinrates.py"
elif [ "$2" = "toughEnemies" ]; then
    fileToRun = "toughenemies.py"
elif [ "$2" = "blessings" ]; then
    fileToRun = "neowwinrates.py"
else
    echo Invalid argument.
    echo "Usage: $0 characterName fileToRun [outputCSV]"
    exit 1
fi

outputCSV=${3:-output.csv}

python formatrundata.py "MAC" "$characterName"

python $fileToRun "$outputCSV"
