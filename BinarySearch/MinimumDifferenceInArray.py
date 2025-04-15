def minimumDifference(nums,target):
    start,end = 0 , len(nums) - 1
    while start <= end:
        mid = int(start + ((end - start)/2))
        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            
            start = mid + 1
        else:
            
            end = mid - 1
    leftDiff = abs(nums[start] - target) if start < len(nums) else float('inf')
    rightDiff = abs(nums[end] - target) if end >= 0 else float('inf')

    return min(leftDiff, rightDiff)

nums = [1,2,2,3,4,8,13,18]

print(minimumDifference(nums,15))

