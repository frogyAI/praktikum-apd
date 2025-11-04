from auth import login
from animal_operations import *
from utils import clear_screen, tampilkan_header

def tampilkan_menu():
    menu_awal = {
        "1": "DAFTAR HEWAN",
        "2": "MENAMBAH DAFTAR HEWAN", 
        "3": "MENGHAPUS DAFTAR HEWAN",
        "4": "UPDATE INFO HEWAN", 
        "5": "KELUAR PROGRAM"
    }
    
   
    from prettytable import PrettyTable
    
    table = PrettyTable()
    table.field_names = ["Pilihan", "Menu"]
    table.align["Pilihan"] = "c"
    table.align["Menu"] = "l"
    
    for key, value in menu_awal.items():
        table.add_row([key, value])
    
    print("\nDAFTAR MENU SATWA KEBUN BINATANG")
    print(table)

def main():
   
    if not login():
        return
    
    clear_screen()
    
    while True:
        tampilkan_header()
        tampilkan_menu()
        
        try:
            pilih_menu = input("PILIH MENU [1-5]: ")
        except KeyboardInterrupt:
            print("\n Program dihentikan oleh pengguna")
            exit()
            
        print()

        if pilih_menu == "1":
            clear_screen()
            tampilkan_header()
            tampilkan_semua_hewan()
            input("\nTekan enter untuk kembali ke menu...")
            clear_screen()
            
        elif pilih_menu == "2":
            tambah_hewan()
            
        elif pilih_menu == "3":
            hapus_hewan()
            
        elif pilih_menu == "4":
            update_hewan()
             
        elif pilih_menu == "5":
            clear_screen()
            tampilkan_header()
            print("Terima kasih telah menggunakan program!")
            break
            
        else: 
            clear_screen()
            print("Error: Menu yang dipilih tidak ada!")
            input("Tekan enter untuk melanjutkan...")
            clear_screen()

if __name__ == "__main__":
    main()