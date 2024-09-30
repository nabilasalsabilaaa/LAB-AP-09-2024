def gamenya_Budi():
    try:
        n = float(input('Masukkan angka: '))
        if n <= 0:
            return 'Input tidak Valid'
        steps = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 3 + 1
            print(f'{n}')
            steps = steps + 1
        return f'Jumlah langkah: {steps}'
    except ValueError:
        return 'Input tidak Valid'

print(gamenya_Budi())