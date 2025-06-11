from collections import defaultdict, deque

class TransportGraph:
    def __init__(self):
        # Grafo como lista de adyacencia
        self.graph = defaultdict(list)
    
    def add_route(self, station1, station2):
        # Agregar conexión bidireccional (grafo no dirigido)
        self.graph[station1].append(station2)
        self.graph[station2].append(station1)
    
    def dfs(self, start_station):
        # Recorrido DFS (búsqueda en profundidad)
        visited = set()
        print("Recorrido DFS desde", start_station, ":", end=" ")
        self._dfs_recursive(start_station, visited)
        print()
    
    def _dfs_recursive(self, station, visited):
        visited.add(station)
        print(station, end=" ")
        for neighbor in self.graph[station]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)
    
    def bfs(self, start_station):
        # Recorrido BFS (búsqueda en amplitud)
        visited = set()
        queue = deque([start_station])
        visited.add(start_station)
        print("Recorrido BFS desde", start_station, ":", end=" ")
        
        while queue:
            station = queue.popleft()
            print(station, end=" ")
            for neighbor in self.graph[station]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

# Ejemplo de uso
if __name__ == "__main__":
    transport = TransportGraph()
    
    # Agregar rutas entre estaciones
    routes = [
        ("Central", "Norte"),
        ("Central", "Sur"),
        ("Norte", "Este"),
        ("Sur", "Oeste"),
        ("Este", "Noreste"),
        ("Oeste", "Suroeste"),
        ("Central", "Oeste"),
        ("Norte", "Noroeste")
    ]
    
    for station1, station2 in routes:
        transport.add_route(station1, station2)
    
    # Realizar recorridos
    print("Red de transporte público:")
    transport.dfs("Central")  # Ejemplo: Central Norte Este Noreste Noroeste Sur Oeste Suroeste
    transport.bfs("Central")  # Ejemplo: Central Norte Sur Oeste Este Noroeste Suroeste Noreste