# -*- coding: utf-8 -*-
"""multipleways of creating arrays.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P6cQah8diU2CfvunMRHUYI40S0FpyyX4
"""

from numpy import*
arr=array([1,2,3,4,5.8,6],int)
print(arr.dtype)
print(arr)

"""#linespace"""

arr=linspace(0,15,16)
print(arr)

"""#arange"""

arr=arange(1,15,2)
print(arr)

"""#logspace

"""

arr=logspace(1,40,5)
print(arr)

"""#zeros"""

# arr=zeros(7)
arr=ones(5,int)
print(arr)

#adding 5 to array
# each number is added with 5in array
arr=array([1,2,3,4,5,6])
print(arr)
arr=arr+5
print(arr)

# adding two arrays
arr1=array([1,2,3,4,5,6])
arr2=array([6,5,4,3,2,1,])
arr=arr1+arr2
print(arr)

"""#concatenate"""

arr1=array([1,2,3,4,5,6])
arr2=array([6,5,4,3,2,1])
print(concatenate([arr1,arr2]))

"""#sin,cos,tan,log,sqrt,min,max,sort,unique,"""

arr=array([1,2,3,4,5,6])
print(sqrt(arr))
print(sin(arr))
print(tan(arr))
print(sum(arr))
print(cos(arr))

"""#Coping array"""

arr1=array([1,2,3,4,5,6])
arr2=arr1
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

"""###shalow copy"""

arr1=array([1,2,3,4,5,6])
arr2=arr1.view()
arr1[1]=7
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

"""#Deep copy"""

arr1=array([1,2,3,4,5,6])
arr2=arr1.copy()
arr1[1]=7
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

