angka = int(input('Masukkan Angka : ')) 
print(angka) #input 'Hai' 
# try: 
#     angka = int(input('Masukkan Angka : '))
# except ValueError: 
#     print('input yang anda masukkan bukan Integer (angka)')
# try: 
#     angka = int(input('Masukkan Angka : ')) 
# except ValueError: 
#     print('input yang anda masukkan bukan Integer (angka)') 
# else : 
#     print(f'Angka yang kamu input : {angka}') 
try: 
 usn = input('Username yang diinginkan : ') 
 if len(usn) < 5: 
    raise ValueError('Nama Minimal Memiliki 5 karakter') 
except ValueError as e: 
    print(e) 
