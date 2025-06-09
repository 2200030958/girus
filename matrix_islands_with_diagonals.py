def count_islands(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False]*cols for _ in range(rows)]

    def dfs(r, c):
        directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        stack = [(r, c)]
        while stack:
            x, y = stack.pop()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and matrix[nx][ny] == 1:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    count = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                visited[r][c] = True
                dfs(r, c)
                count += 1
    return count

def test_count_islands():
    matrix1 = [
        [1, 1, 0, 0],
        [0, 1, 0, 1],
        [1, 0, 0, 1],
        [0, 0, 1, 1]
    ]
    matrix2 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    matrix3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print(count_islands(matrix1))
    print(count_islands(matrix2))
    print(count_islands(matrix3))

if __name__ == "__main__":
    test_count_islands()
