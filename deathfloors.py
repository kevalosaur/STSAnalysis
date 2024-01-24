import analysistools
import pickle
import sys

NUM_FLOORS = 57
floors = [0] * NUM_FLOORS

with open(analysistools.PKL_PATH, 'rb') as file:
    runlist = pickle.load(file)

for run in runlist:
    floors[run['floor_reached']] += 1

data = [{'floor': floor, 'frequency': freq} for floor, freq in enumerate(floors)][1:]
csv_file_path = sys.argv[1] if len(sys.argv) > 1 else 'output.csv'
analysistools.write_to_csv(data, csv_file_path)
analysistools.clean()