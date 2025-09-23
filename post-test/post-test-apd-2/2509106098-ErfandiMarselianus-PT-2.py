name = "Erfandi Marselianus"
nim = 2509106098
harga = 1000000
acer = 5
asus = 7
lenovo = 10
laptop = "acer,asus,lenovo"
print(name + " dengan NIM " + str(nim) + " ingin membeli laptop seharga " + str(harga))
print("dengan rincian diskon [Acer 5%] [Asus 7%] [Lenovo 10%]")
print("harga laptop setelah diskon adalah")
diskon = harga * acer / 100
hargaAkhir = harga - diskon
print("1, jika Erfandi membeli laptop acer |Rp" + str(hargaAkhir)+"|")
diskon = harga * asus / 100
hargaAkhir = harga - diskon
print("2, jika Erfandi membeli laptop asus |Rp" + str(hargaAkhir)+"|")
diskon = harga * lenovo / 100
hargaAkhir = harga - diskon
print("3, jika Erfandi membeli laptop lenovo|Rp" + str(hargaAkhir)+"|")

