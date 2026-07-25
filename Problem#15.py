#Take a list and remove duplicates.

size = int(input("Enter the size of list:"))

numbers = []

for i in range(size+1):
    num = int(input(f"Enter {i+1} element of the list:"))
    numbers.append(num)

print(numbers)

#Check if there are any duplicates

for i in range(len(numbers)-1, -1, -1):
    for j in range(0, i):
        if numbers[j] == numbers[i]:
            print("Duplicate Found!", numbers[j])
            del numbers[i]
            break

print("New List: ", numbers)



