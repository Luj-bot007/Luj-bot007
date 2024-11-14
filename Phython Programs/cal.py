#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Owner
#
# Created:     10-07-2024
# Copyright:   (c) Owner 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
input ("Enter a number ")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    if b ==0:
      return ("ERROR")
    return a/b
def calcaulator():
print("Select any operation")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")