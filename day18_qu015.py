'''

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

'''

#code

a = int(input())

n1 = a
n2 = a*10 + a
n3 = a*100 + n2
n4 = a*1000 + n3

print(n1 + n2 + n3 + n4)
