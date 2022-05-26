value = input("Enter the string value: ")
vowels = 0
for i in value:
    if (i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U"):
        vowels = vowels+1
print(vowels)