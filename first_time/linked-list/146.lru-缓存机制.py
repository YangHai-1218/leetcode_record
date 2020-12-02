#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = OrderedDict()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        val = self.dic[key]
        self.dic.move_to_end(key)
        return val


    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)
        self.dic[key] = value
        if len(self.dic) > self.capacity:
            oldest = next(iter(self.dic))
            del self.dic[oldest]


# linked list version
class node(object):
    def __init__(self,data=0,key=0,prev=None,next=None):
        self.data = data
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = dict()
        self.head = node()
        self.tail = node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        node_read = self.cache[key]
        self.move_to_head(node_read)

        return node_read.data

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node_read = self.cache[key]
            node_read.data = value
            self.move_to_head(node_read)
        else:
            node_insert = node(value, key)
            if len(self.cache) < self.capacity:
                self.add_to_head(node_insert)
            else:
                self.move_tail()
                self.add_to_head(node_insert)


    def add_to_head(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.cache[node.key] = node

    def move_to_head(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.add_to_head(node)
    def move_tail(self):
        node_delete = self.tail.prev
        self.tail.prev = node_delete.prev
        node_delete.prev.next = self.tail
        del self.cache[node_delete.key]
        del node_delete
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

a = LRUCache(2)
a.put(1,1)
a.put(2,2)
a.get(1)
a.put(3,3)
a.get(2)
a.put(4,4)
a.get(1)
a.get(3)
a.get(4)
