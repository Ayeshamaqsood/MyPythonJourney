#reverse a number
num = int(input("Enter a number: "))
new_num = 0 
while num > 0 :
    remainder = num % 10
    new_num = new_num * 10 + remainder
    num = num // 10
print(new_num)

