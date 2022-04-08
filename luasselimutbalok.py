print("Menghitung Balok")
print("=========================")
panjang = int(input("Masukan Panjang :"))
lebar = int(input("Masukan Lebar :"))
tinggi = int(input("Masukan Tinggi :"))
luas_selimut = 2 * panjang * lebar + 2 * lebar *panjang + 2 * panjang * tinggi
volume = panjang * lebar * tinggi

print(f"Luas Selimut = {luas_selimut}")
print(f"Volume       = {volume}")
print(f"Dimensi Balok = {panjang} x {lebar} x {tinggi}")
