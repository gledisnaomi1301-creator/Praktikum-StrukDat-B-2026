class Node:
  def __init__(self, nama, keluhan):
    self.nama = nama
    self.keluhan = keluhan
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self._size = 0

  def enqueue(self, nama, keluhan):
    new_node = Node(nama, keluhan)
    if self.tail is None:
      self.head = self.tail = new_node
      self._size += 1
      print(f"[DAFTAR] {nama.upper()} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._size})")
      return
    self.tail.next = new_node
    self.tail = new_node
    self._size += 1
    print(f"[DAFTAR] {nama.upper()} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._size})")

  def dequeue(self):
    if self.isEmpty():
      print("[ERROR] Antrian kosong!")
      return None
    
    temp = self.head
    self.head = temp.next
    self._size -= 1
    if self.head is None:
      self.tail = None

    print(f"[PANGGIL] Dokter memanggil: {temp.nama.upper()} (keluhan: {temp.keluhan})")
    return temp  

  def peek(self):
    if self.isEmpty(): 
      print("[PEEK] Antrian Kosong!")
      return None
    else:
      print(f"[PEEK] Pasien berikutnya: {self.head.nama.upper()} — {self.head.keluhan}")
      return self.head  

  def isEmpty(self):
    return self._size == 0

  def size(self):
    return self._size

  def printQueue(self):
    if self.isEmpty():
      print("[ANTRIAN KOSONG]")
      return

    print("[ANTRIAN SAAT INI]")
    temp = self.head
    nomor = 1
    while temp:
      print(f"{nomor}. {temp.nama.upper()}  {temp.keluhan}")
      temp = temp.next
      nomor += 1
    print()

  def clear(self):  
    self.head = None
    self.tail = None
    self._size = 0
    print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")


# =========================
# PROGRAM UTAMA
# =========================

myQueue = Queue()

print("====================================")
print("SISTEM ANTRIAN POLI UMUM")
print("RS Sehat Bersama")
print("====================================\n")

print("[CEK] Apakah antrian kosong? ",  
      "YA, antrian masih kosong." if myQueue.isEmpty() else "TIDAK")

myQueue.enqueue('Budi', 'demam tinggi')
myQueue.enqueue('Ani', 'batuk pilek')
myQueue.enqueue('Citra', 'sakit kepala')

print(f"\n[INFO] Jumlah pasien menunggu: {myQueue.size()} orang")

myQueue.peek()
myQueue.dequeue()
myQueue.enqueue('Dodi', 'nyeri perut')
myQueue.printQueue()
myQueue.dequeue()

print(f"[INFO] Jumlah pasien masih menunggu: {myQueue.size()} orang")

myQueue.clear()

print("[CEK] Apakah antrian kosong? ",  
      "YA, antrian sudah kosong." if myQueue.isEmpty() else "TIDAK")

print("\n====================================")
print("Simulasi Selesai!")
print("====================================")