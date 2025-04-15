def search(nums,target):
    row = 0
    col = len(nums[0]) - 1
    n = len(nums)
    print(row,col,n)
    while row >= 0 and row < n and col >= 0 and col < n:
        if nums[row][col] == target:
            return (row,col)
        elif nums[row][col] > target:
            col -= 1
        elif nums[row][col] < target:
            row += 1
    return -1

nums = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

print(search(nums,8))