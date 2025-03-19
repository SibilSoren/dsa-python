nums = [100,80,60,70,60,75,85]

def StockSpan(arr):
    stack = []
    result = []
    for index, value in enumerate(arr):
        if len(stack) == 0:
            result.append(index - -1)
        elif len(stack) != 0 and stack[-1]["value"] > value:
            result.append(index - stack[-1]["index"])
        elif len(stack) != 0 and stack[-1]["value"] <= value:
            while len(stack) > 0 and stack[-1]["value"] <= value:
                stack.pop()
            if len(stack) == 0:
                result.append(index - -1)
            else:
                result.append(index - stack[-1]["index"])
        stack.append({"index":index,"value":value})
    return result


print(StockSpan(nums))