import pandas as pd

nama_siswa = ['Andi', 'Bella', 'Candra', 'Daniel', 'Eka']
nilai_siswa = {
    'Andi': 100,
    'Bella': 95,
    'Candra': 80,
    'Daniel': 85,
    'Eka': 90
}

print(nama_siswa)
print(nilai_siswa)

# menambahkan dan mengapus satu siswa
nama_siswa.append('Fanny')
del nama_siswa[2]

print(nama_siswa)

# mencetak nama siswa pertama dan terakhir, cetak 3 siswa terakhir
print(nama_siswa[0::4])
print(nama_siswa[2:])

# cetak index dan nama siswa
for i in range(len(nama_siswa)):
    print(f"Index {i} -> {nama_siswa[i]}")

# ubah nilai ujian siswa dan hapus data siswa dengan pop
nilai_siswa['Daniel'] = 78
nilai_siswa.pop('Bella')

print(nilai_siswa)

# ganti key nama siswa 
nilai_siswa['Eli'] = nilai_siswa.pop('Eka')
print(nilai_siswa)