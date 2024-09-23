import random
nomor_rahasia = random.randint(1, 100)
percobaan = 5

while percobaan > 0:
    try:
        tebakan = int(input('Masukkan tebakan Anda (0 untuk berhenti) : '))
        if tebakan == 0:
            print('Permainan dihentikan')
            break
        if tebakan > nomor_rahasia :
            print('Angka terlalu besar.')
        elif tebakan < nomor_rahasia :
            print('Angka terlalu kecil.')
        else:
            print('Selamat! Anda menebak angka dengan benar.')
            break
        percobaan = percobaan - 1
        print(f'Percobaan tersisa: {percobaan}')      
    except :
        print('Input tidak valid. Harap masukkan angka.')
    
    if percobaan == 0 and tebakan != nomor_rahasia:
        print(f'Maaf, kesempatan Anda habis. Angka yang benar adalah {nomor_rahasia}.')
