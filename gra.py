from lib import *
import queue

def calculate_components(grad):
    color = np.zeros((grad.shape[0], grad.shape[1]))
    current_color = 0
    for x in range(0, color.shape[0]):
        for y in range(0, color.shape[1]):
            if color[x][y] == 0:
                current_color += 1
                que = queue.Queue()
                que.put(Point(x, y))
                color[x][y] = current_color
                while not que.empty():
                    vert = que.get()
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if i == 0 and j == 0:
                                continue
                            current = Point(vert.x + i, vert.y + j)
                            if (not in_range(current.x, color.shape[0])) or (not in_range(current.y, color.shape[1])):
                                continue
                            if color[current.x][current.y] != 0:
                                continue
                            if dist(grad[x][y], grad[current.x][current.y]) >= EPS:
                                continue
                            color[current.x][current.y] = current_color
                            que.put(current)
            if length(grad[x][y]) <= MIN_LENGTH:
                color[x][y] = -1
    return color
