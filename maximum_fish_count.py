def dfs(row, col, grid, vis, n, m):
    if row < 0 or col < 0 or row >= n or col >= m or vis[row][col] or grid[row][col] == 0:
        return 0
        
    vis[row][col] = True
    fish_count = grid[row][col]
    fish_count += dfs(row + 1, col, grid, vis, n, m)
    fish_count += dfs(row - 1, col, grid, vis, n, m)
    fish_count += dfs(row, col + 1, grid, vis, n, m)
    fish_count += dfs(row, col - 1, grid, vis, n, m)
    return fish_count

class solution:
    def maxFish(self, grid, n, m):
        vis = [[False] * m for _ in range(n)]
        max_fish_count = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] > 0 and not vis[row][col]:
                    max_fish_count = max(max_fish_count, dfs(row, col, grid, vis, n, m))
        return max_fish_count