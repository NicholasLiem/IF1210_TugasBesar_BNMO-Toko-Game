import operasi_array as arr
import constant as c
    
def ubah_game(data_game):
    id = input(c.s_idGame)
    row_id = arr.find_row_id(data_game,c.csvID_game_id,id)

    if arr.found_in_kolom(data_game, c.csvID_game_id, id):
        new_name = input(c.s_nameGame)
        new_category = input(c.s_categoryGame)
        new_year = input(c.s_releaseYear)
        new_price = input(c.s_priceGame)

        new_data = [id, new_name, new_category, new_year, new_price]
        while not (arr.cekinteger(new_year) and arr.cekinteger(new_price)):
            print(c.tg_invalid)
            new_name = input(c.s_nameGame)
            new_category = input(c.s_categoryGame)
            new_year = input(c.s_releaseYear)
            new_price = input(c.s_priceGame)
        for i in range(5):
            if new_data[i] != "":
                data_game[row_id][i] = new_data[i]
        return data_game

    else:
        print(c.s_notFound)
