class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        dirs = {
            1: [(0, 1), (0, -1)],
            2: [(1, 0), (-1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        visited = set()

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return True

            visited.add((r, c))

            for dr, dc in dirs[grid[r][c]]:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if (nr, nc) in visited:
                    continue

                # Next cell must connect back to current cell
                if (-dr, -dc) in dirs[grid[nr][nc]]:
                    if dfs(nr, nc):
                        return True

            return False

        return dfs(0, 0)