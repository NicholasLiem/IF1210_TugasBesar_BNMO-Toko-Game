import argparse
import parseran
import os
import time

data_user = []
data_game = []
data_riwayat = []
data_riwayat_baru = []
data_kepemilikan = []

directory = ''

def load(directory, data_game, data_user, data_riwayat, data_kepemilikan):
    if os.path.isdir(directory):
        for i in range(4):
            print('Loading' + '.' * i, end='\r')
            time.sleep(0.5)
        print()
        print('\nSelamat datang di antarmuka "Binomo"\n')
        data_game = parseran.csv_to_matrix(directory + '/game.csv')
        data_user = parseran.csv_to_matrix(directory + '/user.csv')
        data_riwayat = parseran.csv_to_matrix(directory + '/riwayat.csv')
        data_kepemilikan = parseran.csv_to_matrix(directory + '/kepemilikan.csv')
        return True
    else:
        print(f'Folder "{directory}" tidak ditemukan.')
        return False

def save(directory):
    ...

def exit(save_change):
    ...

load('Data', data_game=data_game, data_user=data_user, data_riwayat=data_riwayat, data_kepemilikan=data_kepemilikan)