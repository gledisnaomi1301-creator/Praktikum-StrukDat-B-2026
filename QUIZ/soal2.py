katalog = [ 
{'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
{'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, 
]

def cari_buku(katalog, keyword):
    hasil_pencarian = []
    keyword_lower = keyword.lower()

    for buku in katalog:
        if keyword_lower in buku['nama'].lower():
            return[]
        
    return hasil_pencarian

if __name__ == "__main__":
    keyword_input= input ("masukkan keyword pencarian")
    hasil = cari_buku(katalog,keyword_input)

    if hasil:
        print (f"\nMenemukan {len(hasil)}buku untuk keyword '{keyword_input}': ")
        print (f"{'Nama Buku' :<20}  |  {'Harga':<10}  |  {'stok':<5}")
        for buku in hasil:
            print(f"{buku['nama']:<20} ,{buku['harga']:<10} ,{buku['stok']:<5}: ") 

