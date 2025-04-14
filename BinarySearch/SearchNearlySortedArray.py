def searchNearlySorted(arr,target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int(start + ((end - start)/2))
        if arr[mid] == target:
            return mid
        elif mid - 1 >= start and arr[mid - 1] == target:
            return mid - 1
        elif mid + 1 <= end and arr[mid + 1] == target:
            return mid + 1
        
        if arr[mid] < target:
            start = mid + 2
        else:
            end = mid - 2
    return -1

nums = [5,10,30,20,50]

print(searchNearlySorted(nums,100))