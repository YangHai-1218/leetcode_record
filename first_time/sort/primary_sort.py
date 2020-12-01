

class SelectionSort:
    def __call__(self, nums):
        len_nums = len(nums)
        for i in range(len_nums):
            min_num, min_num_index = float("inf"), i
            for j in range(i, len_nums):
                if nums[j] < min_num:
                    min_num, min_num_index = nums[j],j
            nums[i], nums[min_num_index] = nums[min_num_index], nums[i]
        return nums

class InsertSort:
    def __call__(self, nums):
        len_nums = len(nums)
        for i in range(len_nums):
            val = nums[i]
            j = i -1
            while j>=0 and nums[j]>val:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = val
        return nums
class BubbleSort:
    def __call__(self, nums):
        len_nums = len(nums)
        for _ in range(len_nums):
            for j in range(len_nums-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums


if __name__ == '__main__':
    nums = [1,3,2,5,4,8,6]
    sort = BubbleSort()
    print(sort(nums))

