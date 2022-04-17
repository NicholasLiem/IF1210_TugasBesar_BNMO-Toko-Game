import parseran
import operasi_array as arr
import constant as c

def cekinteger(variabel):
    for c in variabel:
        if not(48 <= ord(c) <= 57):
            return False
    return True 

def masukkan():
    new_name = input(c.s_nameGame)
    new_category = input(c.s_categoryGame)
    new_year = input(c.s_releaseYear)
    new_price = input(c.s_priceGame)
    
    return new_name, new_category, new_year, new_price
    
def ubah_game(data_game):
    id = input(c.s_idGame)
    row_id = arr.find_row_id(data_game,c.csvID_game_id,id)

    if arr.found_in_kolom(data_game, c.csvID_game_id, id):
        inputs = masukkan()
        new_data = [id, inputs[0], inputs[1], inputs[2], inputs[3]]
        while not (cekinteger(inputs[2]) and cekinteger(inputs[3])):
            print(c.tg_invalid)
            inputs = masukkan()
        for i in range(5):
            if new_data[i] != "":
                data_game[row_id][i] = new_data[i]
        #parseran.matrix_to_csv(path, data_game)
        return data_game

    else:
        print(c.s_notFound)

#ubah_game()
