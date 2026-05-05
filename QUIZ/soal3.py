katalog = [ 
{'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
{'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, 
]

riwayat_transaksi = set()

def proses_transaksi(katalog,nama_buku,jumlah_beli):
    print(f"\nMemproses Pembelian :{nama_buku} (jumlah : {jumlah_beli})")

    buku_ketemu = False

    for buku in katalog:
        if buku ['nama'].lower()== nama_buku.lower():
            buku_ketemu = True
            
        
