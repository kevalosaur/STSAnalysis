import analysistools
import pickle
import sys

with open(analysistools.PKL_PATH, 'rb') as file:
    runlist = pickle.load(file)
analysistools.clean()

floors = [[] for i in range(57)]
first = True
for run in runlist:
    if first:
        print(run['gold_per_floor'])
        first = False
    for floor, gold in enumerate(run['gold_per_floor']):
        floors[floor].append(gold)

csv_file_path = sys.argv[1] if len(sys.argv) > 1 else 'output.csv'
analysistools.write_floormat_to_csv(floors, csv_file_path)
