from gra import * 
import imageio

name = open(".input", "r").read()

arr = imageio.imread("./samples/" + name, pilmode='RGB')
N = arr.shape[0]
M = arr.shape[1]

im = Image(arr, N, M)
print("N = " + str(N) + " M = " + str(M))
grad = calculate_gradient(im)
print("gradient calculated")
color = calculate_components(grad)
print("components calculated")

max_color = 0
max_color_count = 0

count = np.zeros((N * M + 1))
for i in range(0, N):
    for j in range(0, M):
        current_color = int(color[i][j])
        if current_color == -1:
            continue
        count[current_color] += 1
        if count[current_color] > max_color_count:
            max_color = current_color
            max_color_count = count[current_color]

for i in range(0, N):
    for j in range(0, M):
        if color[i][j] != max_color:
            drr = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if in_range(i + x, N) and in_range(j + y, M) and color[i + x][j + y] == max_color:
                        drr += 1
            if drr >= 3:
                color[i][j] = max_color

for i in range(0, N):
    for j in range(0, M):
        if color[i][j] != max_color:
            im.arr[i][j] = (0, 0, 0)

imageio.imwrite("./samples/modified_" + name, im.arr)


# now calculate rectangle

count = np.ones(M)

result_value = 0
result_y1 = 0
result_y2 = 0
result_x = 0
result_h = 0

for i in range(0, N):
    if i > 0:
        for j in range(0, M):
            if color[i][j] == max_color:
                count[j] += 1
            else:
                count[j] = 0
    stack = list()
    current_count = count
    for j in range(0, M):
        position = j
        while len(stack) > 0:
            if current_count[stack[len(stack) - 1]] < count[j]:
                break
            position = stack[len(stack) - 1]
            stack.pop()
        stack.append(position)
        current_count[position] = count[position]
        if result_value < (j - position + 1) * count[j]:
            result_value = (j - position + 1) * count[j];
            result_x = i
            result_y1 = position
            result_y2 = j
            result_h = count[position]

def is_inside(x, y):
    return x > result_x - result_h and x <= result_x and y >= result_y1 and y <= result_y2

for i in range(0, N):
    for j in range(0, M):
        if color[i][j] != max_color:
            continue
        if not is_inside(i, j):
            im.arr[i][j] = (0, 0, 0)

imageio.imwrite("samples/modified_recrangle_" + name, im.arr)
