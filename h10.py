s = input("Enter the string: ")
for i in range(len(s)):
    temp = ""
    for j in range(i,len(s)):
        temp += s[j]
        print(f"\"{temp}\" ")