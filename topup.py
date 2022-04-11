import parseran
import operasi_array as arr
import constant as c

dir = "Data/user.csv"
data_user = parseran.csv_to_matrix(dir)

def topup():
    username = input(c.t_username)
    saldo_topup = int(input(c.t_saldo))
    row_id = arr.find_row_id(data_user,c.csvID_user_username,username)
    nama = data_user[row_id][c.csvID_user_nama]
    saldo_data = int(data_user[row_id][c.csvID_user_saldo])
    new_saldo = saldo_topup + saldo_data
    if not arr.found_in_kolom(data_user,c.csvID_user_username,username):
        print(f"Username ""{username}"" tidak ditemukan.")
    elif new_saldo < 0:
        print(c.t_invalid)
    else: #username ada dan saldo hasil positif
        data_user[row_id][c.csvID_user_saldo] = str(new_saldo)
        print(f"Top up berhasil. Saldo {nama} bertambah menjadi {new_saldo}.")
    #parseran.matrix_to_csv(dir, data_user)
