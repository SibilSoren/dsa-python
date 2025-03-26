nums = [2,10,10,10,10,14,19]

def firstOccurrence(arr,target):
    start = 0
    end = len(arr) - 1
    result = -1
    while start <= end:
        mid = int(start + ((end - start)/2))
        if arr[mid] == target:
            result = mid
            end = mid - 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return result

print(firstOccurrence(nums,10))