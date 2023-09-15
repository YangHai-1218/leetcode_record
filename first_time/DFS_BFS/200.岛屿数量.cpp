/*
 * @lc app=leetcode.cn id=200 lang=cpp
 *
 * [200] 岛屿数量
 */

// @lc code=start

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<bool>> visited = vector<vector<bool>>(m, vector<bool>(n, false));
        int result = 0;
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (grid[i][j] == '1' && !visited[i][j]){
                    // bfs(grid, visited, j, i, m, n);
                    visited[i][j] = true;
                    dfs(grid, visited, j, i, m, n);
                    result ++;
                }
            }
        }
        return result;
    }

    void bfs(vector<vector<char>>& grid, vector<vector<bool>>& visited, int x, int y, int m, int n){
        queue<pair<int, int>> que;
        que.push({x, y});
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!que.empty()){
            pair<int, int> current_point = que.front();
            que.pop();
            for (int i = 0; i < 4; i++){
                int x = current_point.first + directions[i].first;
                int y = current_point.second + directions[i].second;
                if (y < 0 || y > m-1 || x < 0 || x > n-1){
                    continue;
                }
                if (!visited[y][x] && grid[y][x] =='1'){
                    que.push({x, y});
                    visited[y][x] = true;
                }
            }
        }
    }

    void dfs(vector<vector<char>>& grid, vector<vector<bool>>& visited, int x, int y, int m, int n){
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (int i = 0; i < 4; i++){
            int next_x = x + directions[i].first;
            int next_y = y + directions[i].second;
            if (next_x < 0 || next_x >= n || next_y < 0 || next_y >= m){
                continue;
            }
            if (!visited[next_y][next_x] && grid[next_y][next_x] == '1'){
                visited[next_y][next_x] = true;
                dfs(grid, visited, next_x, next_y, m, n);
            }
        }
    }
    
};
// @lc code=end

