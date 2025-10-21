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

while percobaan < 3:
    print("==LOGIN==")
    print("==masukan nama dan password anda==")
    name = input("Username: ")
    password = input("Password: ")

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
    print(menu_awal)
    pilih_menu =input("PILIH MENU YANG ADA DARI [1-4]")
    print()

    if pilih_menu == "1":
        os.system("cls")
        os.system('clear')
        while True:
            print(daftar_hewan)
            print(f"{menu_awal["1"]}{daftar_hewan}")
            print("INGIN MENAMBAH SATWA?")
            lanjut_1=input("YA/TIDAK")
            print()
            if lanjut_1 == "ya": 
                    addkey = input("nomor hewan:")
                    addvalue = input("nama hewan:")
                    daftar_hewan.update({addkey:addvalue})
                    print(daftar_hewan)
                    print("berhasil menambahkan")
                    print("tekan enter untuk melanjutkan")
                    os.system("cls")
                    os.system('clear')
            elif lanjut_1 == "tidak":
             os.system("cls") 
             os.system('clear')
             break

            
            

    elif pilih_menu == "2":
         os.system("cls") 
         os.system('clear')    
         print({menu_awal["2"]})
         print(daftar_hewan )
         print("APA YANG INGIN ANDA HAPUS?")
         hapus = input("input no hewan yang ingin dihapus.")
         if not hapus in daftar_hewan:
            print(f"satwa pada '{hapus}' tidak ada.") 
            input("enter untuk lanjut")  
            os.system("cls") 
            os.system('clear')
         else: 
             del daftar_hewan[hapus]
             print(f"'{hapus}'berhasil dihapus")
             print(daftar_hewan)
             os.system("cls") 
             os.system('clear')
             continue
    
    elif pilih_menu == "3":
         os.system("cls") 
         os.system('clear')
         print({menu_awal["3"]})
         print(daftar_hewan)
         print("anda ingin mengubah apa?")
         ubah=input("pilih no satwa yang ingin di ubah ")
         
         if ubah in daftar_hewan:
             ubah_new= input(f"input perubahan nama'{ubah}': ")
             daftar_hewan[ubah] = ubah_new
             print(f"daftar_hewan'{ubah}'berhasil melakukan perubahan menjadi{ubah_new}")
             print(daftar_hewan)
             os.system("cls") 
             os.system('clear')
         else:
             print(f"satwa pada '{ubah}' tidak ada!")
             input("enter untuk lanjut")
             os.system("cls") 
             os.system('clear')
             
             
             
             
    elif pilih_menu == "4":
         os.system("cls") 
         os.system('clear')
         print("terima kasih telah menggunakan program!")
         break
    else: 
          os.system("cls") 
          os.system('clear')
          print("menu yang dipilih tidak ada")

          

         
        
         




         

        
        
        



            






