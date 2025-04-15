def search(chars,target):
    start, end = 0, len(chars) - 1
    res = None

    while start <= end:
       
        mid = start + (end - start) // 2
        
        if chars[mid] > target:
            res = chars[mid]
            end = mid - 1
        else:
            start = mid + 1

        print(res,mid)

    return res

chars = ['a','b','c','e','f','h']

print(search(chars,'d'))