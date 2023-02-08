#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val 
        self.next = next 

class MyLinkedList:

    def __init__(self):
        self.head = None 
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        node = self.head
        cur_index = 0
        while cur_index < index:
            node = node.next 
            cur_index += 1
        return node.val
            
    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(val=val, next=None)
        else:
            self.head = ListNode(val=val, next=self.head)
        self.size += 1
        # self.printLinkedList()

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(val=val, next=None)
        else:
            node = self.head 
            while node.next is not None:
                node = node.next 
            node.next = ListNode(val=val, next=None)
        self.size += 1
        # self.printLinkedList()

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return -1 
        if index == 0:
            self.addAtHead(val)
        else:
            cur_index = 0
            node = self.head 
            while cur_index < index-1:
                node = node.next 
                cur_index += 1
            newnode = ListNode(val=val, next=node.next)
            node.next = newnode
            self.size += 1
            # self.printLinkedList()


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return -1 
        if index == 0:
            self.head = self.head.next 
        else:
            cur_index = 0
            node = self.head 
            while cur_index < index-1:
                node = node.next 
                cur_index += 1
            node.next = node.next.next
        self.size -= 1
        # self.printLinkedList()
    
    def printLinkedList(self):
        if self.head is None:
            print('empty linked list')
        node = self.head 
        vals = []
        while node is not None:
            vals.append(node.val)
            node = node.next
        print(vals)
        



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
linkedlist = MyLinkedList()
linkedlist.addAtHead(1)
linkedlist.addAtTail(3)
linkedlist.addAtIndex(1, 2)
print(linkedlist.get(1))
linkedlist.deleteAtIndex(1)
print(linkedlist.get(1))


