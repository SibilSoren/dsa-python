nums = [9,4,6,8,10,3]

def nearestGreaterRight(arr):
    
    stack = []
    result = []

    
    for num in reversed(arr):
        if not stack:
            result.append(-1)
        elif stack and stack[-1] > num:
            result.append(stack[-1])
        elif stack != 0 and stack[-1] <= num:
            while stack and stack[-1] <= num:
                stack.pop()
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
        stack.append(num)
    
    result.reverse()
    return result

print(nearestGreaterRight(nums))