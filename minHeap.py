
"""
Min Heap skapades av följande prompt till claude:
'Create a maxheap and a min-heap in python.'
"""
#Jag valde själv att använda en array för att lagra datan, då min heapen ska vara begränsad, något som en lista inte kan vara

class MinHeap:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.data = []

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f"MinHeap({self.data})"

    def peek(self):
        if not self.data:
            raise IndexError("peek from empty heap")
        return self.data[0]

    def insert(self, value):
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def pop(self):
        if not self.data:
            raise IndexError("pop from empty heap")
        top = self.data[0]
        last = self.data.pop()
        if len(self.data):
            self.data[0] = last
            self._sift_down(0)
        return top

    def _sift_up(self, i):
        data = self.data
        while i > 0:
            parent = (i - 1) // 2
            if data[i].downloads < data[parent].downloads:
                data[i], data[parent] = data[parent], data[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        data = self.data
        n = len(data)
        while True:
            left, right, smallest = 2 * i + 1, 2 * i + 2, i
            if left < n and data[left].downloads < data[smallest].downloads:
                smallest = left
            if right < n and data[right].downloads < data[smallest].downloads:
                smallest = right
            if smallest == i:
                break
            data[i], data[smallest] = data[smallest], data[i]
            i = smallest


    #Denna funktion byggde jag själv för att begränsa antalet data som finns i minHeap
    def createMinHeap(self, bookList):
        for i in range(len(bookList)):
            if i <= 99:
                self.insert(bookList[i])
            elif self.peek().downloads < bookList[i].downloads and i > 99:
                self.data[0] = bookList[i]

        for i in range(len(self.data) // 2 - 1, -1, -1):
                    self._sift_down(i)
        
        
        

        