# #praktikum = ["Mahasiswa", 20, True, 45.10, ["APD",25]]
# #praktikum = ["mahasiswa",20, True,45.10, ["APD",25]]
# #(praktikum[4][0])  

# #studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# #studyclub.append("Web")
# #print(studyclub)

# # list awal
# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# studyclub.insert(2,"Web")
# print(studyclub)

# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# print(studyclub)
# studyclub[2] = "AI"
# print(studyclub)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# del matakuliah[2]
# print(matakuliah)


# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # matakuliah.remove('Kalkulus')
# del matakuliah[0:]
# print(matakuliah)


# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # Menghapus & mengambil elemen 'Kalkulus' pada indeks ke-2
# ambil_matkul = matakuliah.pop(2)
# print(matakuliah)
# print(ambil_matkul)


# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
# 'Orsikom','Basis Data']
# # Menampilkan list mulai dari indeks 1 hingga 5 dengan loncatan 2
# print(matakuliah[::2])

a = [1, 2, 3]
b = [4, 5, 6]
# menggabungkan kedua list dengan operator (+)
c = a + b
print(c)


# kelas = [
# ["Ridho", "Lian", "Nabil"],
# ["Daffa", "Dante", "Santoso"]
# ["Pernanda", "Riyadi", "Ahnaf"],
# print(kelas[1][1])

# ]


mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]
# perulangan for untuk mendapatkan semua elemen
for i in mahasiswa:
        for j in i :
         print (j)