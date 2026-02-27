class MySawit:
  def __init__(self,nama, umur, rambut):
    self.nama = nama
    self.umur = umur
    self.rambut = rambut

  def panggil_nama(self):
    print(f"nama saya {self.nama}")
    
  def panggil_umur(self):
    print(f"umur saya {self.umur}")

MySawit1 = MySawit("Mingyu", 28, "comma hair")
MySawit2 = MySawit("Blio", 20, "two block")
MySawit3 = MySawit("Kanglim", 26, "mullet")

print(MySawit1.nama, MySawit1.umur,MySawit1.rambut)
print(MySawit2.nama, MySawit2.umur,MySawit2.rambut)
print(MySawit3.nama, MySawit3.umur,MySawit3.rambut)

MySawit3.umur = 34














