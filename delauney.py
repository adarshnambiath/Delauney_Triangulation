import numpy as np
import matplotlib.pyplot as plt


class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = [tuple(p1), tuple(p2), tuple(p3)]

    def edges(self):
        p = self.points
        return [(p[0], p[1]), (p[1], p[2]), (p[2], p[0])]

    def contains_vertex(self, v):
        return tuple(v) in self.points


def circumcircle_contains(triangle, point):

    ax, ay = triangle.points[0]
    bx, by = triangle.points[1]
    cx, cy = triangle.points[2]
    dx, dy = point

    A = ax - dx
    B = ay - dy
    C = (ax - dx)**2 + (ay - dy)**2

    D = bx - dx
    E = by - dy
    F = (bx - dx)**2 + (by - dy)**2

    G = cx - dx
    H = cy - dy
    I = (cx - dx)**2 + (cy - dy)**2

    det = (
        A * (E * I - F * H)
        - B * (D * I - F * G)
        + C * (D * H - E * G)
    )

    # The determinant sign depends on the triangle winding order.
    orient = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

    if orient > 0:
        return det > 0
    return det < 0


def bowyer_watson(points):

    points = [tuple(p) for p in points]

    min_x = min(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)

    dx = max_x - min_x
    dy = max_y - min_y
    delta = max(dx, dy) * 10

    p1 = (min_x - delta, min_y - delta)
    p2 = (min_x + dx/2, max_y + delta)
    p3 = (max_x + delta, min_y - delta)

    triangulation = [Triangle(p1, p2, p3)]

    for point in points:

        bad_triangles = []

        for triangle in triangulation:
            if circumcircle_contains(triangle, point):
                bad_triangles.append(triangle)

        polygon = []

        for triangle in bad_triangles:
            for edge in triangle.edges():

                if edge in polygon:
                    polygon.remove(edge)
                elif (edge[1], edge[0]) in polygon:
                    polygon.remove((edge[1], edge[0]))
                else:
                    polygon.append(edge)

        for triangle in bad_triangles:
            triangulation.remove(triangle)

        for edge in polygon:
            triangulation.append(Triangle(edge[0], edge[1], point))

    triangulation = [
        t for t in triangulation
        if not (
            t.contains_vertex(p1)
            or t.contains_vertex(p2)
            or t.contains_vertex(p3)
        )
    ]

    return triangulation


def plot_triangulation(points, triangles):

    plt.figure()

    for tri in triangles:
        x = [p[0] for p in tri.points] + [tri.points[0][0]]
        y = [p[1] for p in tri.points] + [tri.points[0][1]]
        plt.plot(x, y)

    px = [p[0] for p in points]
    py = [p[1] for p in points]

    plt.scatter(px, py, color="red")

    plt.gca().set_aspect("equal")
    plt.title("Bowyer-Watson Delaunay Triangulation")
    plt.show()


if __name__ == "__main__":

    points = np.random.rand(20, 2) * 100

    triangles = bowyer_watson(points)

    print("Triangles created:", len(triangles))

    plot_triangulation(points, triangles)