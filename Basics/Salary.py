a = int(input("Enter the number of empolyees: "))
i = 0
while i<a:
    i = i+1
    name = input("Enter the name of empolyee: ")
    salary = int(input("Enter the salary of empolyee: "))
    if salary>10000:
        tax = (salary*10)/100
        print("The tax of empolyee is: ",tax)
    else:
        print("No tax")
print("Thank you")