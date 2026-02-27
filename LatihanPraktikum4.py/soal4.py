transaksi = [ 
{"produk": "Buku", "harga": 10000, "jumlah": 3}, 
{"produk": "Pena", "harga": 5000, "jumlah": 10}, 
{"produk": "Penghapus", "harga": 2000, "jumlah": 2} 
] 

transaksi[0]["jumlah"]= 8
print(transaksi)

transaksi += [{"produk": "pensil", "harga":2000 , "jumlah":7}]
transaksi += [{"produk": "penggaris", "harga":7000 , "jumlah":8}]
print(transaksi)


for i in range(len(transaksi)):
    print(f"produk {transaksi[i]["produk"]} | total: {transaksi[i]["harga"] * transaksi[i]["jumlah"]}")
      

