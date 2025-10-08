import sys
mark = float(input("Enter the marks: "))
if(mark>100.0 or mark<0.0):
    print("Invalid marks")
    sys.exit(0)
if(mark>=90.0):
    print("Grade: A \nExcellent!")
elif(mark>=80.0):
    print("Grade: B \nGood")
elif(mark >= 70):
    print("Grade: C \nAverage")
elif(mark>=60):
    print("Grade: D \nNeeds Improvement")
else:
    print("Grade: F \nFailing")

