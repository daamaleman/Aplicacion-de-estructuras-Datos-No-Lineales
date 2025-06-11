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

def solicitar_numeros():
    numeros = []
    print("\n=== Ingreso de Números ===")
    while True:
        try:
            num = input("Ingrese un número (o 'fin' para terminar): ")
            if num.lower() == 'fin':
                break
            numeros.append(int(num))
        except ValueError:
            print("Error: Por favor ingrese un número válido")
    return numeros

def mostrar_menu():
    print("\n=== Menú de Ordenamiento ===")
    print("1. Ingresar nuevos números")
    print("2. Ordenar números")
    print("3. Salir")
    return input("Seleccione una opción (1-3): ")

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            numeros = solicitar_numeros()
            if numeros:
                print(f"\nNúmeros ingresados: {numeros}")
        elif opcion == "2":
            if 'numeros' not in locals() or not numeros:
                print("\nPrimero debe ingresar números (opción 1)")
                continue
                
            bst = BST()
            for num in numeros:
                bst.insert(num)
                
            numeros_ordenados = bst.inorder()
            print(f"\nLista original: {numeros}")
            print(f"Lista ordenada: {numeros_ordenados}")
        elif opcion == "3":
            print("\n¡Gracias por usar el programa!")
            break
        else:
            print("\nOpción no válida. Por favor seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()