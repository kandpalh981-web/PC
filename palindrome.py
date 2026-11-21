
def palindrome(word):
    n=len(word)
    m=word[::-1]
    if word==m:
           return "palindrome"
    else:
         return "not palindrome"
    
a=palindrome(input("enter a word: "))
print(a)


