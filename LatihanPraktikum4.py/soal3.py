sesi_pagi = {"Andi", "Budi", "Cici"}
sesi_siang = {"Budi", "Deni", "Eka"}

print(sesi_pagi & sesi_siang)

kehadiran = sesi_pagi | sesi_siang
print(kehadiran)

sesi_hari_ini = sesi_pagi.union(sesi_siang)
print(sesi_hari_ini)