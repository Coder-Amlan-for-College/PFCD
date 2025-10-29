import random as rd
n = int(input("Size: "))
lst = []
for i in range(n):
    lst.append(rd.random())

print("List:",lst)
print("Sum:",sum(lst))
print("Average:",sum(lst)/n)

'''
Size: 5
List: [0.9758057852667823, 0.42608913628336864, 0.5560035132591358, 0.6615830234431948, 0.004145781425571982]
Sum: 2.6236272396780533
Average: 0.5247254479356107
'''