def binarySearch(arr,target,start,end):
    while start <= end:
        mid = int(start + ((end - start)/2))
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def firstSmallestElementIndex(arr):
    start = 0
    end = len(arr) - 1
    n = len(arr)
    while start <= end:
        if arr[start] <= arr[end]:
            return start
        mid = int(start + ((end - start)/2))
        prev = (mid + n - 1) % n
        next = (mid + 1) % n
        if arr[mid] < arr[prev] and arr[mid] < arr[next]:
            return mid
        elif arr[start] <= arr[mid]:
            start = mid + 1
        elif arr[mid] <= arr[end]:
            end = mid - 1
    
def findElement(arr,target):
    minElementIndex = firstSmallestElementIndex(arr)

    leftSearch = binarySearch(arr,target,0,minElementIndex)
    rightSearch = binarySearch(arr,target,minElementIndex,len(arr) - 1)

    if leftSearch == -1 and rightSearch == -1:
        return -1
    elif leftSearch > -1:
        return leftSearch
    elif rightSearch > -1:
        return rightSearch
    
nums = [11,12,14,15,2,5,6,8]
# nums = [1,0,1,1,1]

print(findElement(nums,11))