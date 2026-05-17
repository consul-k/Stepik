def search(A, elem):
    res = -1
    for i in range(len(A)-1,-1,-1):
        if A[i] == elem:
            res = i
            break
    return res
    
A = [int(i) for i in input().split()]
elem = int(input())
print(search(A, elem))
