"""
Max Heap skapades av följande prompt till claude:
'Create a maxheap and a min-heap in python. I want the maxheap to be stored in a list, 
and the minheap in an array'
"""
 
class MaxHeap:
    def __init__(self, items=None):
        self._data = list(items) if items else []
        for i in range(len(self._data) // 2 - 1, -1, -1):
            self._sift_down(i)
 
    def __len__(self):
        return len(self._data)
 
    def __repr__(self):
        return f"MaxHeap({self._data})"
 
    def peek(self):
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]
 
    def push(self, value):
        self._data.append(value)
        self._sift_up(len(self._data) - 1)
 
    def pop(self):
        if not self._data:
            raise IndexError("pop from empty heap")
        top = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            self._sift_down(0)
        return top
 
    def _sift_up(self, i):
        data = self._data
        while i > 0:
            parent = (i - 1) // 2
            if data[i] > data[parent]:
                data[i], data[parent] = data[parent], data[i]
                i = parent
            else:
                break
 
    def _sift_down(self, i):
        data = self._data
        n = len(data)
        while True:
            left, right, largest = 2 * i + 1, 2 * i + 2, i
            if left < n and data[left] > data[largest]:
                largest = left
            if right < n and data[right] > data[largest]:
                largest = right
            if largest == i:
                break
            data[i], data[largest] = data[largest], data[i]
            i = largest
 