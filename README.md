# ALgorithm Analysis
#HeapSort
Time Complexity of HeapSort
Heap Function:
In the worst case, Heap is called recursively for log(n) levels of the heap.
O(logn).
Max-Heap Function:
The time complexity is 
O(n) 
Heap Sort Function:

Extracting the maximum element (root) takes 
𝑂(log𝑛)
Total complexity: 
𝑂(𝑛log𝑛)

#kruskal
Time Complexity :
Sorting Edges:
Sorting all 
n edges takes 𝑂(nlogn)
UnionFind Operations:
Using path compression and union by rank:𝑂(1)
For n edges, the total complexity for union-find is (n𝛼(𝑉))
where 𝛼is the inverse Ackermann function, very small for practical purposes.
Overall Complexity:O(nlogn+n⋅α(V)), which simplifies to 
O(nlogn) 

