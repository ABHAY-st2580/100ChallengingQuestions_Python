'''

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

'''

#code

inputtedVar = input()

list1 = inputtedVar.split(",")

tup1 = tuple(list1)

print(list1)
print(tup1)