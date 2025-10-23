# Simulasi mesin ATM

PIN_BENAR = 25075
kesempatan = 3

while kesempatan > 0:
    pin = input("Masukkan PIN (5 digit): ")

    # Validasi: harus angka
    if not pin.isdigit():
        print("PIN berisi huruf, coba lagi.")
        continue

    # Validasi: harus 5 digit
    if len(pin) != 5:
        print("PIN harus 5 digit!")
        continue

    # Cek PIN
    if int(pin) == PIN_BENAR:
        print("PIN benar, akses diterima.")
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print("PIN salah, coba lagi. Sisa percobaan:", kesempatan)
        else:
            print("Akses ditolak, kartu diblokir.")