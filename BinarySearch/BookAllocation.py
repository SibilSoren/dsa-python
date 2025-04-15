def isPossible(books,m,mid):
    students = 1
    maxPageSum = 0
    for book in books:
        if maxPageSum + book <= mid:
            maxPageSum += book
        else:
            students += 1
            if students > m or book > mid:
                return False
    return True

def allocateBooks(books,m): #m -> number of students
    if len(books) < m: return -1 #edge case

    start = min(books)
    end = sum(books)
    result = -1
    while start <= end:
        mid = int(start + ((end - start)/2))
        if isPossible(books,m,mid):
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result
        
books = [10,20,30,40]

print(allocateBooks(books,3))