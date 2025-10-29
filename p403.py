# Q4 Design and develop a menu-driven Python program for the following list operations.
# a. Create a list of N integers
# b. Display the list elements
# c. Insert an element at a specific position
# d. Delete an element at a given position
# e. Exit
import sys
while(True):
    print("""a. Create a list of N integers
    b. Display the list elements
    c. Insert an element at a specific position
    d. Delete an element at a given position
    e. Exit""")
    ch = input("Enter your choice: ")
    match ch:
        case 'a':
            n = int(input("N: "))  
            lst = []
            print(f"Enter {n} integers:")
            for i in range(n):
                e = int(input())
                lst.append(e)
        case 'b':
            print(lst)
        case 'c':
            el = int(input("Enter an integer: "))
            pos = int(input("Position to insert: "))
            lst.insert(pos,el)
        case 'd':
            pos = int(input("Enter the position:"))
            lst.pop(pos)
        case 'e':
            print("Exiting....")
            sys.exit(0)
        case _:
            print("Invalid choice")