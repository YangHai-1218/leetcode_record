/*
 * @lc app=leetcode.cn id=417 lang=cpp
 *
 * [417] 太平洋大西洋水流问题
 */

#include <vector>
#include <iostream>
#include <queue>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        vector<vector<bool>> visited_by_pacific(m, vector<bool>(n, false));
        vector<vector<bool>> visited_by_atlantic(m, vector<bool>(n, false));
        
        for (int i=0; i<n;i++){
            visited_by_pacific[0][i] = true;
            // dfs(heights, visited_by_pacific, i, 0, n, m);
            bfs(heights, visited_by_pacific, i, 0, n, m);
        }
        for (int i=1; i<m;i++){
            visited_by_pacific[i][0] = true;
            // dfs(heights, visited_by_pacific, 0, i, n, m);
            bfs(heights, visited_by_pacific, 0, i, n, m);
        }

        for (int i=0; i<n;i++){
            visited_by_atlantic[m-1][i] = true;
            // dfs(heights, visited_by_atlantic, i, m-1, n, m);
            bfs(heights, visited_by_atlantic, i, m-1, n, m);
        }
        for (int i=0; i<m-1;i++){
            visited_by_atlantic[i][n-1] = true;
            // dfs(heights, visited_by_atlantic, n-1, i, n, m);
            bfs(heights, visited_by_atlantic, n-1, i, n, m);
        }

        vector<vector<int>> result;
        for (int y=0; y<m; y++){
            for (int x=0; x<n; x++){
                if (visited_by_atlantic[y][x] && visited_by_pacific[y][x]){
                    result.push_back({y, x});
                }
            }
        }
        return result;

    }

    void dfs(vector<vector<int>>& heights, vector<vector<bool>>& visited, int x, int y, int n, int m){
        for (int i=0; i<4; i++){
            int next_x = x + directions[i].first;
            int next_y = y + directions[i].second;
            if (next_x < 0 || next_x >= n || next_y < 0 || next_y >= m) continue;;
            if (!visited[next_y][next_x] && heights[next_y][next_x] >= heights[y][x]){
                visited[next_y][next_x] = true;
                dfs(heights, visited, next_x, next_y, n, m);
            }
        }
    }

    void bfs(vector<vector<int>>& heights, vector<vector<bool>>& visited, int x, int y, int n, int m){
        queue<pair<int, int>> que;
        que.emplace(x, y);
        while (!que.empty()){
            auto [current_x, current_y] = que.front();
            que.pop();
            for (int i=0; i<4; i++){
                int next_x = current_x + directions[i].first;
                int next_y = current_y + directions[i].second;
                if (next_x < 0 || next_x >= n || next_y < 0 || next_y >= m) continue;
                if (!visited[next_y][next_x] && heights[next_y][next_x] >= heights[current_y][current_x]){
                    que.emplace(next_x, next_y);
                    visited[next_y][next_x] = true;
                }
            }
        }
        
    }
};
// @lc code=end

