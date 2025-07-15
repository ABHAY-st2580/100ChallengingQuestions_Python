'''

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010

'''

#code

x = input()
ans = []
list1 = x.split(",")

for i in list1:
    base_2_int = int(i,2)

    if base_2_int % 5 == 0:
        ans.append(i)

print(",".join(ans))
