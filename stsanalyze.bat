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
    set fileToRun=scripts/cardwinrates.py
)
if "%~2" == "floorsReached" (
    set fileToRun=scripts/deathfloors.py
)
if "%~2" == "toughEnemies" (
    set fileToRun=scripts/toughenemies.py
)
if "%~2" == "relics" (
    set fileToRun=scripts/relicwinrates.py
)
if "%~2" == "blessings" (
    set fileToRun=scripts/neowwinrates.py
)
if "%~2" == "gold" (
    set fileToRun=scripts/goldperfloor.py
)
if "%~2" == "hp" (
    set fileToRun=scripts/hpperfloor.py
)

if "%fileToRun%" == "" (
    echo Invalid argument.
    echo Usage: %0 characterName fileToRun [outputCSV]
    exit /b 1
)

set outputCSV=%3

if "%outputCSV%" == "" set outputCSV=output.csv

python scripts/formatrundata.py "WINDOWS" "%characterName%"

python "%fileToRun%" "%outputCSV%"
