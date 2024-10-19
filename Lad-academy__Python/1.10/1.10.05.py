def cyclic_shift(arr, k):
    n = len(arr)
    k = k % n
    print(*(arr[-k:] + arr[:-k]))

arr = list(map(int, input().split()))
k = int(input())

cyclic_shift(arr, k)
