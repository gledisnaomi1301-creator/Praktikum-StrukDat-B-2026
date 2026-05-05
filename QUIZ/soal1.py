def tambah_buku(nama, harga, stok):
    if harga < 0:
        print ("Error ")
        return None
    
    if  stok < 0:
        print ("Error")
        return None
    
    return{
        "nama" : nama,
        "harga" : harga,
        "stok" : stok 
    }

daftar_buku = []
    
for i in range(3):
    print(f"\nData Buku ke-{i+1}: ")
    nama = input ("nama: ")
    harga = input ("harga: ")
    stok = input ("stok: ")

buku = tambah_buku(nama,harga,stok)

for buku in nama,harga,stok:
    i+=1
    print(buku)

   




 
    