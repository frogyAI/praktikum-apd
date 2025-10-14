#login program sebagai admin
import os

namaID = "erfandi"
passID = "123"  # Ubah ke string untuk menghindari error jika input non-angka
percobaan = 0
login_berhasil = False  # Ubah ke False awal
daftar_satwa = []

while percobaan < 3:
    print("==LOGIN==")
    print("==masukan nama dan password anda==")
    name = input("Username: ")
    password = input("Password: ")

    if name == namaID and password == passID:  # Perbaiki kondisi login
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
    print("1. Tambah Daftar Hewan")
    print("2. Hapus Daftar Hewan")
    print("3. Update Info Hewan")
    print("4. Tampilkan List Hewan")
    print("5. Keluar Program")

    pilih = input("pilih daftar yang tersedia(1-5): ")
    print()

    #penambahan
    if pilih == "1":
        os.system("cls")
        while True:
            list_hewan = []  # Pindahkan deklarasi ke sini
            menambah = input("input Nama Hewan : ")
            list_hewan.append(menambah)
            
            menambah = input("input jenis pakan hewan: ")
            list_hewan.append(menambah)

            menambah = input("input umur hewan: ")
            list_hewan.append(menambah)

            menambah = input("input status kesehatan Hewan : ")
            list_hewan.append(menambah)

            daftar_satwa.append(list_hewan.copy())
            list_hewan.clear()
            print("berhasil menambahkan")
            print("tekan enter untuk melanjutkan")
            os.system("cls")
            break
            

    #jika ingin ada perubahan/hapus
    elif pilih == "2":
        if daftar_satwa:
            while True:
                os.system("cls")
                print("=== DAFTAR HEWAN ===")
                for i, j in enumerate(daftar_satwa, start=1):
                    print(f"{i}. {j}")
                hapus = input("Masukan Pilihan 1,2 dst.. : ")
                if hapus.isdigit() and 1 <= int(hapus) <= len(daftar_satwa):
                    simpan = int(hapus)
                    daftar_satwa.pop(simpan - 1)
                    print("Penghapusan berhasil")
                else:
                    print("Pilihan tidak valid")
                    os.system("cls")
                    break
        else:
            os.system("cls")
            print("Tidak Ada Hewan \n")

    #update informasi hewan       
    elif pilih == "3":
        if daftar_satwa:
            while True:
                os.system("cls")
                print("=== DAFTAR HEWAN ===")
                for i, j in enumerate(daftar_satwa, start=1):
                    print(f"{i}. {j}")
                
                pilihan = input("Masukan Pilihan (1,2,dst) : ")
                if pilihan.isdigit() and 1 <= int(pilihan) <= len(daftar_satwa):
                    update = int(pilihan)
                    print(f"Data saat ini: {daftar_satwa[update - 1]}")
                    
                    while True:
                        print("\nPilihan Update :")
                        print("1. Nama Hewan")
                        print("2. Jenis pakan Hewan")
                        print("3. Umur Hewan")
                        print("4. Kondisi Hewan")
                        print("5. Selesai Update")
                        
                        sub_pilihan = input("Pilih Nomor (1-5): ")

                        if sub_pilihan == "1":
                            daftar_satwa[update - 1][0] = input("Masukan Nama Baru: ")
                            print("Nama berhasil diupdate!")
                        elif sub_pilihan == "2":
                            daftar_satwa[update - 1][1] = input("Masukan jenis pakan baru: ")
                            print("Jenis pakan berhasil diupdate!")
                        elif sub_pilihan == "3":
                            daftar_satwa[update - 1][2] = input("Masukan umur hewan baru: ")
                            print("Umur berhasil diupdate!")
                        elif sub_pilihan == "4":
                            daftar_satwa[update - 1][3] = input("Update kondisi hewan: ")
                            print("Kondisi berhasil diupdate!")
                        elif sub_pilihan == "5":
                            print("Update selesai!")
                            break
                        else:  
                            print("Pilihan Tidak Ada \n")
                    
                    lanjut_update = input("Update hewan lain? (yes/no): ")
                    if lanjut_update.lower() != "yes":
                        os.system("cls")
                        break
                else:
                    print("Pilihan tidak valid!")
                    lanjut_update = input("Coba lagi? (yes/no): ")
                    if lanjut_update.lower() != "yes":
                        os.system("cls")
                        break
        else:               
            os.system("cls")
            print("Tidak Ada Hewan\n")

    #menampilkan list hewan
    elif pilih == "4":
        if len(daftar_satwa) == 0:
            os.system("cls")
            print("Tidak Ada Hewan \n")
        else:
            os.system("cls")
            print("=== DAFTAR HEWAN ===")
            for i, hewan in enumerate(daftar_satwa, 1):
                print(f"{i}. Nama: {hewan[0]}, Pakan: {hewan[1]}, Umur: {hewan[2]}, Kesehatan: {hewan[3]}")
            print()
            input("Tekan Enter untuk kembali ke menu...")
            os.system("cls")

    #keluar
    elif pilih == "5":
        os.system("cls")
        print("Terima kasih telah menggunakan program!")
        break
    
    # Pilihan tidak valid
    else:
        os.system("cls")
        print("Pilihan tidak valid! Silakan pilih 1-5.\n")