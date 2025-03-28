nums = [3,4,5,1,2]

def rotateArr(arr,k):
    count = 1
    n = len(arr) - 1
    if k == 0:
        return arr 
    while count <= k:
        arr.append(arr[0])
        arr.pop(0)
        count += 1
    return arr

def findIndex(arr):
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

def arraySortedOrNot(arr, n):

    # Base case
    if (n == 0 or n == 1):
        return True
        
    # Check if present index and index 
    # previous to it are in correct order
    # and rest of the array is also sorted
    # if true then return true else return
    # false
    return (arr[n - 1] >= arr[n - 2] and
            arraySortedOrNot(arr, n - 1))

def isSortedAndRotated(arr):

    idx = findIndex(arr)
    print(idx)
    rotateArr(arr,idx)
    return arraySortedOrNot(arr,len(arr))

    
        

print(isSortedAndRotated(nums))