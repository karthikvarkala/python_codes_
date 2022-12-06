# -*- coding: utf-8 -*-
"""Lambda funtion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18q4JgzM653yVgw-vvr1VAvWIWQnfcedV
"""

''' A lambda function is an anonymous function (i.e., defined without
 a name) that can take any number of arguments but, unlike normal functions,
  evaluates and returns only one expression. '''


  # square of number using lambda funtion
  #3square
f=lambda a : a*a
result=f(3)
print(result)

# addition of two numbers
f=lambda a,b :a+b
result=f(3,5)
print(result)

#multiplication of two numbers
f=lambda a,b :a*b
result=f(3,5)
print(result)

# max value
mx =lambda x,y: x if x>y else y
print(max(8,6))

#lambda funtion to get the values greater then 2 in list
n=[4,3,5,2,1,0]
print(list(filter(lambda x : x>=2,n)))

