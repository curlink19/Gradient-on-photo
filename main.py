from gra import * 
import imageio


arr = imageio.imread('images.jpeg', pilmode='RGB')
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
            im.arr[i][j] = (0, 0, 0)

imageio.imwrite('images_.jpeg', im.arr)

# some debug info
for i in range(0, N):
    for j in range(0, M):
        print(int(length(grad[i][j])), end=' ')
    print('')

for i in range(0, N):
    for j in range(0, M):
        print(int(color[i][j]), end=' ')
    print('')
