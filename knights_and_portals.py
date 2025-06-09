from collections import deque

def shortest_path_with_teleport(grid):
    rows, cols = len(grid), len(grid[0])
    empty_cells = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

    def neighbors(r, c):
        for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                yield nr, nc

    dist = [[[float('inf')] * 2 for _ in range(cols)] for _ in range(rows)]
    dist[0][0][0] = 0
    queue = deque([(0, 0, 0)])

    while queue:
        r, c, used = queue.popleft()
        d = dist[r][c][used]

        if (r, c) == (rows-1, cols-1):
            return d

        for nr, nc in neighbors(r, c):
            if dist[nr][nc][used] > d + 1:
                dist[nr][nc][used] = d + 1
                queue.append((nr, nc, used))

        if used == 0:
            for tr, tc in empty_cells:
                if (tr, tc) != (r, c) and dist[tr][tc][1] > d + 1:
                    dist[tr][tc][1] = d + 1
                    queue.append((tr, tc, 1))

    return -1

def test_knights_and_portals():
    grid1 = [
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0]
    ]

    grid2 = [
        [0, 1],
        [1, 0]
    ]

    grid3 = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]

    print(shortest_path_with_teleport(grid1))
    print(shortest_path_with_teleport(grid2))
    print(shortest_path_with_teleport(grid3))

if __name__ == "__main__":
    test_knights_and_portals()
