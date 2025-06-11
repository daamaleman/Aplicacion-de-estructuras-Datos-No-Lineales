# Example 2: Sorting using a Binary Search Tree (BST)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    # Insert a value into the tree
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
    
    # In-order traversal to get sorted values
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

def request_numbers():
    numbers = []
    print("\n=== Ingreso de Números ===")
    while True:
        try:
            num = input("Ingrese un número (o 'fin' para terminar): ")
            if num.lower() == 'fin':
                break
            numbers.append(int(num))
        except ValueError:
            print("Error: Por favor ingrese un número válido")
    return numbers

def show_menu():
    print("\n=== Menú de Ordenamiento ===")
    print("1. Ingresar nuevos números")
    print("2. Ordenar números")
    print("3. Salir")
    return input("Seleccione una opción (1-3): ")

def main():
    while True:
        option = show_menu()
        
        if option == "1":
            numbers = request_numbers()
            if numbers:
                print(f"\nNúmeros ingresados: {numbers}")
        elif option == "2":
            if 'numbers' not in locals() or not numbers:
                print("\nPrimero debe ingresar números (opción 1)")
                continue
                
            bst = BST()
            for num in numbers:
                bst.insert(num)
                
            sorted_numbers = bst.inorder()
            print(f"\nLista original: {numbers}")
            print(f"Lista ordenada: {sorted_numbers}")
        elif option == "3":
            print("\n¡Gracias por usar el programa!")
            break
        else:
            print("\nOpción no válida. Por favor seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()