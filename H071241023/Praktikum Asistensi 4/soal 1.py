import random

def kartu():
    kartu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(kartu)

def jumlah_kartu(nilai):
    return sum(nilai)

def mulai():
    print('Welcome to Blackjack!')
    pemain = [kartu()] 
    dealer = [kartu()]
    print(f'Kartu anda sekarang adalah: {pemain[0]}')
    
    while True:
        keputusan = input('Apakah masih akan mengambil kartu? (y/n) \n').lower()
        total1 = jumlah_kartu(pemain)
        
        if keputusan == 'y':
            pemain.append(kartu())
            total1 = jumlah_kartu(pemain)
            if total1 > 21:
                print('Anda kalah!')
                break
            print(f'Kartu anda sekarang adalah: {total1}')
        elif keputusan == 'n':
            break
        else:
            print('Inputan tidak valid')
            continue
            
    total2 = 0
    if total1 <= 21:
        print(f'Kartu dealer adalah: {dealer[0]}')
        while total2 <= 17:
            dealer.append(kartu())
            total2 = jumlah_kartu(dealer)
            print('Kartu dealer dibawah 17, dealer akan mengambil 1 kartu')
            print(f'Kartu dealer sekarang adalah: {total2}')
    
    if total1 <= 21:
        if total1 > total2 or total2 > 21:
            print('Anda menang!')
        elif total1 < total2:
            print('Dealer menang!')
        else:
            print('Seri!')

mulai()
