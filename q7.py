def check(ch):
    ch = ch.lower()
    lst = ['a','e','i','o','u']
    if ch in lst:
        print("Vowel")
    else:
        print("Consonant")

ch = input("Enter an Alphabet: ")
if(len(ch)>1):
    print("Invalid input")
else:
    check(ch)