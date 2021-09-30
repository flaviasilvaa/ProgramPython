#this program is going to inform based in the user input how many days is in the month choosed

month = input("Enter the name of the month\n").upper()

if month == "FEBRUARY":
    print("number of the days is 28/29")
elif month in ("APRIL", "JUNE", "SEPTEMBER", "NOVEMBER"):
    print("Number of days:  30 days")
elif month in ("JANUARY", "MARCH", "MAY","JULY", "AUGUST","OCTOBER", "DECEMBER"):
    print("Number of days: 31 days")
else:
    print("Please inform a correct month!!!")