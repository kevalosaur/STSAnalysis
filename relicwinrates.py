import analysistools
import pickle
import sys

with open(analysistools.PKL_PATH, 'rb') as file:
    runlist = pickle.load(file)

relics = dict()

for run in runlist:
    # For the purposes of this analysis, a win is defined as defeating the Act 3 boss
    isWin = run['floor_reached'] >= analysistools.ACT3_WIN_FLR
    for relic in run['relics']:
        if relic not in relics:
            relics[relic] = analysistools.new_winrate_obj()
        relics[relic]['runs_picked'] += 1
        if isWin:
            relics[relic]['wins'] += 1
        else:
            relics[relic]['losses'] += 1

data = analysistools.reformat_dict_to_csv(relics, 'relic')
analysistools.add_winrates(data)

csv_file_path = sys.argv[1] if len(sys.argv) > 1 else 'output.csv'
analysistools.write_to_csv(data, csv_file_path)
analysistools.clean()