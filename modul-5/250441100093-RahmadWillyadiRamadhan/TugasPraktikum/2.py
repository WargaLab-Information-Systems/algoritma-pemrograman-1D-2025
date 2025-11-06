def cekanagram(kata1, kata2):
    return sorted(kata1) == sorted(kata2)

while True:
    kata1 = input("Masukkan kata pertama: ").lower()
    kata2 = input("Masukkan kata kedua: ").lower()
    
    if not (kata1.isalpha() and kata2.isalpha()):
        print("Error: Input harus huruf alfabet saja!\n")
        continue  

    hasil = cekanagram(kata1, kata2)
    print(f"Apakah '{kata1}' dan '{kata2}' merupakan anagram {hasil}")
    
    if input("Apa ada perhitungan lagi? (y/n): ") != "y":
        break