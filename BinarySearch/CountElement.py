nums = [2,8,10,10,10,14,19]

def firstOccurrence(arr,target):
    start = 0
    end = len(arr) - 1
    result = -1
    while start <= end:
        mid = int(start + ((end - start)/2))
        if arr[mid] == target:
            result = mid
            #now we start to search to the left of the array if the array is sorted in ascending order
            end = mid - 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return result

def lastOccurrence(arr,target):
    start = 0
    end = len(arr) - 1
    result = -1
    while start <= end:
        mid = int(start + ((end - start)/2))
        if arr[mid] == target:
            result = mid
            #now we start to search to the right of the array if the array is sorted in ascending order
            start = mid + 1 
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return result



def countElements(arr,target):

    firstIndex = firstOccurrence(arr,target)
    lastIndex = lastOccurrence(arr,target)

    return lastIndex - firstIndex + 1

print(countElements(nums,10))