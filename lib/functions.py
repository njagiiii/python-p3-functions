#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

def greet(name="Guido"):
    print(f"Hello, {name}!")
    
greet()

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    
greet_with_default()

def add(num1, num2):
    return num1 + num2
number = add(45 ,55)
print(number)

def halve(number):
   if not isinstance(number, (int, float)):
       raise ValueError('Wrong input')
   else:
       return number / 2
      
   
               
   
try:
       num =50
       result = halve(num)
       print(result)

except Exception as e :
    print(e)

