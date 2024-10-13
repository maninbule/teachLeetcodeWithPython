'''
https://leetcode.cn/problems/max-area-of-island/description/
'''
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vistied = [[False] * m for i in range(n)]  # nxm大小的二维数组
        maxArea = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vistied[i][j]:
                    vistied[i][j] = True
                    self.curArea = 1
                    self.dfs(grid, i, j, vistied)
                    maxArea = max(maxArea,self.curArea)
        return maxArea

    def dfs(self, grid, x, y, vistied):
        n = len(grid)
        m = len(grid[0])
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            # 计算出来的下一个坐标，越界了，就跳过
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if grid[nx][ny] == 0:
                continue
            if vistied[nx][ny] == True:
                continue
            self.curArea += 1
            vistied[nx][ny] = True
            self.dfs(grid, nx, ny, vistied)