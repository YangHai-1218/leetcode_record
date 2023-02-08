#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start

# stack version
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         s_formulated, t_formulated = [], []
#         for c in s:
#             if c == '#':
#                 if len(s_formulated) > 0:
#                     s_formulated.pop(-1)
#             else:
#                 s_formulated.append(c)
#         s_formulated = ''.join(s_formulated)

#         for c in t:
#             if c == '#':
#                 if len(t_formulated) > 0:
#                     t_formulated.pop(-1)
#             else:
#                 t_formulated.append(c)
#         t_formulated = ''.join(t_formulated)
#         print(s_formulated, t_formulated)
#         return s_formulated == t_formulated


# two-pointer version
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        pointer_s, pointer_t = len(s)-1, len(t)-1
        skip_s, skip_t = 0, 0
        while pointer_s >= 0 or pointer_t >= 0:
            while pointer_s >= 0:
                if s[pointer_s] == '#':
                    skip_s += 1
                    pointer_s -= 1
                else:
                    if skip_s > 0:
                        skip_s -= 1
                        pointer_s -= 1
                    else:
                        break
            while pointer_t >= 0:
                if t[pointer_t] == '#':
                    skip_t += 1
                    pointer_t -= 1
                else:
                    if skip_t > 0:
                        skip_t -= 1
                        pointer_t -= 1
                    else:
                        break
            if pointer_t >= 0 and pointer_s >= 0:
                if s[pointer_s] != t[pointer_t]:
                    return False
            elif pointer_s >=0 or pointer_t >= 0:
                return False
            pointer_s -= 1
            pointer_t -= 1
        return True    
        


# @lc code=end

