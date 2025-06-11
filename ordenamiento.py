# Ejemplo 2: Ordenamiento usando un Árbol Binario de Búsqueda (BST)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    # Insertar un valor en el árbol
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    # Recorrido en orden (in-order) para obtener los valores ordenados
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

# Ejemplo de uso del BST para ordenar una lista
numbers = [5, 2, 8, 1, 9, 3]
bst = BST()
for num in numbers:
    bst.insert(num)

sorted_numbers = bst.inorder()
print(f"Lista original: {numbers}")
print(f"Lista ordenada: {sorted_numbers}")