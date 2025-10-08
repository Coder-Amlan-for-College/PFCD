while(True):
    exp = input("Enter two numbers and operator(+,-,*,/) e.g. [5 4 +] : ")
    if exp.lower()=='exit':
        print("Quiting...")
        exit(0)
    n1,n2,op = exp.split(" ")
    n1 = float(n1)
    n2 = float(n2)
    match op:
        case '+':
            print("Sum:",(n1+n2))
        case '-':
            print("Difference:",(n1-n2))
        case '*':
            print("Product:",(n1*n2))
        case '/':
            print("Quotient:",(n1/n2))
        case _:
            print("Invalid input")
    print("type 'exit' to quit")