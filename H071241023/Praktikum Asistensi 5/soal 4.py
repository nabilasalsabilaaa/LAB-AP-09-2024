def MenampilkanSubstring(string):
    print('====================')
    panjang = len(string)
    
    for panjang_substring in range(1, panjang + 1):
        for start in range(panjang - panjang_substring + 1):
            end = start + panjang_substring
            print(string[start:end])

kata = input('Masukkan string: ')
MenampilkanSubstring(kata)

