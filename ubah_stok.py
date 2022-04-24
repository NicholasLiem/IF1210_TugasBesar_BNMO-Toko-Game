#Penulis Modul: Nicholas Liem - 16521108
#Judul Modul: Ubah Stok Game
#Tanggal: 9 April 2022

import operasi_array as arr
import constant as c

def ubah_stok(data_game):
    game_id = input(c.u_idGame)
    

    if not arr.found_in_kolom(data_game,c.csvID_game_id,game_id):
        print(c.u_notFound)
        
    else:
        row_id = arr.find_row_id(data_game,c.csvID_game_id,game_id)
        stock_input = input(c.u_jumlah)
        if stock_input != "" and (arr.cekinteger(stock_input)):
            stock_input = int(stock_input)
            stock_data = int(data_game[row_id][c.csvID_game_stock])
            nama_game = data_game[row_id][c.csvID_game_nama]

            #Kalau hasil penjumlahan dari stok input dan stok data yang asli hasilnya negatif, maka tidak diproses
            if (stock_input + stock_data) < 0:
                print(f"Stok game {nama_game} gagal dikurangi karena stok kurang. Stok sekarang: {stock_data}")

            #Kalau stok inputnya positif, pastinya akan diproses dan ditambahkan
            elif stock_input >= 0:
                # Menghindari bug
                new_stock_data = stock_data + stock_input
                temp = arr.copy(data_game[row_id])
                temp[c.csvID_user_saldo] = str(new_stock_data)
                data_game[row_id] = temp
                print(f"Stok game {nama_game} berhasil ditambahkan. Stok sekarang: {new_stock_data}")
            
            #Kasus ketika stok input negatif tetapi jika dijumlahkan dengan stok data hasilnya tetap positif
            else: #(0 < -1*stock_input < stock_data):
                # Menghindari bug
                new_stock_data = stock_data + stock_input
                temp = arr.copy(data_game[row_id])
                temp[c.csvID_user_saldo] = str(new_stock_data)
                data_game[row_id] = temp
                print(f"Stok game {nama_game} berhasil dikurangi. Stok sekarang: {new_stock_data}")
        else:
            print("Stok input tidak boleh kosong atau bukan angka.")
    return data_game