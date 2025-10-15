def fun(num):
    lst = []
    for i in str(num):
     if not i in lst:
          lst.append(i)
    lst.sort(reverse=True)
    print("First greatest: ",lst[0])
    print("Second greatest: ",lst[1])
    print("Third greatest: ",lst[2])


num = int(input("Number: "))
fun(num)