from pprint import pprint

E = None


def checkHasFilled(two_dimentional_array) -> bool:
    for row in two_dimentional_array:
        if E in row:
            return False
    return True


arr = [
    [E, E, E, 2, 6, E, 7, E, 1],
    [6, 8, E, E, 7, E, E, 9, E],
    [1, 9, E, E, E, 4, 5, E, E],
    [8, 2, E, 1, E, E, E, 4, E],
    [E, E, 4, 6, E, 2, 9, E, E],
    [E, 5, E, E, E, 3, E, 2, 8],
    [E, E, 9, 3, E, E, E, 7, 4],
    [E, 4, E, E, 5, E, E, 3, 6],
    [7, E, 3, E, 1, 8, E, E, E],
]

groups = [[set() for _ in range(3)] for _ in range(3)]
for yi in range(3):
    for xi in range(3):
        for ri in range(yi * 3, yi * 3 + 3):
            for ci in range(xi * 3, xi * 3 + 3):
                if not arr[ri][ci]:
                    continue
                groups[yi][xi].add(arr[ri][ci])
U = set(range(1, 10))


for cnt_i in range(100):
    if checkHasFilled(arr):
        break
    used = [
        [set(groups[ri // 3][ci // 3]) for ci in range(9)] for ri in range(9)
    ]
    for yi in range(9):
        for xi in range(9):
            for cell in arr[yi]:
                used[yi][xi].add(cell)
            for row in arr:
                pass
                used[yi][xi].add(row[xi])
            used[yi][xi].add(arr[yi][xi])

    for yi in range(9):
        for xi in range(9):
            if arr[yi][xi] is not E:
                continue
            st = U.difference(used[yi][xi])
            if len(st) == 1:
                cell = st.pop()
                arr[yi][xi] = cell
                gyi = yi // 3
                gxi = xi // 3
                for ri in range(gyi * 3, gyi * 3 + 3):
                    for ci in range(gxi * 3, gxi * 3 + 3):
                        used[ri][ci].add(cell)
pprint(arr)
