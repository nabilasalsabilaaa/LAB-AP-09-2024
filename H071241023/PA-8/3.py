import re 

def is_valid_username(username): 
    pattern = r"^[A-Za-z0-9]{5,20}$" # TODO: Tambahkan pola untuk memvalidasi panjang karakter minimal 5 dan maksimal 20. 
    return re.search(pattern, username) 

def is_valid_email(email): 
    pattern = r"^[a-z]+[a-z0-9]*([0-9]{2,})?@[a-zA-Z]+\.(com|co\.id)$" # TODO: Buatkan pola RegEx untuk validasi email. Sudah ada clue berupa pola untuk mencocokkan domain email. 
    return re.search(pattern, email) 

def is_valid_password(password): 
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[a-zA-Z0-9]{8,}$" # TODO: Buatkan pola RegEx untuk validasi password sesuai permintaan soal. Sudah ada clue berupa pola RegEx yang bisa kamu gunakan untuk menyelesaikan jawaban. 
    return re.search(pattern, password) 

username = input("Masukkan username: ") 

if is_valid_username(username): 
    email = input("Masukkan email: ") 

    if is_valid_email(email): 
        password = input("Masukkan password: ") 

        if is_valid_password(password): 
            print(f"\nRegistrasi berhasil! Halo {username}") # TODO: Tambahkan sapaan "Halo (username)"  
        else: 
            print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.") 

    else: 
        print("\nEmail yang kamu input tidak valid. Registrasi gagal!") 

else: 
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")