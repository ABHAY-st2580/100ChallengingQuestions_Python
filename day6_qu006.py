'''

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

'''

#code
import math
x = input()

list1 = x.split(",")

C, H = 50, 30

ans = []
for i in list1:
    val = (2 * C * float(i))
    ans.append(str(int(round(math.sqrt(val / H)))))

print(",".join(ans))