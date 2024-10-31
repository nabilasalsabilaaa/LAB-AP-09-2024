import re

def main():
    try:
        N = int(input('Masukkan jumlah baris: '))
            
        results = []
        for _ in range(N):
            ip = input()
            if len(ip) > 500:
                results.append('Bukan IP Adress')
            else:
                results.append(CekIPAdress(ip))
        for result in results:
            print(result)
            
    except ValueError:
        print('Input tidak valid. Harus berupa angka untuk jumlah baris')

def CekIPAdress(ip):
    IPv4_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    IPv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    
    if re.match(IPv4_pattern, ip):
        segments = ip.split('.')
        for segment in segments:
            if all(0 <= int(segment) <= 255 for  segment in segments):
                return 'IPv4'
    elif re.match(IPv6_pattern, ip):
        return 'IPv6'

    return 'Bukan IP Address'

main()

# IPv6_pattern = r'^((([0-9a-fA-F]{1,4}:){1,7}[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){1,7}:)|(::([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){1,6}::([0-9a-fA-F]{1,4}:){0,5}[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){1,5}::([0-9a-fA-F]{1,4}:){0,4}[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){1,4}::([0-9a-fA-F]{1,4}:){0,3}[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){1,3}::([0-9a-fA-F]{1,4}:){0,2}[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){1,2}::[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){1,1}::([0-9a-fA-F]{1,4}:){0,1}[0-9a-fA-F]{1,4}))$'
# IPv4_pattern = r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$'
