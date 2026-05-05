#Implementasi Menggunakan List (Array) Python

history_array = ["google.com", "python.org"]

def tambah_pencarian_array(keyword):
    history_array.insert(0, keyword)

tambah_pencarian_array("PUBG MOBILE")
print("History Array:", history_array)



#Implementasi Menggunakan Singly LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class HistoryLinkedList:
    def __init__(self):
        self.head = None

    def tambah_pencarian_linked(self, keyword):
        new_node = Node(keyword)
        new_node.next = self.head
        self.head = new_node

    def tampilkan_history(self):
        current = self.head
        while current:
            print(current.data, "->", end=" ")
            current = current.next
        print("None")



history = HistoryLinkedList()


history.tambah_pencarian_linked("python.org")
history.tambah_pencarian_linked("google.com")
history.tambah_pencarian_linked("github.com")


print("Riwayat Pencarian:")
history.tampilkan_history()






