# nums = [11,12,14,15,2,5,6,8]
nums = [1,0,1,1,1]

def findMinIndex(arr):
    start = 0
    end = len(arr) - 1
    n = len(arr)
    while start <= end:
        if arr[start] <= arr[end]:
            return start
        mid = int(start + ((end - start)/2))
        prev = (mid + n - 1 ) % n
        next = (mid + 1) % n
        if arr[mid] < arr[prev] and arr[mid] < arr[next]:
            return mid
        elif arr[start] <= arr[mid]:
            start = mid + 1
        elif arr[mid] <= arr[end]:
            end = mid - 1
    
def binarySearch(arr,start,end,target):
    while start <= end:
        mid = int(start + ((end - start)/2))
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
    return -1

def findElement(arr,target):
    minIndex = findMinIndex(arr)
    print(minIndex)
    leftArr = binarySearch(arr,0,minIndex - 1, target)
    rightArr = binarySearch(arr,minIndex,len(arr) -1 , target)
    if leftArr != -1:
        return leftArr
    elif rightArr != -1:
        return rightArr
    return -1

print(findElement(nums,0))
