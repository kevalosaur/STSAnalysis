#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
    echo "Usage: $0 character_name file_to_run [output_csv]"
    exit 1
fi

character_name=$1

if [ "$2" = "cards" ]; then
    file_to_run = "cardwinrates.py"
elif [ "$2" = "floorsReached" ]; then
    file_to_run = "deathfloors.py"
elif [ "$2" = "relics" ]; then
    file_to_run = "relicwinrates.py"
elif [ "$2" = "toughEnemies" ]; then
    file_to_run = "toughenemies.py"
else
    echo Invalid argument
    exit 1
fi

output_csv=${3:-output.csv}

python format_run_data.py "MAC" "$character_name"

python $file_to_run "$output_csv"
