'''

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

'''

#code

str_val = input()
upper, lower = 0, 0
for i in str_val:
    if(i >= "A" and i <= "Z"):
        upper += 1
    elif(i >= "a" and i <= "z"):
        lower += 1

print("UPPER CASE", upper)
print("LOWER CASE", lower)
