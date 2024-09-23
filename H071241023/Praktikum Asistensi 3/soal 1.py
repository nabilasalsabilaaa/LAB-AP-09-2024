# n = int(input('Masukkan Jumlah Baris: '))
# if n % 2 == 0 :
#     for i in range(n // 2) :
#         print(' ' * (n // 2 - i - 1) + '*' * (2 * i + 1))
#     for i in range(n // 2 - 1, -1, -1):
#         print(' ' * (n // 2 - i - 1) + '*' * (2 * i + 1))
# else :
#     for i in range(n // 2 + 1):
#         print(' ' * (n // 2 - i) + '*' * (2 * i + 1))
#     for i in range(n // 2 - 1, -1, -1):
#         print(' ' * (n // 2 - i) + '*' * (2 * i + 1))

n = int(input('Masukkan Jumlah Baris :'))

for i in range(n // 2) if n % 2 == 0 else range(n // 2 + 1) :
    print('  ' * (n // 2 - i - (n % 2 == 0)) + ' *' * (2 * i + 1))
for i in range(n // 2 - 1, -1, -1):
    print('  ' * (n // 2 - i - (n % 2 == 0)) + ' *' * (2 * i + 1))