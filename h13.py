s = input("Enter the letter and number [e.g. a1]: ")
if len(s)>2:
    print("Invalid input")
    exit(0)
ch = s[0].lower()
n = int(s[1])
if n<1 or n>8:
    print("Invalid input")
    exit(0)

match ch:
    case 'a'|'c'|'e'|'g':
        if(n%2==0):
            print("White")
        else:
            print("Black")
    case 'b'|'d'|'f'|'h':
        if(n%2!=0):
            print("Black")
        else:
            print("White")
    case _:
        print("Invalid input")        
    
        
