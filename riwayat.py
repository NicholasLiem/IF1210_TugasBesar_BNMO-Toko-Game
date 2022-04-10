import parseran
import operasi_array as arr
import constant as c

dir = "Data/riwayat.csv"
data_riwayat = parseran.csv_to_matrix(dir)

def riwayat():
    user = input("Login session user: ")
    #usernya harusnya diambil dari login sessionnya. tapi strukturnya harusnya udah jadi.
    #Login session, user.
    if not(arr.found_in_kolom(data_riwayat, c.csvID_riwayat_user_id,user)):
        print(c.r_notFound)
    else:
        list_riwayat = arr.all_valid_row(data_riwayat, c.csvID_riwayat_user_id, user)
        riwayat_tanpa_id = arr.delete_column(list_riwayat, c.csvID_riwayat_user_id)
        print(c.r_listing)
        for item in riwayat_tanpa_id:
            print(item)