nums = [11,14,15,18,2,4,6,8]

def findNoofRotation(arr):
    start = 0
    end = len(arr) - 1
    n = len(arr)
    while start <= end:
        if arr[start] <= arr[end]:
            return start        
        
        mid = int(start + ((end-start)/2))
        prev = (mid + n - 1) % n
        next = (mid + 1) % n

        if arr[mid] < arr[prev] and arr[mid] < arr[next]:
            return mid
        elif arr[start] <= arr[mid]:
            start = mid + 1
        elif arr[mid] <= arr[end]:
            end = mid - 1


print(findNoofRotation(nums))