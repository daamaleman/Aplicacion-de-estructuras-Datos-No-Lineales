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

# Ejemplo de uso del algoritmo de Dijkstra
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

path, cost = dijkstra(graph, 'A', 'E')
print(f"Camino más corto de A a E: {path}")
print(f"Costo total: {cost}")