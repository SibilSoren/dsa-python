def firstOccur(arr,target):
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

nums = [0,1,1,3,4,4,4,4,6,6,7,7,7,9]

print(firstOccur(nums,6))