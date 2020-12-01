




class Solution:
    def rotate_martix(self, martix):
        if not martix:
            return []
        result = []
        num_row = len(martix)
        for i in range(num_row):
            col = [martix[j][i] for j in range(num_row-1, -1, -1)]
            result.append(col)
        return result
    def rotate_martix_inplace(self, martix):
        if not martix:
            return []

class Solution2:
    def carry_people(self, people, limit):
        people.sort()
        num_ = len(people)
        start_index = 0
        end_index = num_ - 1
        result = 0
        # people.insert(num_, 0)
        while start_index < end_index:
            current_weigth = people[start_index]
            min_weight = people[end_index]
            if current_weigth + min_weight <= limit:
                result += 1
                start_index += 1
                end_index -= 1
            else:
                result += 1
                start_index += 1
        return result

if __name__ =='__main__':
    # martix = [[1,2],[3,4]]
    # sol = Solution()
    # print(sol.rotate_martix(martix))
    people = [1,2,3,4]
    limit = 5
    sol = Solution2()
    print(sol.carry_people(people, limit))