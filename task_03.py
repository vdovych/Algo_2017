import math
import copy

class MaxHeap:
    def __init__(self):
        self.A = []

    def add(self, value):
        self.A.append(-math.inf)
        self.increase(len(self.A) - 1, value)

    def increase(self, i, value):
        if value < self.A[i]:
            raise ValueError("Key is smaller that was before")
        self.A[i] = value
        while i > 0 and self.A[(i - 1) // 2] < self.A[i]:
            self.A[i], self.A[(i - 1) // 2] = self.A[(i - 1) // 2], self.A[i]
            i = (i - 1) // 2

    def heapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < len(self) and self.A[l] > self.A[i]:
            lar = l
        else:
            lar = i
        if r < len(self) and self.A[r] > self.A[lar]:
            lar = r
        if lar != i:
            self.A[i], self.A[lar] = self.A[lar], self.A[i]
            self.heapify(lar)

    def get_max(self):
        try:
            return self.A[0]
        except:
            return math.inf

    def extract_max(self):
        if len(self) < 1:
            raise ValueError("Empty heap")
        mx = self.get_max()
        self.A[0] = self.A[-1]
        self.A.pop(-1)
        self.heapify(0)
        return mx

    def __len__(self):
        return len(self.A)


class MinHeap:
    def __init__(self):
        self.A = []

    def add(self, value):
        self.A.append(math.inf)
        self.decrease(len(self.A) - 1, value)

    def decrease(self, i, value):
        if value > self.A[i]:
            raise ValueError("Key is bigger that was before")
        self.A[i] = value
        while i > 0  and self.A[(i - 1) // 2] > self.A[i]:
            self.A[i], self.A[(i - 1) // 2] = self.A[(i - 1) // 2], self.A[i]
            i = (i - 1) // 2

    def heapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < len(self) and self.A[l] < self.A[i]:
            sma = l
        else:
            sma = i
        if r < len(self) and self.A[r] < self.A[sma]:
            sma = r
        if sma != i:
            self.A[i], self.A[sma] = self.A[sma], self.A[i]
            self.heapify(sma)

    def get_min(self):
        try:
            return self.A[0]
        except:
            return -math.inf

    def extract_min(self):
        if len(self) < 1:
            raise ValueError("Empty heap")
        mn = self.get_min()
        self.A[0] = self.A[-1]
        self.A.pop(-1)
        self.heapify(0)
        return mn

    def __len__(self):
        return len(self.A)


class Median:
    def __init__(self):
        self.h_low = MaxHeap()
        self.h_high = MinHeap()

    def add_element(self, value):
        if len(self.h_low) < 1 or value < self.h_low.get_max():
            self.h_low.add(value)
        elif len(self.h_high) < 1 or value > self.h_high.get_min():
            self.h_high.add(value)
        else:
            self.h_high.add(value)
        if len(self.h_low) > len(self.h_high) + 1:
            self.h_high.add(self.h_low.extract_max())
        if len(self.h_low) + 1 < len(self.h_high):
            self.h_low.add(self.h_high.extract_min())

    def get_median(self):
        if len(self.h_low) == len(self.h_high):
            return (self.h_low.get_max(), self.h_high.get_min())
        elif len(self.h_low) > len(self.h_high):
            return self.h_low.get_max()
        else:
            return self.h_high.get_min()

    def get_maxheap_elements(self):
        # self.h_low.reheapify()#Не костиль а фікс
        return self.h_low.A

    def get_minheap_elements(self):
        # self.h_high.reheapify()# Не костиль а фікс
        return self.h_high.A


class MaxPairHeap:
    def __init__(self, root=None, subtrees=[], heap=None):
        if heap != None:
            self.root = heap.root
            self.subtrees = heap.subtrees
        else:
            self.root = root
            self.subtrees = subtrees

    def add(self, value):
        if(self.root != None):
            tmp = self.merge(self, MaxPairHeap(value, []))
            self.root = tmp.root
            self.subtrees = tmp.subtrees
        else:
            self.root = value

    def merge(self, heap1, heap2):
        if len(heap1) == 0:
            return heap2
        if len(heap2) == 0:
            return heap1
        if heap1.root > heap2.root:
            return MaxPairHeap(heap1.root, [heap2] + heap1.subtrees)
        if heap1.root < heap2.root:
            return MaxPairHeap(heap2.root, [MaxPairHeap(heap=heap1)] + heap2.subtrees)

    def get_max(self):
        return self.root

    def merge_pairs(self, pairs):
        if len(pairs) == 0:
            return []
        if len(pairs) == 1:
            return pairs[0]
        return self.merge(self.merge(pairs[0], pairs[1]), self.merge_pairs(pairs[2:]))

    def extract_max(self):
        mx = self.root
        tmp = self.merge_pairs(self.subtrees)
        self.root = tmp.root
        self.subtrees = tmp.subtrees
        return mx

    def asArr(self):
        ret = [self.root]
        for tree in self.subtrees:
            ret += tree.asArr()
        return sorted(ret,reversed=True)

    def __len__(self):
        l = 0
        if self.root != None:
            l += 1
        for tree in self.subtrees:
            l += len(tree)
        return l


class MinPairHeap:
    def __init__(self, root=None, subtrees=[], heap=None):
        if heap != None:
            self.root = heap.root
            self.subtrees = heap.subtrees
        else:
            self.root = root
            self.subtrees = subtrees

    def add(self, value):
        if(self.root != None):
            tmp = self.merge(self, MaxPairHeap(value, []))
            self.root = tmp.root
            self.subtrees = tmp.subtrees
        else:
            self.root = value

    def merge(self, heap1, heap2):
        if len(heap1) == 0:
            return heap2
        if len(heap2) == 0:
            return heap1
        if heap1.root < heap2.root:
            return MinPairHeap(heap1.root, [heap2] + heap1.subtrees)
        if heap1.root > heap2.root:
            return MinPairHeap(heap2.root, [MinPairHeap(heap=heap1)] + heap2.subtrees)

    def get_min(self):
        return self.root

    def merge_pairs(self, pairs):
        if len(pairs) == 0:
            return []
        if len(pairs) == 1:
            return pairs[0]
        return self.merge(self.merge(pairs[0], pairs[1]), self.merge_pairs(pairs[2:]))

    def extract_min(self):
        mx = self.root
        tmp = self.merge_pairs(self.subtrees)
        self.root = tmp.root
        self.subtrees = tmp.subtrees
        return mx

    def asArr(self):
        ret = [self.root]
        for tree in self.subtrees:
            ret += tree.asArr()
        return sorted(ret)

    def __len__(self):
        l = 0
        if self.root != None:
            l += 1
        for tree in self.subtrees:
            l += len(tree)
        return l


class PairingMedian:
    def __init__(self):
        self.h_low = MaxPairHeap()
        self.h_high = MinPairHeap()

    def add_element(self, value):
        if self.h_low.root == None or value < self.h_low.get_max():
            self.h_low.add(value)
        elif self.h_high.root == None or value > self.h_high.get_min():
            self.h_high.add(value)
        else:
            self.h_high.add(value)
        if len(self.h_low) > len(self.h_high) + 1:
            self.h_high.add(self.h_low.extract_max())
        if len(self.h_low) + 1 < len(self.h_high):
            self.h_low.add(self.h_high.extract_min())

    def get_median(self):
        if len(self.h_low) == len(self.h_high):
            return (self.h_low.get_max(), self.h_high.get_min())
        elif len(self.h_low) > len(self.h_high):
            return self.h_low.get_max()
        else:
            return self.h_high.get_min()

    def get_maxheap_elements(self):
        return self.h_low.asArr()

    def get_minheap_elements(self):
        return self.h_high.asArr()
