class QuickSort:
    def __call__(self, nums):
        begin, end = 0, len(nums)-1
        return self.quickSort(nums, begin, end)

    def quickSort(self, nums, begin, end):
        if begin >= end:
            return 
        pivot = self.partition(nums, begin, end)
        self.quickSort(nums, pivot+1, end)
        self.quickSort(nums, begin, pivot-1)
        return nums
    
    def partition(self, nums, begin ,end):
        pivot, pointer = end, begin
        for i in range(begin, end):
            if nums[i] < nums[pivot]:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1
        nums[pointer], nums[pivot] = nums[pivot], nums[pointer]
        # pointer point to value > pivot
        return pointer

class MergeSort:
    def __call__(self, nums):
        begin, end = 0, len(nums)
        self.mergesort(nums, begin, end)
        return nums
    
    def mergesort(self, nums, begin, end):
        if begin >= end - 1:
            return
        mid = int((begin + end)/2)
        self.mergesort(nums, mid, end)
        self.mergesort(nums, begin, mid)
        self.merge(nums, begin, end, mid)
    
    def merge(self, nums, begin, end, mid):
        temp = []
        left, right = begin, mid
        while (left < mid and right < end):
            if nums[left] < nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        if left < mid:
            temp.extend(nums[left:mid])
        if right < end:
            temp.extend(nums[right:end])
        nums[begin:end] = temp

from queue import PriorityQueue
class HeapSort:
    def __call__(self, nums):
        q = PriorityQueue()
        len_nums = len(nums)
        for num in nums:
            q.put(num)
        for i in range(len_nums):
            nums[i] = q.get()
        return nums


    
if __name__ == '__main__':
    sort = HeapSort()
    nums = [1,2,3,4,5,6,9,8]
    print(sort(nums))
    
