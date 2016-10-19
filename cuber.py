cube = [
    [
        ['w', 'g', 'o'],
        ['w', 'g'],
        ['w', 'o', 'b']
    ],
    [
        ['w', 'g'],
        ['w'],
        ['w', 'b']
    ],
    [
        ['w', 'r', 'g'],
        ['w', 'r'],
        ['w', 'b', 'r']
    ]
]
def display(c):
    for i in range(3):
        print(c[i])
def rotate(c, d):
    if d == 0:
        c = [[c[j][2-i] for j in range(3)] for i in range(3)]
    elif d == 1:
        c = [[c[2-j][i] for j in range(3)] for i in range(3)]
    display(c)
display(cube)
print()
rotate(cube, 0)
