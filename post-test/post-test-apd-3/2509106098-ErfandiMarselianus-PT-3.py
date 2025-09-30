ukt = 6000000
biayaAdmin = 1
biayaAdmin2X = 5
biayaAdmin4X = 8
biayaAdmin6X = 12
print("masukan nama")
nama = input()
if nama == "erfandi marselianus":
    print("masukan nim")
    nim = int(input())
    if nim == 2509106098:
        print("OPSI PEMBAYARAN UKT")
        print("Lunas(sekali bayar) dengan biaya administrasi 1%")
        print("Cicilan 2X per semester dengan biaya andministrasi 5%")
        print("Cicilan 4X per semester dengan biaya andministrasi 8%")
        print("Cicilan 6X per semester dengan biaya andministrasi 12%")
        print("DAN TOTAL YANG HARUS DIBAYAR SESUAI OPSI ADALAH")
        totalBayar = ukt + float(ukt * biayaAdmin) / 100
        print("UNTUK OPSI SEKALI BAYAR,TOTALNYA ADALAH |Rp" + str(totalBayar) + "|")
        totalBayar = ukt + float(ukt * biayaAdmin2X) / 100
        cicilan = float(totalBayar) / 2
        print("UNTUK YANG CICIL 2X,TOTALNYA ADALAH |Rp" + str(totalBayar) + "| dengan membayar besaran cicilan |Rp" + str(cicilan) + "| sebanyak 2X per semester")
        totalBayar = ukt + float(ukt * biayaAdmin4X) / 100
        cicilan = float(totalBayar) / 4
        print("UNTUK YANG CICIL 4X,TOTALNYA ADALAH |Rp" + str(totalBayar) + "| dengan membayar besaran cicilan |Rp" + str(cicilan) + "| sebanyak 4X per semester")
        totalBayar = ukt + float(ukt * biayaAdmin6X) / 100
        cicilan = float(totalBayar) / 6
        print("UNTUK YANG CICIL 6X,TOTALNYA ADALAH |Rp" + str(totalBayar) + "| dengan membayar besaran cicilan |Rp" + str(cicilan) + "| sebanyak 6X per semester")
    else:
        print("nim yang anda masukan salah,silahkan ulangi dari awal")
else:
    print("nama yang anda masukan salah,silahkan masukan ulang dengan nama yang benar")
