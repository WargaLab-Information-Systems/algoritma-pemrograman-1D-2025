NIM = "250441100055"
PIN = "25055"
attempts = 3
for i in range(attempts):
    user_pin = input("Masukkan PIN (5 digit): ")
    if user_pin == PIN:
        print("PIN benar, akses diterima.")
        break
    else:
        print("PIN salah, coba lagi.")
        if i == attempts - 1:
            print("Akses ditolak, kartu diblokir.")