def count(n):
    return len(str(n))

n = int(input("Enter a positive integer: "))
if(n<=0):
   print("Invalid input")
else:
    print("Digits:",count(n))
