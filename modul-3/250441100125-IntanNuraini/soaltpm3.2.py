PIN_BENAR = "25125"  
kesalahan = 0  
print("Masukkan PIN (5 digit angka):")

while kesalahan < 3:  
    pin = input("PIN: ")  
    
    if len(pin) != 5 or not pin.isdigit():
        print("Salah format! Harus 5 angka. Coba lagi.")
        continue  
    
    if pin == PIN_BENAR:
        print("PIN benar! Akses diterima.")
        break  
    else:
        kesalahan = kesalahan + 1  
        print("PIN salah! Sisa {3 - kesalahan} kesempatan.")

if kesalahan == 3:
    print("Akses ditolak! Kartu diblokir.")