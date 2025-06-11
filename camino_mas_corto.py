# Ejemplo 1: Algoritmo de Dijkstra para encontrar el camino más corto en un grafo
import heapq
from collections import defaultdict

def dijkstra(graph, start, end):
    # Cola de prioridad para explorar nodos (distancia, nodo)
    queue = [(0, start)]
    # Diccionario para almacenar distancias mínimas
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    # Diccionario para almacenar el camino
    previous = {node: None for node in graph}
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        # Si llegamos al nodo destino, construimos el camino
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous[current_node]
            return path[::-1], current_distance
        
        # Si encontramos una distancia mayor, ignoramos
        if current_distance > distances[current_node]:
            continue
        
        # Exploramos los vecinos
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Si encontramos una distancia menor, actualizamos
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    
    return None, float('infinity')  # No se encontró camino

def crear_grafo():
    grafo = {}
    print("\n=== Creación del Grafo ===")
    num_nodos = int(input("Ingrese el número de nodos: "))
    
    # Crear nodos
    for i in range(num_nodos):
        nodo = input(f"Ingrese el nombre del nodo {i+1}: ").upper()
        grafo[nodo] = {}
    
    # Crear conexiones
    print("\nAhora ingrese las conexiones entre nodos:")
    while True:
        print("\nOpciones:")
        print("1. Agregar conexión")
        print("2. Finalizar")
        opcion = input("Seleccione una opción (1-2): ")
        
        if opcion == "2":
            break
        elif opcion == "1":
            origen = input("Ingrese el nodo de origen: ").upper()
            destino = input("Ingrese el nodo de destino: ").upper()
            
            if origen not in grafo or destino not in grafo:
                print("Error: Uno o ambos nodos no existen en el grafo")
                continue
                
            peso = float(input("Ingrese el peso de la conexión: "))
            
            # Agregar conexión bidireccional
            grafo[origen][destino] = peso
            grafo[destino][origen] = peso
            print(f"Conexión agregada: {origen} <-> {destino} con peso {peso}")
        else:
            print("Opción no válida")
    
    return grafo

def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Crear nuevo grafo")
    print("2. Buscar camino más corto")
    print("3. Salir")
    return input("Seleccione una opción (1-3): ")

def buscar_camino(grafo):
    print("\n=== Buscar camino más corto ===")
    inicio = input("Ingrese el nodo de inicio: ").upper()
    fin = input("Ingrese el nodo de destino: ").upper()

    if inicio not in grafo or fin not in grafo:
        print("Error: Uno o ambos nodos no existen en el grafo")
        return
    
    path, cost = dijkstra(grafo, inicio, fin)
    if path:
        print(f"\nCamino más corto de {inicio} a {fin}: {' -> '.join(path)}")
        print(f"Costo total: {cost}")
    else:
        print(f"\nNo se encontró un camino de {inicio} a {fin}")

def main():
    grafo = None
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            grafo = crear_grafo()
            print("\nGrafo creado exitosamente!")
            
        elif opcion == "2":
            if grafo is None:
                print("\nPrimero debe crear un grafo (opción 1)")
                continue
            buscar_camino(grafo)
            
        elif opcion == "3":
            print("\n¡Gracias por usar el programa!")
            break
            
        else:
            print("\nOpción no válida. Por favor seleccione 1, 2 o 3.")

if __name__ == "__main__":
    print("=== Algoritmo de Dijkstra para encontrar el camino más corto ===")
    main()