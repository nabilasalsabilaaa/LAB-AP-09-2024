def anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_count = {}
    str2_count = {}
    
    for char in str1:
        if char.isalpha():
            str1_count[char] = str1_count.get(char, 0) + 1
    
    for char in str2:
        if char.isalpha():
            str2_count[char] = str2_count.get(char, 0) + 1
    
    remove = 0
    for char in str1_count:
        remove = remove + abs(str1_count[char] - str2_count.get(char, 0))
    for char in str2_count:
        if char not in str1_count:
            remove = remove + str2_count[char]
    
    return remove

str1 = input('Masukkan string pertama: ')
str2 = input('Masukkan string kedua: ')

print('Jumlah minimum penghapusan untuk membuat anagram:', anagram(str1, str2))