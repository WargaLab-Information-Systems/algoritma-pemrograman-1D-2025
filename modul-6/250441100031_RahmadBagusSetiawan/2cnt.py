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

print("=== PROGRAM GABUNG DAN URUTKAN TUPLE ===")
print()

print("CONTOH 1:")
t1 = (3, 1, 4)
t2 = (1, 5, 9)
hasil1 = gabung_dan_urutkan(t1, t2)
print(f"  Input: t1 = {t1}, t2 = {t2}")
print(f"  Output: {hasil1}")
print()
