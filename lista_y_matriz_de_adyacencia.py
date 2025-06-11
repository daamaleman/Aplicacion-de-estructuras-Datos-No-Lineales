def menu():
    print("\n1. Agregar vértices")
    print("2. Agregar arista")
    print("3. Mostrar lista de adyacencia")
    print("4. Mostrar matriz de adyacencia")
    print("5. Salir")

# Inicialización
vertices = []
lista_adyacencia = {}
matriz_adyacencia = []

def actualizar_matriz():
    size = len(vertices)
    matriz_adyacencia.clear()
    for _ in range(size):
        matriz_adyacencia.append([0] * size)

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        entrada = input("Ingrese los vértices separados por espacio (ej: A B C): ").split()
        nuevos = 0
        for vertice in entrada:
            if vertice not in vertices:
                vertices.append(vertice)
                lista_adyacencia[vertice] = []
                nuevos += 1
        if nuevos > 0:
            actualizar_matriz()
        else:
            print("No se agregaron vértices nuevos.")

    elif opcion == "2":
        origen = input("Ingrese el vértice de origen: ")
        destino = input("Ingrese el vértice de destino: ")
        if origen in vertices and destino in vertices:
            lista_adyacencia[origen].append(destino)
            i = vertices.index(origen)
            j = vertices.index(destino)
            matriz_adyacencia[i][j] = 1
        else:
            print("Uno o ambos vértices no existen.")

    elif opcion == "3":
        print("\nLista de adyacencia:")
        for vertice in lista_adyacencia:
            print(f"{vertice} -> {lista_adyacencia[vertice]}")

    elif opcion == "4":
        print("\nMatriz de adyacencia:")
        print("   " + "  ".join(vertices))
        for i, fila in enumerate(matriz_adyacencia):
            print(f"{vertices[i]}: {fila}")

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")
