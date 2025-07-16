'''

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

'''

#code

strx = input()

letters = 0
digits = 0

for i in strx:
    if(i >= 'a' and i <= 'z') or (i >= 'A' and i >= 'Z'):
        letters += 1
    elif (i >= '0' and i <= '9'):
        digits += 1

print("LETTERS", letters)
print("DIGITS", digits)