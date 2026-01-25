#https://code.visualstudio.com/download
#go to extension then install python extension
#to run code, go to terminal then new terminal
#then type your file as for example this file, I named it as main, 
#type at your terminal python main.py
#or maybe if it didn't work try python3 main.py
#if it still doesn't work, make sure you have python installed
#check on your prompt by typong python --version or python3 --version or py --version
#If you don't have python installed, go to https://www.python.org/downloads/


print("Hello world")
#

integer = 5
floatNumber = 5.99
print(integer + floatNumber)
print(5 + 5.99)


string = "This is a sentence"
print(string)
print("Hello World, ", string)


for i in range(5):
    print("Hello, this sentence is printed 5 times")

input = input("Enter your name: ")
print("Hello ", input)

age = int(input("Enter your age: "))
print("You are ", age, " years old")

height = float(input("Enter your height in meters: "))
print(f"You are {height} meters tall")
'''This is a 
multi-line comment
It spans multiple lines
'''
