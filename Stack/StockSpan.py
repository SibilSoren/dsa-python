nums = [100,80,60,70,60,75,85]

def StockSpan(arr):
    stack = []
    result = []

    

    # while stack and stack[-1][0]
    # for index, value in enumerate(arr):
    #     if len(stack) == 0:
    #         result.append(index - -1)
    #     elif len(stack) != 0 and stack[-1]["value"] > value:
    #         result.append(index - stack[-1]["index"])
    #     elif len(stack) != 0 and stack[-1]["value"] <= value:
    #         while len(stack) > 0 and stack[-1]["value"] <= value:
    #             stack.pop()
    #         if len(stack) == 0:
    #             result.append(index - -1)
    #         else:
    #             result.append(index - stack[-1]["index"])
    #     stack.append({"index":index,"value":value})
    # return result

    ## Another way of writing the same problem.

    for value in arr:
        res = 1
        while stack and stack[-1][0] <= value:
            res += stack.pop()[1]
        stack.append([value,res])
        result.append(res)
    
    return result

print(StockSpan(nums))