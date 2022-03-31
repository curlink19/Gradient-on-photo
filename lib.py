from classes import *
import numpy as np
import math as math


def in_range(x, N):
    return (x >= 0) and (x < N)

def calculate_gradient(im: Image):
    grad = np.zeros((im.N, im.M, 3, 2))
    for x in range(0, im.N):
        if x % 10 == 0:
            print(x)
        for y in range(0, im.M):
            for proj in range(0, 3):
                for coor in range(0, 2):
                        value = 0
                        on_point = im.arr[x][y][proj]
                        for offset in range(-1 * LOCAL_SIZE + 1, LOCAL_SIZE):
                            if offset == 0:
                                continue
                            current = 0
                            if coor == 0:
                                if (in_range(x + offset, im.N)):
                                    current = im.arr[x + offset][y][proj]
                            else:
                                if (in_range(y + offset, im.M)):
                                    current = im.arr[x][y + offset][proj]
                            if current < BORDER_VALUE:
                                value += current / offset
                        grad[x][y][proj][coor] = value / (2 * (LOCAL_SIZE - 1))
    return grad

def dist(a, b):
    value = 0
    for i in range(0, 3):
        for j in range(0, 2):
            value += (a[i][j] - b[i][j]) ** 2.0
    return math.sqrt(value)

def length(a):
    value = 0
    for i in range(0, 3):
        for j in range(0, 2):
            value += a[i][j] ** 2.0
    return math.sqrt(value)
