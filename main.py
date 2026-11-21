#Namn: Simon Ek de Bernardo
#KTH-mail: Sedb@ug.kth.se

from maxHeap import MaxHeap
from minHeap import MinHeap
from book import Book
import csv
from memory_profiler import profile
from codecarbon import EmissionsTracker


def createBookList(filename):
    bookList = []
    with open(filename, "r", encoding="utf-8") as file:
        csvFile = csv.reader(file)
        for row in csvFile:
           title, downloads =row[0].split(";")
           newBook = Book(title, downloads)
           bookList.append(newBook)
    return bookList

#@profile
def initMinHeap(bookList, maxSize):
    minHeap = MinHeap(maxSize)
    minHeap.createMinHeap(bookList)

def initMaxHeap(bookList, maxSize):
    maxHeap = MaxHeap(bookList)
    limitedMaxHeap = []
    for i in range(maxSize):
        limitedMaxHeap.append(maxHeap.data[i])


def main(maxSize):
    bookList = createBookList("böcker.csv")
    
    minHeapTracker = EmissionsTracker()
    minHeapTracker.start()
    initMinHeap(bookList, maxSize)
    minHeapEmissions = minHeapTracker.stop()
    
    maxHeapTracker = EmissionsTracker()
    maxHeapTracker.start()
    initMaxHeap(bookList, maxSize)
    maxHeapEmissions = maxHeapTracker.stop()
    print(f"Maxheap utsläpp:{maxHeapEmissions*1000}")
    print(f"MinHeap utsläpp:{minHeapEmissions*1000}")
    

main(100)