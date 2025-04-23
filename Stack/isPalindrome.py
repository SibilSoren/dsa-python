def isPalindrome(s):
    lowerStr = "".join(i for i in s if i.isalnum()).lower()
    revStr = "".join(reversed(lowerStr))

    return lowerStr == revStr


s = "A man, a plan, a canal: Panama"

print(isPalindrome(s)) 