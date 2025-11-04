from prettytable import PrettyTable
from utils import tampilkan_header, clear_screen, input_teks, validasi_nama_hewan, konfirmasi_aksi

daftar_hewan = {
    "H001": "SINGA",
    "H002": "HARIMAU",
    "H003": "BUAYA", 
    "H004": "MUSANG",
}

def tampilkan_semua_hewan():
   
    if not daftar_hewan:
        print(" Daftar hewan kosong")
        return
    
    table = PrettyTable()
    table.field_names = ["Kode Hewan", "Nama Hewan"]
    table.align["Kode Hewan"] = "l"
    table.align["Nama Hewan"] = "l"
    
    for key, value in daftar_hewan.items():
        table.add_row([key, value])
    
    print("\n DAFTAR HEWAN:")
    print(table)

def tambah_hewan():
   
    clear_screen()
    tampilkan_header()
    print("TAMBAH HEWAN BARU")
    tampilkan_semua_hewan()
    
    while True:
        if konfirmasi_aksi("Ingin menambah satwa?"):
            try:
                kode = input_teks("Masukkan kode hewan (contoh: H005): ").upper()
                
                if kode in daftar_hewan:
                    print(f" Error: Kode '{kode}' sudah ada!")
                    continue
                    
                nama = input_teks("Masukkan nama hewan: ")
                
                if validasi_nama_hewan(nama):
                    daftar_hewan[kode] = nama.upper()
                    print(f" Berhasil menambahkan {nama.upper()} dengan kode {kode}")
                    
                    # Tampilkan data terbaru
                    tampilkan_semua_hewan()
                    input("Tekan enter untuk melanjutkan...")
                    clear_screen()
                    
            except Exception as e:
                print(f" Error: {e}")
                input("Tekan enter untuk melanjutkan...")
        else:
            break

def hapus_hewan():
    
    clear_screen()
    tampilkan_header()
    print("MENGHAPUS DAFTAR HEWAN")
    tampilkan_semua_hewan()
    
    if not daftar_hewan:
        input("Tekan enter untuk kembali...")
        return
        
    kode = input_teks("Masukkan kode hewan yang ingin dihapus: ").upper()
    
    try:
        if kode not in daftar_hewan:
            print(f" Error: Kode hewan '{kode}' tidak ditemukan!")
        else:
            # Konfirmasi penghapusan
            if konfirmasi_aksi(f"Yakin ingin menghapus {daftar_hewan[kode]}?"):
                nama_hewan = daftar_hewan[kode]
                del daftar_hewan[kode]
                print(f" '{nama_hewan}' berhasil dihapus")
                tampilkan_semua_hewan()
                
    except Exception as e:
        print(f" Error: {e}")
    
    input("Tekan enter untuk melanjutkan...")
    clear_screen()

def update_hewan():
    
    clear_screen()
    tampilkan_header()
    print("UPDATE INFO HEWAN")
    tampilkan_semua_hewan()
    
    if not daftar_hewan:
        input("Tekan enter untuk kembali...")
        return
        
    kode = input_teks("Masukkan kode hewan yang ingin diubah: ").upper()
    
    try:
        if kode not in daftar_hewan:
            print(f" Error: Kode hewan '{kode}' tidak ditemukan!")
        else:
            nama_baru = input_teks(f"Masukkan nama baru untuk '{daftar_hewan[kode]}': ")
            
            if validasi_nama_hewan(nama_baru):
                nama_lama = daftar_hewan[kode]
                daftar_hewan[kode] = nama_baru.upper()
                print(f" Berhasil mengubah '{nama_lama}' menjadi '{nama_baru.upper()}'")
                tampilkan_semua_hewan()
                
    except Exception as e:
        print(f" Error: {e}")
    
    input("Tekan enter untuk melanjutkan...")
    clear_screen()

def get_daftar_hewan():
    """
    Mengembalikan dictionary daftar hewan
    """
    return daftar_hewan