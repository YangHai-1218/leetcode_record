class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def mergeKLists(self, lists):
        merged_list = []
        indexs = []
        len_lists = []
        for list_i in lists:
            indexs.append(0)
            len_lists.append(len(list_i))
        
        while True:
            terminate = all([index == len_list for index, len_list in zip(indexs, len_lists)])
            if terminate:
                break

            min_num, min_num_index = 10000, -1
            for i, (index, list_i) in enumerate(zip(indexs, lists)):

                if index == len(list_i):
                    continue
                if min_num > list_i[index]:
                    min_num = list_i[index]
                    min_num_index = i
            indexs[min_num_index] += 1
            merged_list.append(min_num)
            
        return merged_list
    
    def mergreKlinkedlists(self, lists):
        mergered_list_head = ListNode()
        mergered_list = ListNode()
        mergered_list_head = mergered_list
        while True:
            terminate = all[list_i is None for list_i in lists]
            if terminate:
                break
            
            min_num, min_num_index = 1000000, -1
            for i, list_i in enumerate(lists):
                if list_i is None:
                    continue
                    
                if min_num > list_i.val:
                    min_num = list_i.val
                    min_num_index = i
            lists[min_num_index] = lists[min_num_index].next
            mergered_list.val = min_num
            mergered_list.next = ListNode()
            mergered_list = mergered_list.next
        return mergered_list_head.next




if __name__ == '__main__':
    lists = [[1,4,5],[1,3,4],[2,6]]
    solution = Solution()
    print(solution.mergeKLists(lists))



