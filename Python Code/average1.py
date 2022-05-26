number  = int(input("Enter the length of digits: "))
list = []
for i in range (0, number):
    digit = int(input("Enter the number: "))
    list.append(digit)
avg = sum(list) / number
print(avg)

