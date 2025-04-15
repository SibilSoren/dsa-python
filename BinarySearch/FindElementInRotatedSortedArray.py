def search(nums,target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = int(left + ((right - left)/2))

        if nums[mid] == target:
            return True

        # If duplicates, we can't determine the sorted side
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        # Left half is sorted
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Target in left sorted part
            else:
                left = mid + 1   # Target in right part
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Target in right sorted part
            else:
                right = mid - 1  # Target in left part

    return False