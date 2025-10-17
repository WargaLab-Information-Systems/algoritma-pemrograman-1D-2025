PIN = 25031

print("=== Selamat datang di ATM ===")

for i in range(3):
    pin = input("Masukkan PIN 5 digit: ")

    # Cek apakah PIN benar
    if int(pin) == PIN:
        print("PIN benar, akses diterima.")
        break
    else:
        print("PIN salah, coba lagi.")

else:
    print("Akses ditolak, kartu diblokir.")
