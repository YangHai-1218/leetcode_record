/*
 * @lc app=leetcode.cn id=130 lang=cpp
 *
 * [130] 被围绕的区域
 */

#include <iostream>
#include <vector>
using namespace std;

// @lc code=start

class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int m = board.size(), n = board[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        for (int i=0;i<m;i++){
            if (board[i][0] == 'O'){
                visited[i][0] = true;
                dfs(board, visited, 0, i, n, m);
            }
            if (board[i][n-1] == 'O'){
                visited[i][n-1] = true;
                dfs(board, visited, n-1, i, n, m);
            }
        }

        for (int i=1;i<n-1;i++){
            if (board[0][i] == 'O'){
                visited[0][i] = true;
                dfs(board, visited, i, 0, n, m);
            }
            if (board[m-1][i] == 'O'){
                visited[m-1][i] = true;
                dfs(board, visited, i, m-1, n, m);
            }
        }
    
        for (int y=0;y<m;y++){
            for (int x=0;x<n;x++){
                if(!visited[y][x] && board[y][x]=='O'){
                    board[y][x] = 'X';
                }
            }
        }

    }

    void dfs(vector<vector<char>>& board, vector<vector<bool>>& visited, int x, int y, int n, int m){
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (int i = 0; i < 4; i++){
            int next_x = x + directions[i].first;
            int next_y = y + directions[i].second;
            if (next_x < 0 || next_x >= n || next_y < 0 || next_y >= m) continue;
            if  (board[next_y][next_x] == 'O' && !visited[next_y][next_x]){
                visited[next_y][next_x] = true;
                dfs(board, visited, next_x, next_y, n, m);
            }
        }

    }
};
// @lc code=end

