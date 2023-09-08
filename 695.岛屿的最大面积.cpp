/*
 * @lc app=leetcode.cn id=695 lang=cpp
 *
 * [695] 岛屿的最大面积
 */

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// @lc code=start
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<bool>> visited = vector<vector<bool>>(m, vector<bool>(n, false));
        int res = 0;
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (grid[i][j] == 1 && !visited[i][j]){
                    // int area = 1;
                    visited[i][j]=true;
                    // dfs(grid, visited, area, i, j, m, n);
                    int area = bfs(grid, visited, i, j, m, n);
                    res = max(area, res);
                }
            }
        }
        return res;
    }

    void dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int& area, int y, int x, int m, int n){
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (int i = 0;i < 4; i++){
            int next_x = x + directions[i].first;
            int next_y = y + directions[i].second;
            if (next_x < 0 || next_x >= n || next_y < 0 || next_y >= m) continue;
            if (!visited[next_y][next_x] && grid[next_y][next_x] == 1){
                visited[next_y][next_x] = true;
                area ++;
                dfs(grid, visited, area, next_y, next_x, m, n);
            }
        }
    }

    int bfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int y, int x, int m, int n){
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        queue<pair<int, int>> que;
        que.push({x, y});
        int area = 1;
        while (!que.empty()){
            pair<int, int> current_point = que.front();
            que.pop();
            for (int i = 0; i < 4; i++){
                int next_x = current_point.first + directions[i].first;
                int next_y = current_point.second + directions[i].second;
                if (next_x < 0 || next_x >= n || next_y < 0 || next_y >= m) continue;
                if (!visited[next_y][next_x] && grid[next_y][next_x] == 1){
                    visited[next_y][next_x] = true;
                    que.push({next_x, next_y});
                    area ++;
                }
            }
        }
        return area;
    }
};
// @lc code=end


