def peakElement(nums):
    if len(nums) == 1:
        return 0
    start,end = 0 , len(nums) - 1
    while start <= end:
        mid = int(start + ((end - start)/2))
        if mid > 0 and mid < len(nums) - 1:
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] > nums[mid]:
                end = mid - 1
            elif nums[mid + 1] > nums[mid]:
                start = mid + 1
        elif mid == 0:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        elif mid == len(nums) - 1:
            if nums[mid - 1] > nums[mid - 2]:
                return mid - 1
            else:
                return mid - 2
            
nums = [1,2,1,4,5,3,4,7,9]

print(peakElement(nums))