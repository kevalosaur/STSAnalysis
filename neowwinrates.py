import analysistools
import pickle
import sys

with open(analysistools.PKL_PATH, 'rb') as file:
    runlist = pickle.load(file)

all_blessings = dict()

for run in runlist:
    # For the purposes of this analysis, a win is defined as defeating the Act 3 boss
    isWin = run['floor_reached'] >= analysistools.ACT3_WIN_FLR
    blessing = run['neow_bonus']
    if blessing not in all_blessings:
        all_blessings[blessing] = analysistools.new_winrate_obj()
    all_blessings[blessing]['runs_picked'] += 1
    if isWin:
        all_blessings[blessing]['wins'] += 1
    else:
        all_blessings[blessing]['losses'] += 1

# all_blessings = analysistools.updated_names_dict('blessings', all_blessings)
data = analysistools.reformat_dict_to_csv(all_blessings, 'blessing')
analysistools.add_winrates(data)

csv_file_path = sys.argv[1] if len(sys.argv) > 1 else 'output.csv'
analysistools.write_to_csv(data, csv_file_path)
analysistools.clean()