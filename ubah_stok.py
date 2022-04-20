import operasi_array as arr
import constant as c

#Nicholas
def ubah_stok(data_game):
    game_id = input(c.u_idGame)
    row_id = arr.find_row_id(data_game,c.csvID_game_id,game_id)
    if not arr.found_in_kolom(data_game,c.csvID_game_id,game_id):
        print(c.u_notFound)
    else:
        stock_input = int(input(c.u_jumlah))
        stock_data = int(data_game[row_id][c.csvID_game_stock])
        nama_game = data_game[row_id][c.csvID_game_nama]
        if (stock_input + stock_data) < 0:
            print(f"Stok game {nama_game} gagal dikurangi karena stok kurang. Stok sekarang: {stock_data}")
        elif stock_input >= 0:
            new_stock_data = stock_data + stock_input
            data_game[row_id][c.csvID_game_stock] = str(new_stock_data)
            print(f"Stok game {nama_game} berhasil ditambahkan. Stok sekarang: {new_stock_data}")
        else: #(0 < -1*stock_input < stock_data):
            new_stock_data = stock_data + stock_input
            data_game[row_id][c.csvID_game_stock] = str(new_stock_data)
            print(f"Stok game {nama_game} berhasil dikurangi. Stok sekarang: {new_stock_data}")
        return data_game