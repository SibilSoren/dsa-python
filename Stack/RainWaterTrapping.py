# heights = [3,0,0,2,0,4]
# heights = [0,1,0,2,1,0,1,3,2,1,2,1]
heights = [2,0,2]

def maxLeft(arr):
    result = []
    stack = []
    for i in arr:
        if not stack:
            result.append(i)
            stack.append(i)
        elif stack and stack[-1] > i:
            result.append(stack[-1])
        elif stack and stack[-1] <= i:
            result.append(i)
        if stack[-1] <= i: 
            stack.append(i)
        
    return result

def maxRight(arr):
    result = []
    stack = []
    for i in reversed(arr):
        if not stack:
            result.append(i)
            stack.append(i)
        elif stack and stack[-1] > i:
            result.append(stack[-1])
        elif stack and stack[-1] <= i:
            result.append(i)
        if stack[-1] <= i: 
            stack.append(i)
    result.reverse()
    return result

def rainWater(heights):
    maxL = maxLeft(heights)
    maxR = maxRight(heights)
    print(maxL)
    print(maxR)
    waterList = []
    for i in range(len(heights)):
        minHeight = min(maxL[i],maxR[i])
        heightDiff = minHeight - heights[i]
        waterList.append(heightDiff)
    print(waterList)
    return sum(waterList)

print(rainWater(heights))