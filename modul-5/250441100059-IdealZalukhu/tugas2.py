def cek_huruf(kata1, kata2):
    if any(char.isdigit() for char in kata1) or any(char.isdigit() for char in kata2):
        raise ValueError("Kata tidak boleh mengandung angka!")
           
    return sorted(kata1.replace(" ", "").lower()) == sorted(kata2.replace(" ", "").lower())

kata1 = input("masukkan kata pertama: ")
kata2 = input("masukkan kata kedua  : ")

if cek_huruf(kata1, kata2):
    print(f"{kata1} dan {kata2}, adalah anagram.")
else:
    print(f"{kata1} dan {kata2}, adalah bukan anagram.")

