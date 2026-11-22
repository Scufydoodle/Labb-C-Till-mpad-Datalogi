#Namn: Simon Ek de Bernardo
#KTH-mail: Sedb@ug.kth.se

from maxHeap import MaxHeap
from minHeap import MinHeap
from book import Book
import csv
import tracemalloc
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


def initMinHeap(maxSize):
    bookList = createBookList("böcker.csv")
    minHeap = MinHeap(maxSize)
    minHeap.createMinHeap(bookList)

def initMaxHeap(maxSize):
    bookList = createBookList("böcker.csv")
    maxHeap = MaxHeap(bookList)
    limitedMaxHeap = []
    for i in range(maxSize):
        limitedMaxHeap.append(maxHeap.data[i])
tracemalloc.start()

initMinHeap(10000)

print(tracemalloc.get_traced_memory())

tracemalloc.stop()