import operasi_array as arr
import parseran
import constant as c

<<<<<<< HEAD
def register(data_user):
    name = input(c.register_nama)
=======
dir = "Data/user.csv"


def register():
    data_user = parseran.csv_to_matrix(dir)
    name = input("Masukkan nama : ")
>>>>>>> 6f652465c31da9378f0571c54723c8728895a449
    while True:
        user_baru=input(c.register_username)
        found = False
<<<<<<< HEAD
        for item in data_user:
            if user_baru == item[c.csvID_user_username] :
=======
        for i in range (arr.panjang_baris(data_user)):
            if user_baru == data_user[i][c.csvID_user_nama] :
>>>>>>> 6f652465c31da9378f0571c54723c8728895a449
                found= True
                break
        if not found:
            break
        else:
            print(f"Username {user_baru} sudah terpakai, silakan menggunakan username lain.")

    password = input(c.register_password)
    role = "user"
    balance= "0"
    id = str(arr.panjang_baris(data_user))
    data_temp = [id,user_baru,name,password,role,balance]

    print(f"Username {user_baru} telah berhasil register ke dalam Binomo")
    
    data_baru = arr.fungsi_append(data_user, data_temp)
    #parseran.matrix_to_csv(directory, data_baru)