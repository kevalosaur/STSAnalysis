import analysistools
import pickle
import sys

enemies = dict()

with open(analysistools.PKL_PATH, 'rb') as file:
    runlist = pickle.load(file)

for run in runlist:
    if 'killed_by' in run:
        enemy = run['killed_by']
        if enemy not in enemies:
            enemies[enemy] = 0
        enemies[enemy] += 1

data = [{'enemy': enemy, 'frequency': enemies[enemy]} for enemy in enemies]
csv_file_path = sys.argv[1] if len(sys.argv) > 1 else 'output.csv'
analysistools.write_to_csv(data, csv_file_path)
analysistools.clean()