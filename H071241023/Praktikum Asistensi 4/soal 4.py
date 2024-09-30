def kalkulator():
    print('Selamat datang di Kalkulator Sederhana!')

    try:
        a = int(input('Masukkan angka pertama: '))
    except ValueError as e:
        print(f'input tidak valid {e}')
        return
    
    try:
        b = int(input('Masukkan angka kedua: '))    
    except ValueError as e:
        print(f'input tidak valid {e}')
        return
    
    operator = input('Operasi (+, -, *, /): ')

    if operator not in ['+', '-', '*', '/']:
        print('Operasi tidak valid. Gunakan +, -, *, dan /')
        return
    
    try:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError('Pembagian dengan Nol tidak diperbolehkan.') 
    except ValueError as e:
        print(e)

print('Hasil: ', ((kalkulator())))