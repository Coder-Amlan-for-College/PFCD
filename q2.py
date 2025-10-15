def find():
    lst = []
    for i in range(101,500):
        if i%3==0 and i%5==0:
            lst.append(i)
    print("The numbers are:\n",lst)

find()