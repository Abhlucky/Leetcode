class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Directions:
        # 0 = up, 1 = right, 2 = down, 3 = left
        directions = [
            (-1, 0),  # up
            (0, 1),   # right
            (1, 0),   # down
            (0, -1)   # left
        ]

        # Which directions each street connects to
        roads = {
            1: {1, 3},  # left <-> right
            2: {0, 2},  # up <-> down
            3: {2, 3},  # left <-> down
            4: {1, 2},  # right <-> down
            5: {0, 3},  # left <-> up
            6: {0, 1}   # right <-> up
        }

        visited = [[False] * n for _ in range(m)]

        stack = [(0, 0)]
        visited[0][0] = True

        while stack:
            r, c = stack.pop()

            if r == m - 1 and c == n - 1:
                return True

            current_road = grid[r][c]

            for d in roads[current_road]:
                dr, dc = directions[d]

                nr = r + dr
                nc = c + dc

                # Check boundaries
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Opposite direction
                opposite = (d + 2) % 4

                # The next street must connect back to current street
                if opposite not in roads[grid[nr][nc]]:
                    continue

                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    stack.append((nr, nc))

        return False