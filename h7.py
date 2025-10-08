num = int(input("Enter a number: "))
s=0
for j in range(1,num):
    c=0
    for i in range(1,j+1):
       if(j%i==0):
          c+=1
          
    if(c==2):
       s+=j

print("Sum:",s)