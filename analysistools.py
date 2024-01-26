import csv
import json
import os
import yaml

# Common helper functions for STS Analysis

PKL_PATH = 'runlist.pkl'
NAME_UPDATE = json.load(open('updatednames.json'))
BLESSINGS_VERBOSE = json.load(open('verboseblessings.json'))
with open('settings.yaml', 'r') as file:
    SETTINGS = yaml.safe_load(file)

ACT_3_WIN_FLR = 51
ACT_4_WIN_FLR = 56

def add_winrates(data):
    for item in data:
        item['winrate'] = item['wins']/item['runs_picked']

def clean():
    os.remove(PKL_PATH)

def get_win_flr(asc):
    if asc == 20:
        if [SETTINGS['win_condition']] == 'act3':
            return ACT_3_WIN_FLR + 1
        else:
            return ACT_4_WIN_FLR + 1
    else:
        if [SETTINGS['win_condition']] == 'act3':
            return ACT_3_WIN_FLR
        else:
            return ACT_4_WIN_FLR

def new_winrate_obj():
    return {
        'runs_picked' : 0,
        'wins' : 0,
        'losses' : 0
    }

def reformat_dict_to_csv(dct, label):
    formatted_list = []
    for key, subdct in dct.items():
        new_dict = {label : key, **subdct}
        formatted_list.append(new_dict)
    return formatted_list

def update_name(option, query):
    if option == 'blessings':
        if query in BLESSINGS_VERBOSE:
            return BLESSINGS_VERBOSE[query]['description']
    if query in NAME_UPDATE[option]:
        return NAME_UPDATE[option][query]
    else:
        return query
    
def updated_names_dict(option, dct):
    new_dct = dict()
    for key in dct.keys():
        new_dct[update_name(option, key)] = dct[key]
    return new_dct

def write_to_csv(data, filepath):
    with open(filepath, 'w', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(data)