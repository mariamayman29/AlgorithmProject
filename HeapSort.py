# -*- coding: utf-8 -*-
def heap(arr, n, i):
    l =( 2 * i) + 1
    r = (2 * i) + 2
    largest = i

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap(arr, n, largest)

def max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heap(arr, n, i)

def heap_sort(numbers):
    n = len(numbers)
    max_heap(numbers)
    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heap(numbers, i, 0)

# Example Usage
numbers=[]
n=int(input("Enter Array Size"))
for i in range (n):
    num=int(input("Enter A Number"))
    numbers.append(num)
heap_sort(numbers)
print("Sorted array:", numbers)


