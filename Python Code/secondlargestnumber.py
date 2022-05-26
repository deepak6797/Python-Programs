number = int(input("Enter the length: "))
list = []
for i in range(0,number):
    digit = int(input("Enter the number: "))
    list.append(digit)
    list.sort()
print(list[number-2])
