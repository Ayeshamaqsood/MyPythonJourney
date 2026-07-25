#Find Second smallest
numbers = [ 1, 1, 2, 3, 4]
smallest = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] < smallest:
        smallest = numbers[i]
    i += 1
print("The Smallest number is: ", smallest)

second_smallest = float('inf') #i dont understand
i = 0
while i < len(numbers):
    if numbers[i] < second_smallest and numbers[i] > smallest:
        second_smallest = numbers[i]
    i += 1
print("The Second Smallest number is: ", second_smallest)