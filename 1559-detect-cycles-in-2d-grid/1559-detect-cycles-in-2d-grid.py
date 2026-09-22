class Solution:
    def containsCycle(self, grid):
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for sr in range(m):
            for sc in range(n):
                if visited[sr][sc]:
                    continue

                stack = [(sr, sc, -1, -1)]
                visited[sr][sc] = True

                while stack:
                    r, c, pr, pc = stack.pop()

                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc

                        if nr < 0 or nr >= m or nc < 0 or nc >= n:
                            continue

                        if grid[nr][nc] != grid[r][c]:
                            continue

                        if nr == pr and nc == pc:
                            continue

                        if visited[nr][nc]:
                            return True

                        visited[nr][nc] = True
                        stack.append((nr, nc, r, c))

        return False