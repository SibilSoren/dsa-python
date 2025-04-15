def search(nums,target):
    start,end = 0, len(nums) - 1
    res = -1
    while start <= end:
        mid = int(start + ((end - start)/2))
        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            start = mid + 1
        else:
            res = nums[mid]
            end = mid - 1
    return res

nums = [1,2,3,4,8,10,12,14]

print(search(nums,11))