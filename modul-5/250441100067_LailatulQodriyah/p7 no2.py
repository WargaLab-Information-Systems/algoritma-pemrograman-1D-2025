# def cek_anagram(kata1, kata2):
#     kata1 = kata1.replace(" ", "").lower()  
#     kata2 = kata2.replace(" ", "").lower()
#     print(kata1)

#     return sorted(kata1) == sorted(kata2)

# kata1 = input("Masukkan kata pertama: ")
# kata2 = input("Masukkan kata kedua: ")

# if cek_anagram(kata1, kata2):
#     print(f"'{kata1}' dan '{kata2}' adalah anagram!")
# else:
#     print(f"'{kata1}' dan '{kata2}' bukan anagram.")



def cek_anagram_sederhana(kata1, kata2):
    
    kata_bersih1 = ""
    for i in kata1:
        if i != " ":   
            kata_bersih1 += i.lower()
            
    kata_bersih2 = ""
    for i in kata2:
        if i != " ":
            kata_bersih2 += i.lower()
    if len(kata_bersih1) != len(kata_bersih2):
        return False
    
    hitungan = {}   

    for i in kata_bersih1:
        hitungan[i] = hitungan.get(i, 0) + 1 

    for i in kata_bersih2:
        if hitungan.get(i, 0) > 0:
            hitungan[i] -= 1
        else:
            return False 
    return True

kata1 = (input("Masukkan kata pertama: "))
kata2 = (input("Masukkan kata kedua: "))

if 

if cek_anagram_sederhana(kata1, kata2):
    print(f"'{kata1}' dan '{kata2}' adalah anagram!")
else:
    print(f"'{kata1}' dan '{kata2}' bukan anagram.")