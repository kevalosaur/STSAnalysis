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
    'all' : ['IRONCLAD', 'THE_SILENT', 'DEFECT', 'WATCHER']
}

if sys.argv[1] == 'WINDOWS':
    root_dir = ROOT_DIR_WINDOWS
else:
    root_dir = ROOT_DIR_MAC
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