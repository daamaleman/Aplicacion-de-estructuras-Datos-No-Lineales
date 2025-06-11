class RoomNode:
    def __init__(self, room_number, room_type):
        self.room_number = room_number  # Clave para ordenar el árbol
        self.room_type = room_type      # Tipo de habitación
        self.left = None
        self.right = None

class HotelTree:
    def __init__(self):
        self.root = None  # Árbol inicialmente vacío
    
    def insert_room(self, room_number, room_type):
        if not self.root:
            self.root = RoomNode(room_number, room_type)  # Raíz si está vacío
        else:
            self._insert_recursive(self.root, room_number, room_type)
    
    def _insert_recursive(self, node, room_number, room_type):
        # Inserta en subárbol izquierdo (menor) o derecho (mayor/igual) según room_number
        if room_number < node.room_number:
            if node.left is None:
                node.left = RoomNode(room_number, room_type)
            else:
                self._insert_recursive(node.left, room_number, room_type)
        else:
            if node.right is None:
                node.right = RoomNode(room_number, room_type)
            else:
                self._insert_recursive(node.right, room_number, room_type)
    
    def search_room(self, room_number):
        return self._search_recursive(self.root, room_number)
    
    def _search_recursive(self, node, room_number):
        # Retorna nodo si se encuentra o None si no existe
        if node is None or node.room_number == room_number:
            return node
        return self._search_recursive(node.left if room_number < node.room_number else node.right, room_number)
    
    def list_rooms_inorder(self):
        self._inorder_recursive(self.root)  # Lista habitaciones en orden ascendente
        print()
    
    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(f"Habitación {node.room_number}: {node.room_type}", end=" | ")
            self._inorder_recursive(node.right)

if __name__ == "__main__":
    hotel = HotelTree()
    
    # Solicita cantidad de habitaciones a registrar
    try:
        num_rooms = int(input("¿Cuántas habitaciones desea registrar? "))  # Entrada validada
        print(f"Ingrese los datos para {num_rooms} habitaciones:")
        
        # Pide datos de cada habitación con validación
        for i in range(num_rooms):
            while True:
                try:
                    room_number = int(input(f"Número de habitación {i+1}: "))  # Número positivo
                    if room_number <= 0:
                        print("El número de habitación debe ser positivo.")
                        continue
                    room_type = input(f"Tipo de habitación {i+1} (Simple/Doble/Suite): ").capitalize()
                    if room_type not in ["Simple", "Doble", "Suite"]:  # Restringe tipos válidos
                        print("Tipo inválido. Use Simple, Doble o Suite.")
                        continue
                    hotel.insert_room(room_number, room_type)  # Inserta en el BST
                    break
                except ValueError:
                    print("Entrada inválida. Ingrese un número válido para la habitación.")
        
        # Muestra habitaciones ordenadas
        print("\nLista de habitaciones (inorden):")
        hotel.list_rooms_inorder()
        
        # Búsqueda interactiva hasta que el usuario decida salir
        while True:
            try:
                search_input = input("\nIngrese número de habitación a buscar (o 'salir' para terminar): ")
                if search_input.lower() == "salir":  # Condición de salida
                    break
                room_number = int(search_input)
                room = hotel.search_room(room_number)
                print(f"Habitación encontrada: {room.room_number} ({room.room_type})" if room else f"Habitación {room_number} no encontrada")
            except ValueError:
                print("Entrada inválida. Ingrese un número o 'salir'.")
    
    except ValueError:
        print("Entrada inválida. Debe ingresar un número válido de habitaciones.")