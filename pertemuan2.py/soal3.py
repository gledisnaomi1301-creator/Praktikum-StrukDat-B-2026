kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}


set1 = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
set2 = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

set1.update(set2)
print(set1)



set1 = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
set2 = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

set3 = set1.difference(set2)

print(set3)



set1 = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
set2 = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

set3 = set1.symmetric_difference(set2)
print(set3)
