@echo off

if "%~2" == "" (
    echo Usage: %0 character_name file_to_run [output_csv]
    exit /b 1
)

set character_name=%1

if "%~2" == "cards" (
    set file_to_run=cardwinrates.py
)
else if "%~2" == "floorsReached" (
    set file_to_run=deathfloors.py
)
else if "%~2" == "toughEnemies" (
    set file_to_run=toughenemies.py
)
else if "%~2" == "relics" (
    set file_to_run=relicwinrates.py
)
else (
    echo Invalid argument
    exit /b 1
)

set output_csv=%3

if "%output_csv%" == "" set output_csv=output.csv

python formatrundata.py "WINDOWS" "%character_name%"

python "%file_to_run%" "%output_csv%"
