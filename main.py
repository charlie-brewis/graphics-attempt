from graphics import *

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
    [CENT - QUART,  CENT - QUART, 0],    # TLF
    [CENT - QUART, CENT - QUART, QUART], # TLB
    [CENT + QUART, CENT - QUART, 0],     # TRF
    [CENT + QUART, CENT - QUART, QUART], # TRB
    [CENT + QUART, CENT + QUART, 0],     # BRF
    [CENT + QUART, CENT + QUART, QUART], # BRB
    [CENT - QUART, CENT + QUART, 0],     # BLF
    [CENT - QUART, CENT + QUART, QUART], # BLB
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


def project_value(val: float, z: float, focal_length: float) -> float:
    return (focal_length * val) / (focal_length + z)

def project_3d_vertex(vertex: (float, float, float), focal_length: float) -> (float, float):
    x, y, z = vertex
    x_projected = project_value(x, z, focal_length)
    y_projected = project_value(y, z, focal_length)
    return (x_projected, y_projected)

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

def undraw_edges(edges: list[Line]) -> None:
    for edge in edges:
        edge.undraw()

def move_3d_vertex(orginal_vertex: list[float], target_vertex: list[float]) -> list[float]:
    dx = target_vertex[0] - orginal_vertex[0]
    dy = target_vertex[1] - orginal_vertex[1]
    dz = target_vertex[2] - orginal_vertex[2]
    return [orginal_vertex[0] + dx, orginal_vertex[1] + dy, orginal_vertex[2] + dz]

def move_vertex_table(original_vertex_table: list[list[float]], target_vertex_table: list[list[float]]) -> list[list[float]]:
    moved_vertex_table = []
    for i in range(len(original_vertex_table)):
        original_vertex = original_vertex_table[i]
        target_vertex = target_vertex_table[i]
        moved_vertex = move_3d_vertex(original_vertex, target_vertex)
        moved_vertex_table.append(moved_vertex)
    return moved_vertex_table

def main() -> None:
    win = GraphWin("3D cube", 200, 200)
    # last_cube_vertexes = project_vertex_table(cube_vertexes, focal_length)
    # projected_cube_vertexes = project_vertex_table(cube_vertexes, focal_length)
    # for focal_length in range(100):
    #     projected_cube_vertexes = move_vertex_table(last_cube_vertexes, projected_cube_vertexes)
    #     edges = draw_obj_from_verticies(win, projected_cube_vertexes, cube_edges)   
    #     last_cube_vertexes = projected_cube_vertexes
    last_cube_vertexes = cube_vertexes
    for focal_length in range(100):
        projected_cube_vertexes = project_vertex_table(last_cube_vertexes, focal_length)
        target_vertexes = move_vertex_table()
        edges = draw_obj_from_verticies(win, projected_cube_vertexes, cube_edges)
        undraw_edges(edges)


    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()