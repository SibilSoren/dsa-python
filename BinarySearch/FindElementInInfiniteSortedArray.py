def bs(arr,target,start,end):
    while start <= end:
        mid = int(start + ((end - start)/2))
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1
        
def search(nums,target):
    start = 0
    end = 1
    while target > nums[end]:
        start = end
        end *= 2
    return bs(nums,target,start,end)

nums = [1,2,3,4,8,10,12,14]

print(search(nums,10))
    