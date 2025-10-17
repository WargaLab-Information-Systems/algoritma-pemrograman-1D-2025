# Program Simulasi ATM - Percobaan PIN
# PIN yang benar: 25153

pin_benar = "25153"
kesempatan = 3  # jumlah kesempatan

for i in range(kesempatan):
    pin = input("Masukkan PIN Anda (5 digit): ")

    if pin == pin_benar:
        print("PIN benar, akses diterima.")
        break
    else:
        print("PIN salah, coba lagi.")

    # Jika sudah mencoba 3 kali dan tetap salah
    if i == kesempatan - 1:
        print("Akses ditolak, kartu diblokir.")