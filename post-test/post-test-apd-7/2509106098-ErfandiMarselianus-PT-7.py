import os

namaID = "erfandi"
passID = "123"  
percobaan = 0
login_berhasil = False  
daftar_hewan = {"hewan_1" : "SINGA",
         "hewan_2" : "HARIMAU",
         "hewan_3" : "BUAYA",
         "hewan_4" : "MUSANG",
}

def tampilkan_header():
    print("=" * 50)
    print("SISTEM MANAJEMEN SATWA KEBUN BINATANG")
    print("=" * 50)

def tampilkan_semua_hewan():
    if not daftar_hewan:
        print(" Daftar hewan kosong")
    else:
        print("\n DAFTAR HEWAN:")
        for key, value in daftar_hewan.items():
            print(f"  {key}: {value}")



def input_teks(pesan):
    while True:
        try:
            teks = input(pesan).strip()
            if not teks:
                raise ValueError("Input tidak boleh kosong!")
            return teks  
        except ValueError as e:
            print(f" Error: {e}")
        except KeyboardInterrupt:
            print("\n Program dihentikan oleh pengguna")
            exit()

def validasi_nama_hewan(nama):
    try:
        if not nama.replace(" ", "").isalpha():
            raise ValueError("Nama hewan hanya boleh mengandung huruf!")
        return True 
    except ValueError as e:
        print(f"  Error: {e}")
        return False  


while percobaan < 3:
   
    tampilkan_header()
    print("==LOGIN==")
    print("==masukan nama dan password anda==")
    
    try:
        name = input("Username: ")
        password = input("Password: ")
    except KeyboardInterrupt:
        print("\n Program dihentikan oleh pengguna")
        exit()

    if name == namaID and password == passID:  
        print("anda berhasil login !!!,selamat datang ", namaID)
        login_berhasil = True
        break
    else:
        percobaan += 1
        print("Login Gagal! Percobaan ke-", percobaan)
        if percobaan < 3:
            print("Coba lagi.\n")
        continue

if not login_berhasil:
    print("anda sudah 3 kali gagal login, program dihentikan.")
    exit()

print("DAFTAR MENU  SATWA KEBUN BINATANG") 
while True:
    menu_awal = {
     "1" : "DAFTAR HEWAN",
     "2" : "MENGHAPUS DAFTAR HEWAN", 
     "3" : "UPDATE INFO HEWAN",
     "4" : "KELUAR PROGRAM"
      }
    

    print("\n")
    for key, value in menu_awal.items():
        print(f"[{key}] {value}")
    
    try:
        pilih_menu = input("PILIH MENU YANG ADA DARI [1-4]: ")
    except KeyboardInterrupt:
        print("\n Program dihentikan oleh pengguna")
        exit()
        
    print()

    if pilih_menu == "1":
        os.system("cls" if os.name == 'nt' else "clear")
    
        tampilkan_header()
        tampilkan_semua_hewan()  
        
        while True:
            print("INGIN MENAMBAH SATWA?")
            try:
                lanjut_1 = input("YA/TIDAK: ").lower()
            except KeyboardInterrupt:
                print("\n Program dihentikan oleh pengguna")
                exit()
                
            print()
            if lanjut_1 == "ya": 
                try:
                    addkey = input("nomor hewan: ")
                    addvalue = input("nama hewan: ")
                    
                    if validasi_nama_hewan(addvalue): 
                        daftar_hewan.update({addkey:addvalue.upper()})
                        print("berhasil menambahkan")
                       
                        tampilkan_semua_hewan()
                        print("tekan enter untuk melanjutkan")
                        input()
                        os.system("cls" if os.name == 'nt' else "clear")
                except Exception as e:
                    print(f" Error: {e}")
                    input("Tekan enter untuk melanjutkan...")
                    
            elif lanjut_1 == "tidak":
                os.system("cls" if os.name == 'nt' else "clear")
                break
            else:
                print("Pilihan tidak valid! Silakan pilih YA atau TIDAK")
                input("Tekan enter untuk melanjutkan...")

    elif pilih_menu == "2":
        os.system("cls" if os.name == 'nt' else "clear")
        tampilkan_header()  
        print("MENGHAPUS DAFTAR HEWAN")
        tampilkan_semua_hewan()  
        print("APA YANG INGIN ANDA HAPUS?")
        
        try:
            hapus = input("input no hewan yang ingin dihapus: ")
        except KeyboardInterrupt:
            print("\n Program dihentikan oleh pengguna")
            exit()
            
        try:
            if hapus not in daftar_hewan:
                raise KeyError(f"Kode hewan '{hapus}' tidak ditemukan!")
            
            del daftar_hewan[hapus]
            print(f"'{hapus}' berhasil dihapus")
            tampilkan_semua_hewan()  
                
        except KeyError as e:
            print(f" Error: {e}")
        
        input("enter untuk lanjut")  
        os.system("cls" if os.name == 'nt' else "clear")
    
    elif pilih_menu == "3":
        os.system("cls" if os.name == 'nt' else "clear")
        tampilkan_header()  
        print("UPDATE INFO HEWAN")
        tampilkan_semua_hewan()  
        print("anda ingin mengubah apa?")
        
        try:
            ubah = input("pilih no satwa yang ingin di ubah: ")
        except KeyboardInterrupt:
            print("\n Program dihentikan oleh pengguna")
            exit()
         
        try:
            if ubah not in daftar_hewan:
                raise KeyError(f"Kode hewan '{ubah}' tidak ditemukan!")
            
            ubah_new = input(f"input perubahan nama '{ubah}': ")
            
            if validasi_nama_hewan(ubah_new):
                daftar_hewan[ubah] = ubah_new.upper()
                print(f"daftar_hewan '{ubah}' berhasil melakukan perubahan menjadi {ubah_new.upper()}")
                tampilkan_semua_hewan() 
                    
        except KeyError as e:
            print(f" Error: {e}")
        
        input("enter untuk lanjut")
        os.system("cls" if os.name == 'nt' else "clear")
             
    elif pilih_menu == "4":
        os.system("cls" if os.name == 'nt' else "clear")
        tampilkan_header()  
        print("terima kasih telah menggunakan program!")
        break
        
    else: 
        os.system("cls" if os.name == 'nt' else "clear")
        print("menu yang dipilih tidak ada")
        input("Tekan enter untuk melanjutkan...")