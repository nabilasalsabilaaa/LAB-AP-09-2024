def palindrome():
    kata = input('Masukkan string: ')
    palindrom = ''.join(reversed(kata.lower()))
    if kata.lower() == palindrom:
        print('Palindrome')
    else:
        print('Bukan Palindrome')

palindrome()