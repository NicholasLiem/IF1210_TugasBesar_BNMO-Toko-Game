import argparse
import parseran
import os

data_user = []
data_game = []
data_riwayat = []
data_riwayat_baru = []
data_kepemilikan = []

directory = ''

def load(path_to_folder):
    if os.path.isdir(path_to_folder):
        data_game = parseran.csv_to_matrix(path_to_folder + '/game.csv')
        data_user = parseran.csv_to_matrix(path_to_folder + '/user.csv')
        data_riwayat = parseran.csv_to_matrix(path_to_folder + '/riwayat.csv')
        data_kepemilikan = parseran.csv_to_matrix(path_to_folder + '/kepemilikan.csv')

        return data_game, data_user, data_riwayat, data_kepemilikan
    else:
        ...

def save(path_to_folder):
    ...

def exit(save_change):
    ...