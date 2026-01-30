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

#variables for numbers 
#notes: for variables, there are no rules in naming them (You don't have to name them as integer/float/string. name it anything except a function. 
integer = 5 #natural number is an integer
floatNumber = 5.99 #decimal is saved as a float 
print(integer + floatNumber)
print(5 + 5.99)

#variables for sentence
string = "This is a sentence"
print(string)
print("Hello World, ", string)

#loops
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
#defining function
#we will tell if a number is even or odd by using % 
# We sometimes use % a lot for calculating remainders
# example: num is 8 
#if 8 % 2 == o, return true(Print even)
#any odd number divided by 2 always ends up with a remainder(int divided by an int equals a float)
def comparing(num):
    if num % 2 == 0:
        return True 
    else:
        return False
#def comparing is the equation/ rule to know if the number input is even or odd
def main(): #main is the body that makes use of the comparing(think of it as main is the worker, and comparing is the tool to get the job done)
    num = int(input("Please input a number, I'll tell if it was an even or an odd: "))
    if comparing(num) == True:
        print("Your inputed number is even")
    elif comparing(num) == False:
        print("Your inputed number is odd")
    else:
        print("Hmm... problems...")
main()#that is why we call main() in the end. 
# isn't this too long and more complicated?
#I got a better one 
def comparing(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
        
def main():
    num = int(input("Please input a number, I'll tell if it was an even or an odd: "))
    print(comparing(num))
    
main()

#I got even shorter version with main only
def main():
    num = int(input("Please input a number, I'll tell if it was an even or an odd: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
main()

#the even shorter version
def main():
    num = int(input("Please input a number, I'll tell if it was an even or an odd: "))
    print(f"Even" if num % 2 == 0 else "Odd")
main()
#I promise you it will work
#which one can you understand better and quicker?
#programming is hard but we want to do it better
#the point is that if you want to get better, you actually have to do it. it's like learning how to read as a kid, it's like learning how to eat and take talent.
#You will only be good at it when you are curious and keep typing code. Solve your errors. You fail, make another one as you tried to solve the problems.
#coding is more about journey. not build cool stuff. 

#learn from a youtube video how to code. you don't need me.     



