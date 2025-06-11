class RoomNode:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.left = None
        self.right = None

class HotelTree:
    def __init__(self):
        self.root = None
    
    def insert_room(self, room_number, room_type):
        if not self.root:
            self.root = RoomNode(room_number, room_type)
        else:
            self._insert_recursive(self.root, room_number, room_type)
    
    def _insert_recursive(self, node, room_number, room_type):
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
        if node is None or node.room_number == room_number:
            return node
        if room_number < node.room_number:
            return self._search_recursive(node.left, room_number)
        return self._search_recursive(node.right, room_number)
    
    def list_rooms_inorder(self):
        self._inorder_recursive(self.root)
        print()
    
    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(f"Habitación {node.room_number}: {node.room_type}", end=" | ")
            self._inorder_recursive(node.right)

# Ejemplo de uso
if __name__ == "__main__":
    hotel = HotelTree()
    
    # Insertar habitaciones
    rooms = [
        (101, "Simple"),
        (205, "Doble"),
        (103, "Suite"),
        (204, "Simple"),
        (102, "Doble"),
        (301, "Suite")
    ]
    
    for room_number, room_type in rooms:
        hotel.insert_room(room_number, room_type)
    
    print("Lista de habitaciones (inorden):")
    hotel.list_rooms_inorder()  # Salida: Habitación 101: Simple | Habitación 102: Doble | Habitación 103: Suite | Habitación 204: Simple | Habitación 205: Doble | Habitación 301: Suite |
    
    # Buscar una habitación
    room_number = 103
    room = hotel.search_room(room_number)
    if room:
        print(f"\nHabitación encontrada: {room.room_number} ({room.room_type})")
    else:
        print(f"\nHabitación {room_number} no encontrada")
    
    # Buscar una habitación que no existe
    room_number = 999
    room = hotel.search_room(room_number)
    if room:
        print(f"Habitación encontrada: {room.room_number} ({room.room_type})")
    else:
        print(f"Habitación {room_number} no encontrada")