#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands, obstacles):
        start = (0,0)
        obstacles_set = set([tuple(obstacle) for obstacle in obstacles])
        max_distance = 0
        # direction:down, right, up, left
        # turn left: +1
        # turn righe: +3
        dx = [0,1,0,-1]
        dy = [-1,0,1,0]
        direction = 2
        for command in commands:
            if command == -2:
                direction = (direction + 1) % 4
            elif command == -1:
                direction = (direction + 3) % 4
            else:
                for _ in range(command):
                    end = (start[0]+dx[direction], start[1]+dy[direction])
                    if end not in obstacles_set:
                        start = end
                        max_distance = max(max_distance, end[0]**2+end[1]**2)
        return max_distance


        

        
# @lc code=end

sol = Solution()
print(sol.robotSim([4,-1,3],[]))

