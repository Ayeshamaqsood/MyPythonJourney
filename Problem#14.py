#Armstrong number Checker
num = int(input("Enter a number:"))
digit_count = 0 
remainder = 0 
temp = num
#Count the number of digits 
while temp > 0: 
    remainder = temp % 10
    digit_count = digit_count + 1
    temp = temp // 10 
print(f"The number of digits are : {digit_count}")
#Power sum 
temp = num 
total_sum = 0
power_result = 1 
while temp > 0:
    remainder = temp % 10
    power_result = 1 
    for i in range(1, digit_count+1):
        power_result *= remainder
    total_sum += power_result
    temp = temp // 10 
if total_sum == num:
     print("The number is Armstrong")
else:
    print("The number is not Armstrong")
