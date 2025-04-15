def search(nums,target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = int(start + ((end - start)/2))

        if nums[mid] == target:
            return True
        
        if nums[start] == nums[mid] == nums[end]:
            start += 1
            end -= 1
        
        if nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] <= target < nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return False

nums = [1,1,1,1,1,1,1,1,2,1,1,1,1]

print(search(nums,3))