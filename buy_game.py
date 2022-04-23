import operasi_array as arr
import constant as c

def buy_game(data_game, data_kepemilikan, data_user, data_riwayat, username):
    user_id = username
    game_id = input(c.bg_idGame)

    row_data_user = arr.find_row_id(data_user, c.csvID_user_username, user_id)
    data_user_baris = data_user[row_data_user]

    saldo_user = int(data_user_baris[c.csvID_user_saldo])

    found_game_id = arr.found_in_kolom(data_game, c.csvID_game_id, game_id)
    if found_game_id:
        row_game_id = arr.find_row_id(data_game, c.csvID_game_id, game_id)
        data_row_game_id = data_game[row_game_id]
        data_pemilik_game = arr.all_valid_row(data_kepemilikan, c.csvID_game_id, game_id)

        harga_game = int(data_row_game_id[c.csvID_game_price])
        stok_game = data_row_game_id[c.csvID_game_stock]
        sudah_punya = arr.found_in_kolom(data_pemilik_game, c.csvID_kepemilikan_user_id, username)

        #Kasus sudah dimiliki
        if sudah_punya:
            print(c.bg_sudahPunya)
        else: #Kasus game tidak dimiliki
        #Kasus tidak memiliki saldo
            if saldo_user < harga_game:
                print(c.bg_saldoTidakCukup)
            else: #Kasus tidak memiliki game, saldo user melebihi harga_game
                if stok_game == 0:
                    print(c.bg_stokHabis)
                else: #Kasus tidak memiliki game, saldo user melebihi harga game, dan stok lebih dari 0. (Intinya kasus berhasil)
                    #Update saldo
                    data_user[row_data_user][c.csvID_user_saldo] = str(int(data_user[row_data_user][c.csvID_user_saldo]) - harga_game)

                    #Update stok
                    data_game[row_game_id][c.csvID_game_stock] = str(int(data_game[row_game_id][c.csvID_game_stock]) - 1) #update stok game

                    #Bagian update kepemilikan
                    data_kepemilikan = arr.fungsi_append(data_kepemilikan, [game_id,user_id])
                    
                    # Bagian update_riwayat
                    nama_game = data_game[row_game_id][c.csvID_game_nama]
                    temp_riwayat = [game_id, nama_game, str(harga_game), username, "2022"]
                    data_riwayat = arr.fungsi_append(data_riwayat, temp_riwayat)
                    
                    # matrix_to_csv("Data/kepemilikan.csv",data_kepemilikan)
                    # matrix_to_csv("Data/user.csv", data_user)
                    # matrix_to_csv("Data/game.csv", data_game)
                    # matrix_to_csv("Data/riwayat.csv", data_riwayat)
                    print(f"Kamu berhasil membeli '{data_game[row_game_id][c.csvID_game_nama]}'! Saldo sekarang: {data_user[row_data_user][c.csvID_user_saldo]}.")

    else:
        print(c.bg_notFound)


# data_game = csv_to_matrix("Data/game.csv")
# data_kepemilikan = csv_to_matrix("Data/kepemilikan.csv")
# data_user = csv_to_matrix("Data/user.csv")
# data_riwayat = csv_to_matrix("Data/riwayat.csv")
# buy_game(data_game, data_kepemilikan, data_user, data_riwayat, "admin")