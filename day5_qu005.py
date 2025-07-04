'''

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

'''

#code

class practice:
    def __init__(self):
        self.stri = ""

    def getString(self):
        self.stri = input()

    def printString(self):
        print(self.stri.upper())


strin = practice()
strin.getString()
strin.printString()
