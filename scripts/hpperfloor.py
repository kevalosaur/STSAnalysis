import analysistools
import pickle
import sys

with open(analysistools.PKL_PATH, 'rb') as file:
    runlist = pickle.load(file)
analysistools.clean()

floors = [[] for _ in range(57)]
for run in runlist:
    for floor, gold in enumerate(run['current_hp_per_floor']):
        floors[floor].append(gold)

csv_file_path = sys.argv[1] if len(sys.argv) > 1 else 'output.csv'
analysistools.write_floormat_to_csv(floors, csv_file_path)
