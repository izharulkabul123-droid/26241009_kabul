# perogram oprator komprasi dan boolean
print("=== PROGRAM PERBANSINGAN NIM ===")
# identitas maha siswa
nama = input("Nama mahasiswa:")
nim = input("NIM lengkap")
#mengambil dua digit nim terakhir
digit_a = nim[-2]
digit_b = nim[-1]
# bilangan integer
A = int(digit_a)
B = int(digit_b)
#menampilan identitas
print("\nNama mahasiswa :", nama)
print("NIM lengkap :", nim)
print("digit A :", A)
print("digit B :", B)
#menampilkan hasil perbandingan 
print("A > B :", A > B)
print("A < B :", A < B)
print("A == B :", A == B)
print(" A != B :", A != B)
print("A >= B :", A >= B)
print("A <= B :", A <= B)