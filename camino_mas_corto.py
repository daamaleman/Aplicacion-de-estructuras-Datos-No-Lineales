# Example 1: Dijkstra's Algorithm for finding the shortest path in a graph
import heapq
from collections import defaultdict

def dijkstra(graph, start, end):
    # Priority queue to explore nodes (distance, node)
    queue = [(0, start)]
    # Dictionary to store minimum distances
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    # Dictionary to store the path
    previous = {node: None for node in graph}
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        # If we reached the destination node, build the path
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous[current_node]
            return path[::-1], current_distance
        
        # If we found a greater distance, ignore
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If we found a shorter distance, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    
    return None, float('infinity')  # No path found

def create_graph():
    graph = {}
    print("\n=== Creación del Grafo ===")
    num_nodes = int(input("Ingrese el número de nodos: "))
    
    # Create nodes
    for i in range(num_nodes):
        node = input(f"Ingrese el nombre del nodo {i+1}: ").upper()
        graph[node] = {}
    
    # Create connections
    print("\nAhora ingrese las conexiones entre nodos:")
    while True:
        print("\nOpciones:")
        print("1. Agregar conexión")
        print("2. Finalizar")
        option = input("Seleccione una opción (1-2): ")
        
        if option == "2":
            break
        elif option == "1":
            origin = input("Ingrese el nodo de origen: ").upper()
            destination = input("Ingrese el nodo de destino: ").upper()
            
            if origin not in graph or destination not in graph:
                print("Error: Uno o ambos nodos no existen en el grafo")
                continue
                
            weight = float(input("Ingrese el peso de la conexión: "))
            
            # Add bidirectional connection
            graph[origin][destination] = weight
            graph[destination][origin] = weight
            print(f"Conexión agregada: {origin} <-> {destination} con peso {weight}")
        else:
            print("Opción no válida")
    
    return graph

def show_menu():
    print("\n=== Menú Principal ===")
    print("1. Crear nuevo grafo")
    print("2. Buscar camino más corto")
    print("3. Salir")
    return input("Seleccione una opción (1-3): ")

def find_path(graph):
    print("\n=== Buscar camino más corto ===")
    start = input("Ingrese el nodo de inicio: ").upper()
    end = input("Ingrese el nodo de destino: ").upper()

    if start not in graph or end not in graph:
        print("Error: Uno o ambos nodos no existen en el grafo")
        return
    
    path, cost = dijkstra(graph, start, end)
    if path:
        print(f"\nCamino más corto de {start} a {end}: {' -> '.join(path)}")
        print(f"Costo total: {cost}")
    else:
        print(f"\nNo se encontró un camino de {start} a {end}")

def main():
    graph = None
    
    while True:
        option = show_menu()
        
        if option == "1":
            graph = create_graph()
            print("\nGrafo creado exitosamente!")
            
        elif option == "2":
            if graph is None:
                print("\nPrimero debe crear un grafo (opción 1)")
                continue
            find_path(graph)
            
        elif option == "3":
            print("\n¡Gracias por usar el programa!")
            break
            
        else:
            print("\nOpción no válida. Por favor seleccione 1, 2 o 3.")

if __name__ == "__main__":
    print("=== Algoritmo de Dijkstra para encontrar el camino más corto ===")
    main()