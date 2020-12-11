# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 23:31:37 2020

@author: Charya
"""
# Python program for simple calculator 
  
# Function to add two numbers  
def add(num1, num2, num3): 
    return num1 + num2 +num3
  
# Function to subtract two numbers  
def subtract(num1, num2): 
    return num1 - num2 - num3
  
# Function to multiply two numbers 
def multiply(num1, num2, num3): 
    return num1 * num2 * num3
  
# Function to divide two numbers 
def divide(num1, num2, num3): 
    return num1 / num2 / num3
  
print("Please select operation -\n" 
        "1. Add\n"  
        "2. Subtract\n"  
        "3. Multiply\n"  
        "4. Divide\n")
  
  
# Take input from the user  
select = int(input("Select operations form 1, 2, 3, 4 :")) 
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 
number_3 = int(input("Enter third number: "))   
if select == 1: 
    print(number_1, "+", number_2, "+", number_3, "=", 
                    add(number_1, number_2, number_3)) 
  
elif select == 2: 
    print(number_1, "-", number_2, "-", number_3, "=", 
                    subtract(number_1, number_2, number_3)) 
  
elif select == 3: 
    print(number_1, "*", number_2, "*", number_3, "=", 
                    multiply(number_1, number_2, number_3)) 
  
elif select == 4: 
    print(number_1, "/", number_2, "/", number_3, "=", 
                    divide(number_1, number_2, number_3)) 
else: 
    print("Invalid input") 
