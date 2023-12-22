from graphics import *
from math import sin, cos

WIN_SIZE = 200
CENT = WIN_SIZE // 2
QUART = CENT // 2



square_vertexes = [
    [CENT - QUART,  CENT - QUART], # TL
    [CENT + QUART, CENT - QUART], # TR
    [CENT + QUART, CENT + QUART], # BR
    [CENT - QUART, CENT + QUART], # BL
]


square_edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0]
]

cube_vertexes = [
    [CENT - QUART, CENT - QUART, 0],    # TLF
    [CENT - QUART, CENT - QUART, CENT], # TLB
    [CENT + QUART, CENT - QUART, 0],    # TRF
    [CENT + QUART, CENT - QUART, CENT], # TRB
    [CENT + QUART, CENT + QUART, 0],    # BRF
    [CENT + QUART, CENT + QUART, CENT], # BRB
    [CENT - QUART, CENT + QUART, 0],    # BLF
    [CENT - QUART, CENT + QUART, CENT], # BLB
]

cube_edges = [
    [0, 1],
    [0, 2],
    [0, 6],
    [1, 3],
    [1, 7],
    [2, 3],
    [2, 4],
    [3, 5],
    [4, 5],
    [4, 6],
    [5, 7],
    [6, 7]
]

pyramid_vertexes = [
    [CENT, CENT - QUART, QUART],        # T
    [CENT + QUART, CENT + QUART, 0],    # FR
    [CENT + QUART, CENT + QUART, CENT], # BR
    [CENT - QUART, CENT + QUART, 0],    # FL
    [CENT - QUART, CENT + QUART, CENT]  # BL
]

pyramid_edges = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [1, 2],
    [1, 3],
    [2, 4],
    [3, 4]
]


def project_value(val: float, z: float, focal_length: float) -> float:
    return (focal_length * val) / (focal_length + z)

def project_3d_vertex(vertex: [float, float, float], focal_length: float) -> [float, float]:
    x, y, z = vertex
    x_projected = project_value(x, z, focal_length)
    y_projected = project_value(y, z, focal_length)
    return [x_projected, y_projected]

def project_vertex_table(vertex_table: list[float], focal_length: float) -> list[float]:
    projected_vertex_table = []
    for vertex in vertex_table:
        projected_vertex = project_3d_vertex(vertex, focal_length)
        projected_vertex_table.append(projected_vertex)
    return projected_vertex_table

def draw_edge(win: GraphWin, v1: list[float], v2: list[float]) -> Line:
    line = Line(Point(*v1), Point(*v2))
    line.draw(win)
    return line

def draw_obj_from_verticies(win: GraphWin, vertex_table: list[list[float]], edge_table: list[list[int]]) -> None:
    obj = []
    for edge in edge_table:
        v1 = vertex_table[edge[0]]
        v2 = vertex_table[edge[1]]
        obj.append(draw_edge(win, v1, v2))
    return obj

def undraw_edges(edges: list[Line]) -> None:
    for edge in edges:
        edge.undraw()

def rotate_vertex(vertex: list[float], theta: float, axis: str) -> list[float]:
    excluded_index = 'xyz'.index(axis)
    excluded_value = vertex.pop(excluded_index)
    # A = [y, z] * B = [[cos(theta), -sin(theta)]
    #                  [sin(theta), cos(theta)]]
    # A is 1x2, B is 2x2
    # METHOD:
    # A[row0] * B[col0] -> ycos(theta) + zsin(theta)  --> Result = [ycos(theta) + zsin(theta), ]
    # A[row1] * B[col1] -> -ysin(theta) + zcos(theta) --> Result = [ycos(theta) + zsin(theta), -ysin(theta) + zcos(theta)]
    #! List index 1 out of range
    rotated_vertex = [vertex[0]*cos(theta) + vertex[1]*sin(theta), -vertex[0]*sin(theta) + vertex[1]*cos(theta)]
    rotated_vertex.insert(excluded_index, excluded_value)
    return rotated_vertex


def rotate_vertex_table(vertex_table: list[list[float]], theta: float, axis: str) -> list[list[float]]:
    new_vertex_table = []
    for vertex in vertex_table:
        rotated_vertex = rotate_vertex(vertex, theta, axis)
        new_vertex_table.append(rotated_vertex)
    return new_vertex_table

def main() -> None:
    win = GraphWin("3D cube", 200, 200)
    # focal_length = 2 * CENT
    # # original_vetexes = pyramid_vertexes
    # original_edges = pyramid_edges
    # projected_cube_vertexes = project_vertex_table(original_vetexes, focal_length)
    # draw_obj_from_verticies(win, projected_cube_vertexes, original_edges)

    #* focal length display - to move: render, undrender, genrate next value, repeat
    # last_cube_vertexes = cube_vertexes
    # for focal_length in range(1, 300):
    #     projected_cube_vertexes = project_vertex_table(last_cube_vertexes, focal_length)
    #     edges = draw_obj_from_verticies(win, projected_cube_vertexes, cube_edges)
    #     undraw_edges(edges)

    #* Rotation
    focal_length = 2 * CENT
    axis = 'y'
    theta = 0.01
    vertexes = cube_vertexes
    while True:
        projected_vertexes = project_vertex_table(vertexes, focal_length) 
        edges = draw_obj_from_verticies(win, projected_vertexes, cube_edges)
        vertexes = rotate_vertex_table(vertexes, theta, axis)
        undraw_edges(edges)
        







    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()