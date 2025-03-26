# heights = [1,2,1,3,1,3,0,1]
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
def maxRight(arr):
    stack = []
    result = []
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

def maxLeft(arr):
    stack = []
    result = []
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

def getWater(heights):
    maxL = maxLeft(heights)
    maxR = maxRight(heights)

    water = []
    for i in range(len(heights)):
        minHeight = min(maxL[i],maxR[i])
        heightDiff = minHeight - heights[i]
        water.append(heightDiff)
    return sum(water)

print(getWater(heights))