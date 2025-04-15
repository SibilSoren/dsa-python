def findMaximum(nums):
    if len(nums) == 1:
        return nums[0]
    start,end = 0, len(nums) - 1
    while start <= end:
        mid = int(start + ((end - start)/2))
        if mid > 0 and mid < len(nums) - 1:
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return nums[mid]
            elif nums[mid + 1] > nums[mid]:
                start = mid + 1
            elif nums[mid - 1] > nums[mid]:
                end = mid - 1
        


nums = [1,2,3,8,6,5,4,3,2,1]

print(findMaximum(nums))