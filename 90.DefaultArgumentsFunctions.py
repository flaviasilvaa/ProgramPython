##this program is going to pass a default argumentments using function

def students_details(name="Ben", school="DCU", math=50, cloud=78, sql=60,
                     java=87, enrolled=True):
    total = math + sql + java

    print("Name:", name)
    print("School:", school, "Enrolled:", enrolled)
    print("Math:", math)
    print("Cloud Computer:", cloud)
    print("SQL:", sql)
    print("java:", java)
    print("Score:", total)


##to invoke a function
print(students_details())

print(students_details("Flavia", "CCT", 90, 89, 56, ))  ##I can pass how many arguments I want it

