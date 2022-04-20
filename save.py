import parseran
import time
import os

def save(data_game, data_user, data_riwayat, data_kepemilikan):
    directory = input('Masukkan nama folder penyimpanan: ')
    if not os.path.isdir(directory):
        os.mkdir(directory)
    print()
    for i in range(4):
        print('Saving' + '.' * i, end='\r')
        time.sleep(0.5)
    parseran.matrix_to_csv(directory + '/game.csv', data_game)
    parseran.matrix_to_csv(directory + '/user.csv', data_user)
    parseran.matrix_to_csv(directory + '/riwayat.csv', data_riwayat)
    parseran.matrix_to_csv(directory + '/kepemilikan.csv', data_kepemilikan)
    print('\nData telah disimpan pada folder ' + directory + '!')