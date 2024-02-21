Tamil = int(input("Tamil:"))
English = int(input("English:"))
Maths=int(input("Maths:"))
Science =int(input("Science:"))
Social = int(input("Social:"))
add=int(Tamil+English+Maths+Science+Social)
avg =add/5
print(avg)
if(avg>35):
    print("You are good to go")
else:
    print("Need additional class")
