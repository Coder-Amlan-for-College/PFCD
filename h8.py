while(True):
    num = int(input("Enter a number: "))
    if(num > 0):
        break

if(num%2 == 0):
    print("Number is even, after multiplying by 2:",num*2)
else:
    print("Number is odd, after squaring:",num**2)