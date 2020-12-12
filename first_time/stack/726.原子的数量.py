#
# @lc app=leetcode.cn id=726 lang=python3
#
# [726] 原子的数量
#

# @lc code=start
class Solution:
    def countOfAtoms(self, formula):
        dic = dict()
        i, flag = 0, 0
        stack = []
        while i < len(formula):
            char = formula[i]
            if char.isupper():
                atom, multi_atom = char, 0
                i += 1
                while i < len(formula) and formula[i].islower():
                    atom += formula[i]
                    i += 1
                while i < len(formula) and formula[i].isdigit():
                    multi_atom = 10 * multi_atom + int(formula[i])
                    i += 1
                multi_atom = 1 if multi_atom == 0 else multi_atom
                stack.append([atom, multi_atom, flag])
            elif char == '(':
                i += 1
                flag += 1
            elif char == ')':
                brac_multi = 0
                i += 1
                while i < len(formula) and formula[i].isdigit():
                    brac_multi = brac_multi * 10 + int(formula[i])
                    i += 1
                brac_multi = 1 if brac_multi == 0 else brac_multi
                end = len(stack)
                while stack and stack[end-1][2] == flag:
                    stack[end-1][1] *= brac_multi
                    stack[end-1][2] -= 1
                    end -= 1
                flag -= 1
            else:
                pass
        for atom in stack:
            dic[atom[0]] = dic.get(atom[0],0) + atom[1]
        dic = sorted(dic.items(), key=lambda obj: obj[0])
        ans = ''
        for atom, multi in dic:
            multi = '' if multi== 1 else str(multi)
            ans += atom + multi
        return ans

# @lc code=end

