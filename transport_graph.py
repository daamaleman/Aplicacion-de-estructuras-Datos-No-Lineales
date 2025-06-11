from collections import defaultdict, deque

class TransportGraph:
    def __init__(self):
        self.graph = defaultdict(list)  # Grafo como lista de adyacencia
    
    def add_route(self, station1, station2):
        self.graph[station1].append(station2)  # Conexión bidireccional
        self.graph[station2].append(station1)
    
    def dfs(self, start_station):
        visited = set()
        print("Recorrido DFS desde", start_station, ":", end=" ")
        self._dfs_recursive(start_station, visited)  # Inicia DFS recursivo
        print()
    
    def _dfs_recursive(self, station, visited):
        visited.add(station)
        print(station, end=" ")
        for neighbor in self.graph[station]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)  # Explora vecinos no visitados
    
    def bfs(self, start_station):
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
                    queue.append(neighbor)  # Agrega vecinos a la cola
        print()

if __name__ == "__main__":
    transport = TransportGraph()
    
    # Solicitar cantidad de rutas a registrar
    try:
        num_routes = int(input("¿Cuántas rutas desea registrar? "))  # Entrada validada
        print(f"Ingrese {num_routes} rutas (parejas de estaciones):")
        
        # Pedir estaciones y conexiones
        for i in range(num_routes):
            while True:
                try:
                    station1 = input(f"Estación 1 de la ruta {i+1}: ").strip()
                    station2 = input(f"Estación 2 de la ruta {i+1}: ").strip()
                    if not station1 or not station2:
                        print("Las estaciones no pueden estar vacías.")
                        continue
                    transport.add_route(station1, station2)  # Agrega conexión al grafo
                    break
                except ValueError:
                    print("Entrada inválida. Ingrese nombres de estaciones válidos.")
        
        # Listar estaciones registradas
        print("\nEstaciones registradas:", list(transport.graph.keys()))
        
        # Solicitar estación inicial para recorridos
        while True:
            start_station = input("\nIngrese la estación inicial para los recorridos (o 'salir' para terminar): ").strip()
            if start_station.lower() == "salir":
                break
            if start_station not in transport.graph:
                print(f"La estación {start_station} no existe en la red.")
                continue
            # Realizar recorridos DFS y BFS
            print("\nRed de transporte público:")
            transport.dfs(start_station)
            transport.bfs(start_station)
    
    except ValueError:
        print("Entrada inválida. Debe ingresar un número válido de rutas.")