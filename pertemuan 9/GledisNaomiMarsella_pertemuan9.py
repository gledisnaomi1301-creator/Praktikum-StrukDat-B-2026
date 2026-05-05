#Bagian A 

class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, judul, pengarang):
        new_node = Node(judul, pengarang)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp

    def print_forward(self):
        temp = self.head
        while temp:
            print(f"{temp.judul} - {temp.pengarang}")
            temp = temp.next

    def print_backward(self):
        temp = self.head
        if temp is None:
            return
    
        while temp.next:
            temp = temp.next
        
        while temp:
            print(f"{temp.judul} - {temp.pengarang}")
            temp = temp.prev

    def delete_by_judul(self, judul):
        temp = self.head
        
        while temp:
            if temp.judul == judul:
                
                if temp.prev is None:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
                return
            
            temp = temp.next

dll = DoubleLinkedList()

dll.insert_tail("Laskar Pelangi", "Andrea Hirata")
dll.insert_tail("Bumi Manusia", "Pramoedya Ananta Toer")
dll.insert_tail("Sang Pemimpi", "Andrea Hirata")

print("Forward:")
dll.print_forward()

print("\nBackward:")
dll.print_backward()

dll.delete_by_judul("Bumi Manusia")

print("\nSetelah dihapus:")
dll.print_forward()




#Bagian B

class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, nama):
        new_node = Node(nama)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        
        temp.next = new_node
        new_node.next = self.head

    def print_antrian(self):
        if self.head is None:
            return
        
        temp = self.head
        while True:
            print(temp.nama, end=" → ")
            temp = temp.next
            if temp == self.head:
                break
        print("(kembali ke awal)")

    def delete_head(self):
        if self.head is None:
            return
        
        if self.head.next == self.head:
            self.head = None
            return
        
        temp = self.head
        
        while temp.next != self.head:
            temp = temp.next
        
        temp.next = self.head.next
        self.head = self.head.next

cll = CircularLinkedList()

cll.insert_tail("Andi")
cll.insert_tail("Budi")
cll.insert_tail("Citra")
cll.insert_tail("Dina")

print("Antrian awal:")
cll.print_antrian()

cll.insert_tail("Edo")

print("\nSetelah Edo masuk:")
cll.print_antrian()

cll.delete_head()

print("\nSetelah Andi dilayani:")
cll.print_antrian()