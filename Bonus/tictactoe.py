M = [['   ' for x in range(3)] for y in range(3)]

def cetak_papan():
    print('+---+---+---+')
    for baris in range(3):
        print('|', end='')
        for kolom in range(3):
            print(M[baris][kolom] + '|', end='')
        print()
        print('+---+---+---+')

selesai = False
i = 0
pemenang = 0
while not selesai:
    cetak_papan()
    print()
    if i % 2 == 0:
        print('Giliran pemain 1 (X)')
    else:
        print('Giliran pemain 2 (O)')
    print()
    print('Masukkan posisi')
    kosong = False
    while not kosong:
        baris = int(input('Baris (1-3) = '))
        while not (1 <= baris <= 3):
            print('Masukan di luar range, coba lagi!')
            baris = int(input('Baris (1-3) = '))
        kolom = int(input('Kolom (1-3) = '))
        while not (1 <= kolom <= 3):
            print('Masukan di luar range, coba lagi!')
            kolom = int(input('Kolom (1-3) = '))
        if M[baris-1][kolom-1] == '   ':
            kosong = True
        else:
            print('Baris',baris,'kolom',kolom,' sudah terisi')
    print()
    if i % 2 == 0:
        M[baris-1][kolom-1] = ' X '
    else:
        M[baris-1][kolom-1] = ' O '
    # Cek pemenang
    # Horizontal
    for baris in range(3):
        if ' X ' == M[baris][0] and M[baris][0] == M[baris][1] and M[baris][1] == M[baris][2]:
            pemenang = 1
            selesai = True
        elif ' O ' == M[baris][0] and M[baris][0] == M[baris][1] and M[baris][1] == M[baris][2]:
            pemenang = 2
            selesai = True
    # Vertikal
    for kolom in range(3):
        if ' X ' == M[0][kolom] and M[0][kolom] == M[1][kolom] and M[1][kolom] == M[2][kolom]:
            pemenang = 1
            selesai = True
        elif ' O ' == M[0][kolom] and M[0][kolom] == M[1][kolom] and M[1][kolom] == M[2][kolom]:
            pemenang = 2
            selesai = True
    # Diagonal
    if ' X ' == M[0][0] and M[0][0] == M[1][1] and M[1][1] == M[2][2]:
        pemenang = 1
        selesai = True
    elif ' O ' == M[0][0] and M[0][0] == M[1][1] and M[1][1] == M[2][2]:
        pemenang = 2
        selesai = True
    if ' X ' == M[0][2] and M[0][2] == M[1][1] and M[1][1] == M[2][0]:
        pemenang = 1
        selesai = True
    elif ' O ' == M[0][2] and M[0][2] == M[1][1] and M[1][1] == M[2][0]:
        pemenang = 2
        selesai = True
    for baris in range(3):
        terisi = True
        for kolom in range(3):
            terisi = terisi and (M[baris][kolom] != '   ')
    if terisi and pemenang == 0:
        selesai = True
    i += 1

cetak_papan()
print()
if pemenang == 0:
    print('Seri. Tidak ada yang menang.')
elif pemenang == 1:
    print('Pemain 1 (X) memenangkan game.')
else:
    print('Pemain 2 (O) memenangkan game.')

        