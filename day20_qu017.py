'''

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

'''

#code

val = 0

while True:
    s = input()

    if not s:
        break

    list1 = s.split(" ")
    deposit_withdraw = list1[0]
    val1 = int(list1[1])
    if(deposit_withdraw == "D"):
        val += val1
    elif(deposit_withdraw == "W"):
        val -= val1
    else:
        pass


print(val)