import analysistools
import json
import os
import pickle
import sys

ROOT_DIR_WINDOWS = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\SlayTheSpire\\runs"
ROOT_DIR_MAC = "~\\Library\\Application Support\\Steam\\steamapps\\common\\SlayTheSpire\\runs"

NAME_MAP = {
    'ironclad' : ['IRONCLAD'],
    'silent' : ['THE_SILENT'],
    'defect' : ['DEFECT'],
    'watcher' : ['WATCHER'],
    'the ironclad' : ['IRONCLAD'],
    'the silent' : ['THE_SILENT'],
    'the defect' : ['DEFECT'],
    'the watcher' : ['WATCHER'],
    'daily' : ['DAILY'],
    'all' : ['IRONCLAD', 'THE_SILENT', 'DEFECT', 'WATCHER']
}

if analysistools.SETTINGS['runs_file_path'] != 'DEFAULT':
    root_dir = analysistools.SETTINGS['runs_file_path']
elif sys.argv[1] == 'WINDOWS':
    root_dir = ROOT_DIR_WINDOWS
else:
    root_dir = ROOT_DIR_MAC

NAME_MAP['modded'] = []
for chardir in os.listdir(root_dir):
    NAME_MAP[chardir.lower()] = [chardir]
    if chardir not in NAME_MAP['all'] and chardir != 'DAILY':
        NAME_MAP['modded'].append(chardir)
NAME_MAP['allmodded'] = NAME_MAP['all'] + NAME_MAP['modded']

if sys.argv[2].lower() in NAME_MAP:
    dirs = [root_dir + '\\' + name for name in NAME_MAP[sys.argv[2].lower()]]
else:
    print("Invalid character.")
    exit(1)

runlist = []
for dir in dirs:
    runlist += [json.load(open(dir + '\\' + fn)) for fn in os.listdir(dir)]
with open(analysistools.PKL_PATH, 'wb') as file:
    pickle.dump(runlist, file)