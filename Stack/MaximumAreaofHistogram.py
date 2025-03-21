def NSL(arr):
    stack = []
    result = []
    for i,value in enumerate(arr):
        if len(stack) == 0:
            result.append(-1)
        elif len(stack) != 0 and stack[-1][0] < value:
            result.append(stack[-1][1])
        elif len(stack) != 0 and stack[-1][0] >= value:
            while len(stack) > 0 and stack[-1][0] >= value:
                stack.pop()
            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1][1])
        stack.append([value,i])
    return result


def NSR(arr):
    stack = []
    result = []
    for i,value in enumerate(reversed(arr)):
        reverse_index = len(heights) - 1 - i

        if len(stack) == 0:
            result.append(len(arr))
        elif len(stack) != 0 and stack[-1][0] < value:
            result.append(stack[-1][1])
        elif len(stack) != 0 and stack[-1][0]  >= value:
            while len(stack) > 0 and stack[-1][0] >= value:
                stack.pop()
            if len(stack) == 0:
                result.append(len(arr))
            else:
                result.append(stack[-1][1])
        # print(value,reverse_index)
        stack.append([value,reverse_index])
    
    result.reverse()
    return result

heights = [2,4]


def maxArea(arr):
    left = NSL(arr)
    right = NSR(arr)

    print(left,right)

    area = []
    for i,value in enumerate(arr):
        area.append((right[i] - left[i] - 1) * value)

    return abs(max(area))

print(maxArea(heights))
