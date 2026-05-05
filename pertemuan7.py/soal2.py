#Implementasi pada List Array

antrean_array =[ "Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

def sisipkan_pasien_darurat_array(nama_pasien, posisi):
    antrean_array.insert(posisi - 1, nama_pasien)

sisipkan_pasien_darurat_array("Pasien D (Darurat)", 2)

print("Antrean Pasien:", antrean_array)



#Implementasi pada Singly LinkedList

class Node:
    def __init__(self, nama_pasien):
        self.nama_pasien = nama_pasien
        self.next = None



class AntreanLinkedList:
    def __init__(self):
        self.head = None

    
    def append(self, nama_pasien):
        new_node = Node(nama_pasien)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node


    def length(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    
    def insert_at_position(self, nama_pasien, posisi):
        new_node = Node(nama_pasien)

       
        if posisi == 1:
            new_node.next = self.head
            self.head = new_node
            return

        
        if posisi > self.length():
            self.append(nama_pasien)
            return

        current = self.head
        count = 1

        
        while count < posisi - 1:
            current = current.next
            count += 1

        new_node.next = current.next
        current.next = new_node

    
    def display(self):
        current = self.head

        while current:
            print(current.nama_pasien, "->", end=" ")
            current = current.next

        print("None")


# ===============================
# Program utama
# ===============================

antrean = AntreanLinkedList()

antrean.append("Pasien A (Stabil)")
antrean.append("Pasien B (Stabil)")
antrean.append("Pasien C (Stabil)")

print("Antrean awal:")
antrean.display()

antrean.insert_at_position("Pasien D (Darurat)", 2)

print("\nAntrean setelah pasien darurat:")
antrean.display()