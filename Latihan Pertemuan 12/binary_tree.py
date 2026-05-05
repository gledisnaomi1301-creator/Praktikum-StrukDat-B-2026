class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # INSERT MANUAL
    def insert_manual(self):
        print("[INFO] Membangun Struktur Gudang...")

        self.root = Node("A")
        self.root.left = Node("B")
        self.root.right = Node("C")

        self.root.left.left = Node("D")
        self.root.left.right = Node("E")

        self.root.right.right = Node("F")

        print("[INFO] Struktur berhasil dibuat.\n")

    # PREORDER (Root - Left - Right)
    def traverse_preorder(self, node):
        if node:
            print(node.data, end=" - ")
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

    # INORDER (Left - Root - Right)
    def traverse_inorder(self, node):
        if node:
            self.traverse_inorder(node.left)
            print(node.data, end=" - ")
            self.traverse_inorder(node.right)

    # POSTORDER (Left - Right - Root)
    def traverse_postorder(self, node):
        if node:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print(node.data, end=" - ")

    # GET LEAF NODES
    def get_leaf_nodes(self, node):
        if node is None:
            return []

        if node.left is None and node.right is None:
            return [node.data]

        return self.get_leaf_nodes(node.left) + self.get_leaf_nodes(node.right)



tree = BinaryTree()

tree.insert_manual()

print("HASIL AUDIT:")

print("1. Pre-Order :", end=" ")
tree.traverse_preorder(tree.root)
print()

print("2. In-Order :", end=" ")
tree.traverse_inorder(tree.root)
print()

print("3. Post-Order :", end=" ")
tree.traverse_postorder(tree.root)
print()

leaf_nodes = tree.get_leaf_nodes(tree.root)
print("\n[DATA] Gudang Ujung (Leaf Nodes):", ", ".join(leaf_nodes))

print("\n======================================")
print("Audit Selesai!")