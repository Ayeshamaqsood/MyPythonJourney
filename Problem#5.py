num = int(input("Enter a number: "))
sum = 0
temp = num

while num > 0:
    remainder = num % 10
    sum = sum + remainder
    num = num // 10 
print(f"Sum of digits of {temp} is: {sum}")

