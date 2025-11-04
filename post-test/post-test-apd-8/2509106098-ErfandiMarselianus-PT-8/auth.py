def login():
    """
    Modul untuk handle proses login
    """
    namaID = "erfandi"
    passID = "123"  
    percobaan = 0
    login_berhasil = False
    
    while percobaan < 3:
        print("=" * 50)
        print("SISTEM MANAJEMEN SATWA KEBUN BINATANG")
        print("=" * 50)
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
            return True
        else:
            percobaan += 1
            print("Login Gagal! Percobaan ke-", percobaan)
            if percobaan < 3:
                print("Coba lagi.\n")
            continue

    if not login_berhasil:
        print("anda sudah 3 kali gagal login, program dihentikan.")
        return False