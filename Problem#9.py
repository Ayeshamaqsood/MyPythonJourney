#find no of even digits in a string ..
num = int(input("Enter a number: "))
count = 0 
while num > 0:
    remainder = num % 10 ; 
    if remainder % 2 == 0:
        count += 1
    num = num // 10
print(f"The number of even values are: ", count)