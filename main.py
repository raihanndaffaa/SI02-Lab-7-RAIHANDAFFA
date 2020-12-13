# Nama: Raihan Daffa Aziz
# NIM:  0110120020
# Kelas: SI 02

def convert_list(multilist):
  # Tulis kode fungsi convert_list() di bawah ini
  list_data = []
  #BUAT VARIABEL list_data AGAR NANTI SAAT DI PANGGIL OTOMATIS MENJADI LIST
  for i in range(len(multilist)):
  #LOOP DARI JUMLAH LIST 2 DIMENSI
    for j in range(len(multilist[i])):
    #LOOP DARI JUMLAH LIST DIDALAM DIMENSI
      hasil = multilist[i][j]
      #VARIABEL HASIL BERISI MASING MASING ISI DARI
      list_data.append(hasil)
      #BUAT LIST YANG SUDAH DIPISAH, DI BUAT LIST BARU
  return list_data
  #RETURN UNTUK MENGEMBALIKAN NILAI YANG SUDAH DIBUAT

def get_nilai(filename, nama):
  # Tulis kode fungsi get_nilai() di bawah ini
  f = open(filename)
  #OPEN FILE DATA MENGGUNAKAN OPEN LALU AMBIL NAMAFILE DARI VARIABEL FILENAME
  for garis in f:
  #LOOP SEMUA ISI DARI FILE NAME TERSEBUT MENGGUNAKAN PERULANGAN FOR
    data = garis.split()
  #BUAT VARIABEL DATA (BARIS KE 21) YANG GUNANYA MENGUBAH ISI DARI FILE MENJADI LIST
    namanya = data[0]
  #VARIABEL NAMANYA BERFUNGSI MENGAMBIL DATA NAMA, KARENA ARRAY BERMULAI DARI 0 MAKA PEMANGGILANNYA SEPERTI PADA BARIS KE 23
    if(namanya.lower() == nama.lower()):
  #LOWER BERFUNGSI MERUBAH STRING MENJADI HURUF KECIL, DISINI DIBUAT VARIABEL NAMA DARI DATA JADI HURUF KECIL DAN VARIABEL NAMA YANG DIAMBIL DARI FUNCTION JADI KECIL, JADI KEDUA DATA SAMA
      nilai = float(data[1])
  #AMBIL DATA NILAI MENGGUNAKAN DATA LALU 1, LALU SAYA UBAH KE FLOAT AGAR MEMBERI TAU BAHWA INI TIPEDATA NUMBER FLOAT
      return round(nilai)
   #PAKAI ROUND UNTUK MEMBULATKAN NOMOR YANG TELAH DIBUAT
    else:
      pass
  #SELAIN ITU DI SKIP, KARENA TIDAK ADA RETURN OTOMATIS RETURNNYA NONE, ALIAS TIDAK ADA NILAI KEMBALI

def nilai_max(filename):
  list_data = []
  list_nilai = []
  #BUAT BARIABEL UNTUK JADIKAN LIST
  f = open(filename)
  #OPEN FILE DATA MENGGUNAKAN OPEN LALU AMBIL NAMAFILE DARI VARIABEL FILENAME

  for n in f:
  #LOOP SEJUMLAH YANG ADA DI FILE YANG SUDAH DI OPEN
    data = n.split()
    nama = data[0]
    nilai = float(data[1])
    #VARIABEL NAMA DAN NILAI DIAMBIL DARI SPLIT DATA PADA LIST YANG DI OPEN, ARRAY BERAWAL DARI 0, MAKA JIKA INGIN AMBIL NAMA DI AMBIL DARI data[0] DAN DATA NILAI DIAMBIL DARI data[1]
    list_nilai.append(nilai)
    list_data.append([nama, nilai])
    #BARIS KE 53 DAN 54 ITU UNTUK MENGUBAH YANG SUDAH DI PISAH, JADI LIST BARU
  jum = len(list_data)-1
  #JUM MENGHITUNG JUMLAH LIST DATA YANG SUDAH BARU DIBUAT, DIKURANGI 1 KARENA LEN NYA KETIKA DI LOOP JADI KELEBIH 1 DATA
  data_akhir = sorted(list_nilai, key=float)
  #LALU VARIABEL DATA AKHIR AKAN MENSORTIR DATA NILAI DARI TERKECIL KE TERBESAR
  for i in range(jum):
    #LOOP LAGI DARI JUMLAH KESELURUHAN DIAMBIL DARI VARIABEL JUM
    if list_data[i][1] == data_akhir[jum]:
      #JIKA LIST DATA INI SAMA DENGAN DATA NILAI
      return list_data[i][0], list_data[i][1]
      #MAKA AKAN DI RETURN NAMA SEKALIGUS NILAINYA
    else:
      pass
    #SELAIN ITU AKAN DI PASS, ALIAS NONE / TIDAK ADA NILAI KEMBALI


# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = convert_list([[1,2], [3,4], [5,6]])
  print(f"convert_list([[1,2], [3,4], [5,6]]) = {r} \n(solusi: [1, 2, 3, 4, 5, 6])")
  print()
  r = get_nilai('nilai1.txt','joni')
  print(f"get_nilai('nilai1.txt','joni') = {r} \n(solusi: 76)")
  print()
  r = get_nilai('nilai2.txt','joni')
  print(f"get_nilai('nilai2.txt','joni') = {r} \n(solusi: None)")
  print()
  r = nilai_max('nilai1.txt')
  print(f"nilai_max('nilai1.txt') = {r} \n(solusi: ('Zack', 88.05)")
  print()
  r = nilai_max('nilai2.txt')
  print(f"nilai_max('nilai2.txt') = {r} \n(solusi: ('Arya', 90.00)")
  print()

if __name__ == '__main__':
  test()