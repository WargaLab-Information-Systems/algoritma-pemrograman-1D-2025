print("=== SIMULASI PIN ATM ===")

pin_correct = 25019
percobaan = 0

while percobaan <3:
    pin = int(input("Masukkan pin 5 digit:"))
    if pin == pin_correct:
        print("Pin benar, akses diterima")
        break
    else:
        print("Pin salah, coba lagi")
        percobaan = percobaan + 1
if percobaan == 3:
    print("Akses ditolak, kartu diblokir")