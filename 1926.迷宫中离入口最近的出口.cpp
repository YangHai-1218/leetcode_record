/*
 * @lc app=leetcode.cn id=1926 lang=cpp
 *
 * [1926] 迷宫中离入口最近的出口
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int m = maze.size(), n = maze[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        visited[entrance[0]][entrance[1]] = true;
        return bfs(maze, visited, entrance[0], entrance[1], m, n);

    }

    int bfs(vector<vector<char>>& maze, vector<vector<bool>>& visited, int y, int x, int m, int n){
        queue<tuple<int, int, int>> que;
        que.emplace(x, y, 0);
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!que.empty()){
            auto [cx, cy, cd] = que.front();
            que.pop();
            for (int i = 0; i < 4; i++){
                int next_x = cx + directions[i].first;
                int next_y = cy + directions[i].second;
                if (next_x < 0 || next_x >= n || next_y < 0 || next_y >= m) continue;
                if (visited[next_y][next_x]) continue;
                if (maze[next_y][next_x]=='.'){
                    if (next_y == m-1 || next_x == n-1 || next_y == 0 || next_x == 0){
                        return cd+1;
                    }else{
                        visited[next_y][next_x] = true;
                        que.push({next_x, next_y, cd+1});
                    }
                }
            }
        }
        return -1;
    }
};
// @lc code=end

int main(){
    Solution solution;
    vector<vector<char>> maze = {{'.'},{'.'},{'.'}};
    vector<int> entrance = {2, 0};
    int ans = solution.nearestExit(maze, entrance);
    std::cout << ans << std::endl;
    return 0;
}

