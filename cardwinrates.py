import analysistools
import pickle
import sys

def clean_deck(cardlist):
    newlist = [card[:card.index('+')] if '+' in card else card for card in cardlist]
    return set(newlist)

with open(analysistools.PKL_PATH, 'rb') as file:
    runlist = pickle.load(file)

all_cards = dict()

for run in runlist:
    # For the purposes of this analysis, a win is defined as defeating the Act 3 boss
    isWin = run['floor_reached'] >= analysistools.ACT3_WIN_FLR
    card_set = clean_deck(run['master_deck'])
    for card in card_set:
        if card not in all_cards:
            all_cards[card] = analysistools.new_winrate_obj()
        all_cards[card]['runs_picked'] += 1
        if isWin:
            all_cards[card]['wins'] += 1
        else:
            all_cards[card]['losses'] += 1

data = analysistools.reformat_dict_to_csv(all_cards, 'card')
analysistools.add_winrates(data)

csv_file_path = sys.argv[1] if len(sys.argv) > 1 else 'output.csv'
analysistools.write_to_csv(data, csv_file_path)
analysistools.clean()