def palindrome(s):
    if(s==s[::-1]):
        print("Palindrome")
    else:
        print("Non Palindrome")

s = input("String: ")
palindrome(s.lower())