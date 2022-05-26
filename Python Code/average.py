number = int(input("Enter the number: "))
sum = 0
count = 0
while number!=0:
    count = count+1
    digit = number % 10
    sum = sum + digit
    number = number // 10
avg = sum / count
print(avg)