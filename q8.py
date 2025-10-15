def days(month):
    lst1 = ["january","march","may","july","august","october","december"]
    lst2 = ["april","june","september","november"]
    if month in lst1:
        print("No. of days: 31days")
    elif month in lst2:
        print("No. of days: 30days")
    elif month=='february':
        print("No. of days: 28/29days")
    else:
        print("Invalid month")

month = input("Enter the month: ")
days(month.lower())