# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:30:00 2023

@author: cesar
"""

# Implementación del algoritmo de Prim para encontrar el árbol de expansión mínimo

import heapq

def prim(graph, start):
    # Inicialización
    visited = set()
    queue = [(0, start)]
    mst_weight = 0
    mst_edges = []

    # Repetir hasta que todos los vértices estén conectados
    while queue:
        # Seleccionar el vértice con menor peso
        weight, vertex = heapq.heappop(queue)
        if vertex not in visited:
            # Agregar el vértice al conjunto de visitados
            visited.add(vertex)
            mst_weight += weight
            # Agregar la arista al árbol de expansión mínimo
            if vertex != start:
                mst_edges.append((start, vertex, weight))
            # Agregar las aristas adyacentes al vértice seleccionado a la cola de prioridad
            for neighbor, weight in graph[vertex]:
                if neighbor not in visited:
                    heapq.heappush(queue, (weight, neighbor))

    return mst_weight, mst_edges

# Ejemplo de uso
graph = {
    1: [(2, 2), (3, 3), (4, 1)],
    2: [(1, 2), (3, 4), (5, 3)],
    3: [(1, 3), (2, 4), (4, 5), (5, 1)],
    4: [(1, 1), (3, 5)],
    5: [(2, 3), (3, 1)]
}
start_vertex = 1

mst_weight, mst_edges = prim(graph, start_vertex)

print("El peso total del árbol de expansión mínimo es:", mst_weight)
print("Las aristas del árbol de expansión mínimo son:")
for edge in mst_edges:
    print(edge)