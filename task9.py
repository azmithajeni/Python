salary = int(input("Salary :"))
age= int(input("age :"))
if(salary >= 20000 or age >= 25):
    loan=int(input("Enter the loan amount:"))
    if(loan >= 50000):
        print("Maximun amt is 50000")
    else:
        print("No loan")
    print("You are eligible")
else:
    print("Not eligible")
