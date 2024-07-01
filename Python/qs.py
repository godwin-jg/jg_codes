def quicksort(arr):
    qs(arr,0,len(arr)-1)
    
def qs(arr,l,r):
    if l<r:
        p = partition(arr,l,r)
        qs(arr,0,p-1)
        qs(arr,p+1,r)
        
def partition(arr,l,r):
    if l<r:
        i = l-1
        pivot = arr[r]
        for j in range(l,r):
            if arr[j]<pivot:
                i += 1
                arr[j],arr[i] = arr[i],arr[j]
        arr[i+1],arr[r] = arr[r],arr[i+1]
    return i+1

arr = [19,8,100,5,-3,0]
quicksort(arr)
print(arr)