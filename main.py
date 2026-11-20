from maxHeap import MaxHeap
from minHeap import MinHeap
from book import Book
import csv
from memory_profiler import profile

@profile
def createBookList(filename):
    bookList = []
    with open(filename, "r", encoding="utf-8") as file:
        csvFile = csv.reader(file)
        for row in csvFile:
           title, downloads =row[0].split(";")
           newBook = Book(title, downloads)
           bookList.append(newBook)
    return bookList

@profile
def main():
    bookList = createBookList("böcker.csv")
    maxSize = int(input("Bestäm värdet på maxsize\n"))
    maxHeap = MaxHeap(bookList)
    minHeap = MinHeap(maxSize)
    minHeap.createMinHeap(bookList)
    for i in range(len(minHeap.data)):
        print(minHeap.data[i])

main()