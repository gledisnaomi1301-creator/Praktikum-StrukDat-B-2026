pasien_hari_ini = [
    {"id": "P001", "nama": "Andi",  "usia": 34, "penyakit": 
"Flu",   "bayar": False},
    {"id": "P002", "nama": "Budi",  "usia": 22, "penyakit": 
"Tifus", "bayar": True},
    {"id": "P003", "nama": "Cici",  "usia": 45, "penyakit": 
"Flu",   "bayar": False},
    {"id": "P004", "nama": "Dani",  "usia": 30, "penyakit": 
"Maag",  "bayar": True},
    {"id": "P005", "nama": "Eva",   "usia": 28, "penyakit": 
"Tifus", "bayar": False},
    {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": 
"Maag",  "bayar": False},   
]

for i in range(len(pasien_hari_ini)):
    print("===pasien_hari_ini===")
    print(f"{i+1}. {pasien_hari_ini[i]}")




total=0
belum_bayar = []

def filter_belum_bayar(pasien_hari_ini, total):
   for i in range(len(pasien_hari_ini)):
        if i[4] == False:
           belum_bayar += i[1]

   return(belum_bayar)
  
print(len(belum_bayar)) 

info = [(" Klinik Sehat Bersama"),("Jl. Merdeka No. 10, Pekanbaru") ,("0761-12345")]

def info_klinik(info):
    print(info)



      







    
    
