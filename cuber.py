size = 3
#i + size*j + (size**2)*k + 1
cube = [[[i + size*j + (size**2)*k + 1 for i in range(size)] for j in range(size)] for k in range(size)]
def display(c):
    U = c[0]
    D = c[2]
    L = [[i[0] for i in j] for j in c]
    R = [[i[2] for i in j] for j in c]
    B = [i[0][::-1] for i in c]
    F = [i[2] for i in c]
    for i in U:
        print(' '*8, i)
    for i in range(size):
        for j in [L, F, R, B]:
            print(j[i], end = '')
        print()
    for i in D:
        print(' '*8, i)
def rotate(c, d):
    if d == 'c':
        c = [[c[j][size - 1 - i] for j in range(size)] for i in range(size)]
    elif d == 'cc':
        c = [[c[size - 1 - j][i] for j in range(size)] for i in range(size)]
    display(c)
display(cube)
print()
#rotate(cube[0], 'c')
