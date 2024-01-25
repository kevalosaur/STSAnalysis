@echo off

if "%~1" == "-help" (
    echo Usage: %0 characterName fileToRun [outputCSV]
    echo Read README.md for more information.
    exit /b 1
)
if "%~1" == "-h" (
    echo Usage: %0 characterName fileToRun [outputCSV]
    echo Read README.md for more information.
    exit /b 1
)

if "%~2" == "" (
    echo Usage: %0 characterName fileToRun [outputCSV]
    exit /b 1
)

set characterName=%1

if "%~2" == "cards" (
    set fileToRun=cardwinrates.py
)
if "%~2" == "floorsReached" (
    set fileToRun=deathfloors.py
)
if "%~2" == "toughEnemies" (
    set fileToRun=toughenemies.py
)
if "%~2" == "relics" (
    set fileToRun=relicwinrates.py
)
if "%~2" == "blessings" (
    set fileToRun=neowwinrates.py
)

if "%fileToRun%" == "" (
    echo Invalid argument.
    echo Usage: %0 characterName fileToRun [outputCSV]
    exit /b 1
)

set outputCSV=%3

if "%outputCSV%" == "" set outputCSV=output.csv

python formatrundata.py "WINDOWS" "%characterName%"

python "%fileToRun%" "%outputCSV%"
