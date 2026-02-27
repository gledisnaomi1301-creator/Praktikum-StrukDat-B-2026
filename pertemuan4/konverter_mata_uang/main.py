from kurs import kurs
from konverter import idr_ke_mata_uang, mata_uang_ke_idr
from tabulate import tabulate

def tampilkan_kurs():
    tabel = []
    for mata_uang, nilai in kurs.items():
        tabel.append([mata_uang, nilai])

    print(tabulate(tabel, headers=["Mata Uang", "Nilai ke IDR"], tablefmt="grid"))

def main():
    tampilkan_kurs()

    print("\n1. IDR ke Mata Uang Asing")
    print("2. Mata Uang Asing ke IDR")

    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        jumlah = float(input("Masukkan jumlah IDR: "))
        mata_uang = input("Masukkan kode mata uang: ").upper()
        hasil = idr_ke_mata_uang(jumlah, mata_uang)

        if hasil:
            print(f"Hasil: {hasil:.2f} {mata_uang}")
        else:
            print("Mata uang tidak tersedia")

    elif pilihan == "2":
        jumlah = float(input("Masukkan jumlah: "))
        mata_uang = input("Masukkan kode mata uang: ").upper()
        hasil = mata_uang_ke_idr(jumlah, mata_uang)

        if hasil:
            print(f"Hasil: Rp {hasil:,.2f}")
        else:
            print("Mata uang tidak tersedia")

if __name__ == "__main__":
    main()