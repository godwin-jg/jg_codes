def partition(low,high):
    pivot = arr[high]
    i = low-1
    
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
            
    arr[i+1],arr[high] = arr[high],arr[i+1]
    
    return i+1

def qs(low,high):
    if low<high:
        p = partition(low,high)
        qs(low,p-1)
        qs(p+1,high)
     
        
def quicksort(arr):
    qs(0,len(arr)-1)
    
arr = [10, 7, 8, -9, 1, 5] 
quicksort(arr)
print(arr)
    
    
            
