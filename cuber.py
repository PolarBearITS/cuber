size = 3
cube = [[[i + size*j + (size**2)*k + 1 for i in range(size)] for j in range(size)] for k in range(size)]
def display(c):
    for i in range(size):
        print(c[i])
def rotate(c, d):
    if d == 'c':
        c = [[c[j][size - 1 - i] for j in range(size)] for i in range(size)]
    elif d == 'cc':
        c = [[c[size - 1 - j][i] for j in range(size)] for i in range(size)]
    display(c)
display(cube)
print()
rotate(cube, 'c')
