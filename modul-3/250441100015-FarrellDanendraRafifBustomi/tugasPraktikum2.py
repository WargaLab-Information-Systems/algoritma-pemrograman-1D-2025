pin_benar = 25015
kesempatan = 3

for i in range(kesempatan):
    try:
        pin = int(input("Masukkan PIN (5 digit): "))
        if len(str(pin)) != 5:
            print("PIN harus 5 digit!")
            continue
    except ValueError:
        print("PIN harus berupa angka!")
        continue

    if pin == pin_benar:
        print("PIN benar, akses diterima.")
        break
    else:
        print("PIN salah, coba lagi.")
else:
    print("Akses ditolak, kartu diblokir.")
