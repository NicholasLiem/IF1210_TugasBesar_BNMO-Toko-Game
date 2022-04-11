import operasi_array as arr
import parseran

dir = "Data/user.csv"
def register():
    data_user = parseran.csv_to_matrix(dir)
    name = input("Masukkan nama : ")
    while True:
        user_baru=input("Masukkan username: ")
        found = False
        for i in range (arr.panjang_baris(data_user)):
            if user_baru == data_user[i][1] :
                found= True
                break
        if not found:
            break
        else:
            print("Username" , user_baru , "sudah terpakai, silakan menggunakan username lain.")

    password = input("Masukkan password: ")
    role = "user"
    balance= "0"
    id = str(arr.panjang_baris(data_user))
    data_temp = [id,user_baru,name,password,role,balance]

    print("Username" , user_baru, "telah berhasil register ke dalam Binomo")
    
    data_baru = arr.fungsi_append(data_user, data_temp)
    parseran.matrix_to_csv(dir, data_baru)


register()