def gabung_dan_urutkan(tuple1, tuple2):
    tuple_gabungan = tuple1 + tuple2
    
    tanpa_duplikat = []
    for angka in tuple_gabungan:
        if angka not in tanpa_duplikat:
            tanpa_duplikat.append(angka)
    
    n = len(tanpa_duplikat)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tanpa_duplikat[j] < tanpa_duplikat[j + 1]:
                temp = tanpa_duplikat[j]
                tanpa_duplikat[j] = tanpa_duplikat[j + 1]
                tanpa_duplikat[j + 1] = temp
    
    hasil_akhir = tuple(tanpa_duplikat)
    
    return hasil_akhir

def dapatkan_tuple_dari_input(pesan_prompt):
    while True:
        input_str = input(pesan_prompt)
        
        if not input_str.strip():
            return ()
            
        try:
            list_angka_str = input_str.split(',')
            list_angka_int = [int(angka.strip()) for angka in list_angka_str]
            return tuple(list_angka_int)
            
        except ValueError:
            print("Input tidak valid! Harap masukkan angka yang dipisahkan koma (contoh: 3, 1, 4).")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

print("=== PROGRAM GABUNG DAN URUTKAN TUPLE ===")
print("Instruksi: Masukkan angka-angka yang dipisahkan dengan koma.")
print("Contoh input: 5, 1, 10, 2")
print()

t1 = dapatkan_tuple_dari_input("Masukkan angka-angka untuk tuple pertama: ")
t2 = dapatkan_tuple_dari_input("Masukkan angka-angka untuk tuple kedua: ")

hasil = gabung_dan_urutkan(t1, t2)

print()
print("--- Hasil ---")
print(f"  Input: t1 = {t1}, t2 = {t2}")
print(f"  Output Gabungan (Urut Terbesar): {hasil}")