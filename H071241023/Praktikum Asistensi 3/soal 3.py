N = int(input('N = '))
M = int(input('M = '))

for i in range(N):
    if i % 2 == 0:
        for a in range(M):
            print(f'MOVE to ({i}, {a})')
    else:
        for b in range(M - 1, -1, -1):
            print(f'MOVE to ({i}, {b})')
