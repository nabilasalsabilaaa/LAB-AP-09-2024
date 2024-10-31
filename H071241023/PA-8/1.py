import re

string = input('Masukkan string: ') #'2222222222aaaaaaaaaaa2222222222aaaaaaaaaa13 57' 'x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779 '
pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
result = re.match(pattern, string)

if result :
    print('True')
else :
    print('False')