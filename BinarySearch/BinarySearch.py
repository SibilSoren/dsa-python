nums = [1,2,3,4,5,6,7,8,9]

def binarySearch(arr,target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int(start + ((end -start) /2))
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
    return -1

print(binarySearch(nums,9))
    