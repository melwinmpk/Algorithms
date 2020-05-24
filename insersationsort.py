'''
INSERTION-SORT(A) cost times
1 for j ← 2 to length[A]                c1 n
2   do key ← A[j]                       c2 n - 1
    3 ▹ Insert A[j] into the sorted
    sequence A[1  j - 1].              0        n - 1
4   i ← j - 1                           c4 n - 1
5   while i > 0 and A[i] > key          c5
6       do A[i + 1] ← A[i]              c6
7       i ← i - 1                       c7
8   A[i + 1] ← key                      c8 n - 1
'''
def insersationsort(listarray):
    for i in range(1, len(listarray)):
        key = listarray[i]
        j = i - 1
        while j >= 0 and listarray[j] > key:
            listarray[j+1] = listarray[j]
            j-=1
        listarray[j+1] = key

arr = [12, 11, 13, 5, 6]
insersationsort(arr)
print ("Sorted array is:")
print(arr)
