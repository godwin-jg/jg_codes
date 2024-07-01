def mergecall(arr):
    mergesort(arr,0,len(arr)-1)
    
def mergesort(arr,l,r):
    if l>r:return
    mid = (l + r) // 2
    
    mergesort(arr,l,mid-1)
    mergesort(arr,mid+1,r)
    
    merge(arr,l,r,mid)

def merge(arr,l,r,mid):
    left,right = [],[]
    for i in range(l,mid+1):
        left.append (arr[i])
    for i in range(mid+1,r+1):
        right.append(arr[i])
    # left = arr[l:mid+1]
    # right = arr[mid+1:r+1]
    i,j,k = 0,0,l
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i<len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j<len(right):
        arr[k] = right[j]
        j += 1
        k += 1

arr = [19,8,100,5,-3,0]
mergecall(arr)
print(arr)
