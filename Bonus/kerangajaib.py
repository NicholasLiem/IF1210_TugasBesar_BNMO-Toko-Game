import time

JAWABAN = ['Ya', 'Tidak', 'Bisa Jadi', 'Mungkin', 'Tentunya', 'Tidak mungkin']

def random(t0, t1):
    m = 2**31 - 1
    a = 48271
    c = 0
    d = int(time.time_ns())
    time.sleep(0.001)
    d = (a*d + c) % m
    return (d % (t1 - t0)) + t0

def kerangajaib():
    input('Apa pertanyaanmu? ')
    print()
    print(JAWABAN[random(0, 6)])

kerangajaib()