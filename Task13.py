a= int(input())
b= int(input())
even_count = 0
odd_count = 0
for i in range(a,b):
    if(i%2==0):
        even_count = even_count+1
    else:
        odd_count = odd_count+1
print("Odd = ",odd_count)
print("Even = ",even_count)  
