import heapq

class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.Front = 1
        self.heap = [0] * maxsize
        self.heap[0] = 10000000
        self.size = 0
    

    def get_left_chid(self, pos):
        return 2 * pos
    
    def get_right_child(self, pos):
        return 2 * pos + 1
    
    def get_parent_node(self, pos):
        return int(pos//2)
    
    def is_leaf(self, pos):
        if pos * 2 > self.size:
            return True
        return False
    
    def max_heapify(self, pos):
        if not self.is_leaf(pos):
            left_child_pos = self.get_left_chid(pos)
            right_child_pos = self.get_right_child(pos)
            if self.heap[pos] < self.heap[left_child_pos] or \
                self.heap[pos] < self.heap[right_child_pos]:
                if self.heap[left_child_pos] > self.heap[right_child_pos]:
                    self.heap[pos], self.heap[left_child_pos] = self.heap[left_child_pos], self.heap[pos]
                    self.max_heapify(left_child_pos)
                else:
                    self.heap[pos], self.heap[right_child_pos] = self.heap[right_child_pos], self.heap[pos]
                    self.max_heapify(right_child_pos)
    
    def insert(self, val):
        self.size += 1
        self.heap[self.size] = val
        curr = self.size
        while self.heap[self.get_parent_node(curr)] < self.heap[curr]:
            self.heap[curr], self.heap[self.get_parent_node(curr)] = self.heap[self.get_parent_node(curr)], self.heap[curr]
            curr = self.get_parent_node(curr)


        


    def extractmax(self):
        popped = self.heap[self.Front]
        self.heap[self.Front], self.heap[self.size] = self.heap[self.size], self.heap[self.Front]
        self.size -= 1
        self.max_heapify(self.Front)
        return popped



    

def test():
    maxheap = MaxHeap(100)
    maxheap.insert(10)
    maxheap.insert(20)
    maxheap.insert(30)
    maxheap.insert(40)
    maxheap.insert(25)
    maxheap.insert(15)
    print(maxheap.heap[maxheap.Front:maxheap.size+1])


def test_2():
    maxheap = []
    heapq.heappush(maxheap, -1 * 10)
    heapq.heappush(maxheap, -1 * 20)
    heapq.heappush(maxheap, -1 * 30)
    heapq.heappush(maxheap, -1 * 40)
    heapq.heappush(maxheap, -1 * 25)
    heapq.heappush(maxheap, -1 * 15)
    print(maxheap)
    print(f"max_num:{-heapq.heappop(maxheap)}")

if __name__ == '__main__':
    test()
    test_2()
    