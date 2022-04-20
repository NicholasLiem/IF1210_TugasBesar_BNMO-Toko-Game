import save

def exit_program(data_user, data_user_baru, data_game, data_game_baru, data_riwayat, data_riwayat_baru, data_kepemilikan, data_kepemilikan_baru):
    if data_user != data_user_baru or data_game != data_game_baru or data_riwayat != data_riwayat_baru or data_kepemilikan != data_kepemilikan_baru:
        simpan = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)')[0]
        while simpan.lower() != 'y' or simpan.lower() != 'n':
            simpan = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)')[0]
        if simpan.lower() == 'y':
            save.save(data_game=data_game_baru, data_user=data_user_baru, data_riwayat=data_riwayat_baru, data_kepemilikan=data_kepemilikan_baru)