import heapq

class MaxHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.heap = [0] * (max_size+1)
        self.Front = 1
        self.size = 0
        self.heap[self.Front-1] = 1000000000
    

    def get_left_child(self, pos):
        return pos * 2
    
    def get_right_child(self, pos):
        return pos * 2 + 1
    
    def get_parent_node(self, pos):
        return int(pos // 2)
    

    def is_leaf(self, pos):
        if 2 * pos > self.size and pos <= self.size:
            return True
        return False


    def swap(self, pos, spos):
        self.heap[pos], self.heap[spos] = self.heap[spos], self.heap[pos]
        


    def max_heapify(self, pos):
        if not self.is_leaf(pos):
            left_child_index = self.get_left_child(pos)
            right_child_index = self.get_right_child(pos)
            if self.heap[pos] < self.heap[left_child_index] or \
                self.heap[pos] < self.heap[right_child_index]:
                if self.heap[left_child_index] > self.heap[right_child_index]:
                    self.swap(pos, left_child_index)
                    self.max_heapify(left_child_index)
                else:
                    self.swap(pos, right_child_index)
                    self.max_heapify(right_child_index)

    

    def insert(self, value):
        if self.size > self.max_size:
            return
        
        self.size += 1
        self.heap[self.size] = value

        current = self.size
        while self.heap[current] > self.heap[self.get_parent_node(current)]:
            self.swap(current, self.get_parent_node(current))
            current = self.get_parent_node(current)
    

    def get_max(self):
        return self.heap[self.Front]
    

    def extractMax(self):
        poped = self.heap[self.Front]
        self.heap[self.Front] = self.heap[self.size]
        self.size -= 1
        self.max_heapify(self.Front)
        return poped
    

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
    