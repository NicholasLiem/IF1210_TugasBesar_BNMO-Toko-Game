import math

def isKoprima(a : int, b : int) -> bool:
    return math.gcd(a, b) == 1

def enkripsi(teks : str, key : tuple[int, int]) -> str:
    a, b = key
    if not isKoprima(a, 26):
        print('a harus koprima dengan 26')
        return
    hasil = ''
    for c in teks:
        if c.islower():
            x = ord(c) - ord('a')
            hasil += chr(ord('a') + (a*x + b) % 26)
        elif c.isupper():
            x = ord(c) - ord('A')
            hasil += chr(ord('A') + (a*x + b) % 26)
        else:
            hasil += c
    return hasil

def mod_inverse(a : int, m : int) -> int:
    t = 0
    r = m
    newt = 1
    newr = a
    while newr != 0:
        q = r // newr
        t, newt = newt, t - q*newt
        r, newr = newr, r - q*newr
    if r > 1:
        print('a tidak bisa di-inverse')
        return
    if t < 0:
        t = t + m
    return t

def dekripsi(teks : str, key : tuple[int, int]) -> str:
    a, b = key
    if not isKoprima(a, 26):
        print('a harus koprima dengan 26')
        return
    hasil = ''
    for c in teks:
        if c.islower():
            x = ord(c) - ord('a')
            hasil += chr(ord('a') + (mod_inverse(a, 26)*(x-b) % 26))
        elif c.isupper():
            x = ord(c) - ord('A')
            hasil += chr(ord('A') + (mod_inverse(a, 26)*(x-b) % 26))
        else:
            hasil += c
    return hasil

exit = False
while not exit:
    print('Pilih menu:')
    print('[1] Enkripsi')
    print('[2] Dekripsi')
    print('[3] Keluar')
    x = int(input('>>> '))
    if x == 1 or x == 2:
        if x == 1:
            print('Masukkan teks yang ingin dienkripsi:')
        else:
            print('Masukkan teks yang ingin didekripsi:')
        teks = input('>>> ')
        print('Masukkan key: ')
        a = int(input('a = '))
        b = int(input('b = '))
        if x == 1:
            print('Hasil enkripsi:', enkripsi(teks, (a,b)))
            print()
        else:
            print('Hasil dekripsi:', dekripsi(teks, (a,b)))
            print()
    elif x == 3:
        print('Bye!')
        exit = True
    else:
        print('Pilihan tidak ada di menu!')

            