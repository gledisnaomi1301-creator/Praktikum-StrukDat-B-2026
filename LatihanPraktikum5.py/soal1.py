nilai_tugas = [70,85,90,65,80]

nilai_tugas[3] = 75
print(nilai_tugas)

nilai_tugas.append(95)
nilai_tugas.sort(reverse=True)
print(nilai_tugas)

nilai_total = sum(nilai_tugas)
print(nilai_total)


if 100 in nilai_tugas:
    print("ada nilai sempurna")
else:
    print("tidak ada")
