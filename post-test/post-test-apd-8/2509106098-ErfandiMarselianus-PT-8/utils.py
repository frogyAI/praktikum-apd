import os

def tampilkan_header():
    """
    Menampilkan header program
    """
    print("=" * 50)
    print("SISTEM MANAJEMEN SATWA KEBUN BINATANG")
    print("=" * 50)

def clear_screen():
    
    os.system("cls" if os.name == 'nt' else "clear")

def input_teks(pesan):
    """
    Validasi input teks tidak boleh kosong
    """
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
    """
    Validasi nama hewan hanya mengandung huruf
    """
    try:
        if not nama.replace(" ", "").isalpha():
            raise ValueError("Nama hewan hanya boleh mengandung huruf!")
        return True 
    except ValueError as e:
        print(f"  Error: {e}")
        return False

def konfirmasi_aksi(pesan):
    """
    Fungsi untuk konfirmasi ya/tidak
    """
    while True:
        try:
            jawaban = input(f"{pesan} (ya/tidak): ").lower()
            if jawaban in ['ya', 'tidak']:
                return jawaban == 'ya'
            print("Error: Masukkan 'ya' atau 'tidak'!")
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh pengguna")
            exit()