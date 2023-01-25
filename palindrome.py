def ispalindrome(s):
    return s==s[::-1]
s="123"
ans=ispalindrome(s)
if ans:
    print("True")
else:
    print("false")
    
