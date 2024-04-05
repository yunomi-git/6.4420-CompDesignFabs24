import numpy as np

import copy



class VertexMap:
    # General mapping between vertex and y
    def __init__(self, tolerance=3):
        # Unrealistic for any physical tolerance to exceed 0.01 mm.
        self.vertex_map = {}
        self.tolerance = tolerance

    def set_vertex_value(self, vertex, value):
        vertex = np.round(vertex, self.tolerance)
        if vertex[0] not in self.vertex_map:
            self.vertex_map[vertex[0]] = {}
        if vertex[1] not in self.vertex_map[vertex[0]]:
            self.vertex_map[vertex[0]][vertex[1]] = {}
        if vertex[2] not in self.vertex_map:
            self.vertex_map[vertex[0]][vertex[1]][vertex[2]] = value

    def vertex_is_in_list(self, vertex):
        vertex = np.round(vertex, self.tolerance)
        if vertex[0] not in self.vertex_map:
            return False
        if vertex[1] not in self.vertex_map[vertex[0]]:
            return False
        if vertex[2] not in self.vertex_map[vertex[0]][vertex[1]]:
            return False
        return True

    def get_vertex_value(self, vertex):
        vertex = np.round(vertex, self.tolerance)
        if not self.vertex_is_in_list(vertex):
            return None
        return self.vertex_map[vertex[0]][vertex[1]][vertex[2]]

    def remove_vertex(self, vertex):
        vertex = np.round(vertex, self.tolerance)
        if self.vertex_is_in_list(vertex):
            del self.vertex_map[vertex[0]][vertex[1]][vertex[2]]
            if len(self.vertex_map[vertex[0]][vertex[1]]) == 0:
                del self.vertex_map[vertex[0]][vertex[1]]
            if len(self.vertex_map[vertex[0]]) == 0:
                del self.vertex_map[vertex[0]]




class EdgeDictionary(VertexMap):
    def __init__(self, edges, tolerance=3):
        super().__init__(tolerance)
        for edge in edges:
            self.add_edge(edge.start, edge.end)

    def add_edge(self, vertex_start, vertex_end):
        if not self.vertex_is_in_list(vertex_start):
            self.set_vertex_value(vertex_start, [])
        self.get_vertex_value(vertex_start).append(np.round(vertex_end, self.tolerance))

    def get_connected_vertices(self, vertex, exclude_vertex=None):
        if not self.vertex_is_in_list(vertex):
            return []
        connected_vertices = self.get_vertex_value(vertex)
        return_vertices = []
        for connection in connected_vertices:
            if exclude_vertex is None or not np.equal(connection, exclude_vertex).all():
                return_vertices.append(connection)
        return return_vertices

    def is_not_empty(self):
        return len(self.vertex_map) != 0

    def get_first_vertex_key(self):
        x = list(self.vertex_map.keys())[0]
        y = list(self.vertex_map[x].keys())[0]
        z = list(self.vertex_map[x][y].keys())[0]
        return np.array([x, y, z])


class VertexPath(EdgeDictionary):
    def __init__(self, start_vertex, tolerance=3):
        super().__init__([], tolerance)
        self.first_vertex = start_vertex
        self.last_vertex = start_vertex

    def add_vertex(self, vertex):
        vertex = np.round(vertex, self.tolerance)
        self.add_edge(self.last_vertex, vertex)
        self.last_vertex = vertex

    def construct_path_from_vertex(self, vertex):
        path = []
        path.append(vertex)
        next_vertices = self.get_connected_vertices(vertex)
        while len(next_vertices) > 0:
            last_vertex = vertex
            vertex = next_vertices[0]
            path.append(vertex)
            next_vertices = self.get_connected_vertices(vertex, exclude_vertex=last_vertex)
        return path

    def append_in_front(self, vertex_path):
        self.vertex_map.update(copy.deepcopy(vertex_path.vertex_map))
        self.add_edge(vertex_path.last_vertex, self.first_vertex)

def copy_path(path: VertexPath):
    copy_path = VertexPath(None)
    copy_path.vertex_map = copy.deepcopy(path.vertex_map)
    copy_path.last_vertex = path.last_vertex
    copy_path.first_vertex = path.first_vertex
    return copy_path
# class VertexPath(VertexMap):
#     def __init__(self, tolerance=3):
#         super().__init__(tolerance)
#         self.vertex_list = []
#         self.num_vertices = 0
#
#     def add_vertex(self, vertex):
#         vertex = np.round(vertex, self.tolerance)
#         self.set_vertex_value(vertex, self.num_vertices)
#         self.vertex_list.append(vertex)
#         self.num_vertices += 1
#
#     def get_index_of_vertex(self, vertex):
#         return self.get_vertex_value(vertex)
#
#     def vertex_is_in_path(self, vertex):
#         return self.vertex_is_in_list(vertex)
#
#     def construct_path_from_vertex(self, vertex):
#         index = self.get_index_of_vertex(vertex)
#         return self.vertex_list[index:]
#
#     def append_in_front(self, vertex_path):
#         num_new_vertices = vertex_path.num_vertices
#
#         for vertex in self.vertex_list:
#             vertex_path.set_vertex_value
#         self.vertex_map.update(vertex_path.vertex_map)
#         self.vertex_list = vertex_path.vertex_list + self.vertex_list


