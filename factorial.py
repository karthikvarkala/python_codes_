# -*- coding: utf-8 -*-
"""Factorial

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1135FXWENtu0ORQshjMRp1VROQoGSTIA1
"""

'''Factorial of a non-negative integer, is multiplication of all integers
 smaller than or equal to n.For example factorial of 6 is 6*5*4*3*2*1 which is 720.'''

# python code for factorial
# here x will take the value of whic you want to get the factorial
x=6 
a=1
for i in range(1,x+1):
  a=a*i
print(x,"factorial value is",a)

"""using function

"""

#here we are asking user to enter the number, for which they want to know the value of factorial
n=int(input("enter the number"))
# defining the funtion 
def fact(n):
  f=1
  for i in range(1,n+1):
    f=f*i
  print(n,"factorial value is",f)
#calling the function
fact(n)

"""Factorial using Recursion"""

#Recursion is the technique of making a function call itself.
def fact(n):
  if n==0:
    return 1
  return n * fact(n-1)
#calling the function
fact(5)
