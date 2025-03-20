nums = [100,80,60,70,60,75,85];
# o/p -> 1,1,1,2,1,4,6

def StockSpan(stocks):
    stack = []
    result = []

    for stock in stocks:
        res = 1
        while stack and stack[-1][0] <= stock:
            res += stack.pop()[1]
        stack.append([stock,res])
        result.append(res)
        
    
    # for idx,value in enumerate(stocks):

    #     if not stack:
    #         result.append(idx - -1)
    #     elif stack and stack[-1][0] > value:
    #         result.append(idx - stack[-1][1])
    #     elif stack and stack[-1][0] <= value:
    #         while stack and stack[-1][0] <= value:
    #             stack.pop()
    #         if not stack:
    #             result.append(idx - -1)
    #         else:
    #             result.append(idx - stack[-1][1])
    #     stack.append([value,idx])
    
    return result


print(StockSpan(nums))