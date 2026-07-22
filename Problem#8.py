# find second largest in the list 
numbers = [10, 20, 30,40, 50]
largest = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    i += 1
print("The largest number is: ", largest)

second_largest = numbers[0]
i = 1
while i < len(numbers): 
    if numbers[i] > second_largest and numbers[i] < largest:
        second_largest = numbers[i]
    i += 1
print("The second largest number is: ", second_largest)