/*
 * @lc app=leetcode.cn id=1020 lang=cpp
 *
 * [1020] 飞地的数量
 */

#include <iostream>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int numEnclaves(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));

        for (int i=0; i<m;i++){
            if (grid[i][0]==1){
                visited[i][0] = true;
                dfs(grid, visited, 0, i, n, m);
            }
            if (grid[i][n-1]==1){
                visited[i][n-1] = true;
                dfs(grid, visited, n-1, i, n, m);
            }
        }
        for (int i=1; i<n-1;i++){
            if (grid[0][i]==1){
                visited[0][i] = true;
                dfs(grid, visited, i, 0, n, m);
            }
            if (grid[m-1][i]==1){
                visited[m-1][i] = true;
                dfs(grid, visited, i, m-1, n, m);
            }
        }
        
        int result = 0;
        for (int i=0;i<m;i++){
            for (int j=0;j<n;j++){
                if (grid[i][j] == 1 && visited[i][j]==false){
                    result ++;
                }
            }
        }
        return result;
    }

    void dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int x, int y, int n, int m){
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (int i = 0; i < 4; i++){
            int next_x = x + directions[i].first;
            int next_y = y + directions[i].second;
            if (next_x < 0 || next_x >= n || next_y < 0 || next_y >= m) continue;
            if (grid[next_y][next_x] == 1 && !visited[next_y][next_x]){
                visited[next_y][next_x] = true;
                dfs(grid, visited, next_x, next_y, n, m);
            }
        }
        return;
    }
};
// @lc code=end
int main(){
    Solution solution;
    vector<vector<int>> grid = {
        {0,0,1,1,1,0,1,1,1,0,1},
        {1,1,1,1,0,1,0,1,1,0,0},
        {0,1,0,1,1,0,0,0,0,1,0},
        {1,0,1,1,1,1,1,0,0,0,1},
        {0,0,1,0,1,1,0,0,1,0,0},
        {1,0,0,1,1,1,0,0,0,1,1},
        {0,1,0,1,1,0,0,0,1,0,0},
        {0,1,1,0,1,0,1,1,1,0,0},
        {1,1,0,1,1,1,0,0,0,0,0},
        {1,0,1,1,0,0,0,1,0,0,1}};
    solution.numEnclaves(grid);
    return 0;
}

