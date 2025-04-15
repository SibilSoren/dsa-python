def firstOccurrence(nums,target,start,end):
    result = 0
    while start <= end:
        mid = int(start + ((end - start)/2))
        if nums[mid] == target:
            result = mid
            end = mid - 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return result

def search(nums,target):
    start,end = 0 ,1
    while target > nums[end]:
        start = end
        end *= 2
    
    result = firstOccurrence(nums,target,start,end)
    return result

