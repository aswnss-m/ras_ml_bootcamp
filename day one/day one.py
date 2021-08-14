'''
Pandas Functions
1. Series (lists)
2. Dataframe (dictionary)
3. read_csv('file location',seperator)
'''
import pandas as pd

state_names = ['Kerala','Karnataka','Tamil Nadu','Delhi']
states = pd.Series(state_names)
print(states)
# This makes the list as a pandas series data

population_number = [5000,40000,23000,10000]
population = pd.Series(population_number)
print(population)


state_dataset = pd.DataFrame({'STATES':states,'POPULATION':population})
print(state_dataset)

students = pd.read_csv('students.csv',sep=',')
print(students)

'''
describe()
head()
tail()
'''

print(students.describe()) #display various info about the dataset
print(students.head()) #print the top rows of the dataset head(number) 
print(students.tail()) #print the last rows of the dataset tail(number)


import matplotlib as plt

students.hist('Age')

'''
Why Numpy?
Numerical calculations made easy
'''

import numpy as np
import sys
list1 = range(100)
size_list1 = sys.getsizeof(list1[1])*len(list1)
print("memory size of the list : ",size_list1)

array1 = np.arange(100)
print("size of the array created by numpy : ",array1.size*array1.itemsize)
# numpy array takes less space

arr3 = np.array([[1,2,3],[2,3,5]])
print(arr3.shape) # returns the rows and column number
print(arr3.ndim) #return the dimension of the array 2d 3d

arr_1D = np.array([1,2,3,4,2])
print("original array : ",arr_1D)
print("arr_1D[2:3] : ",arr_1D[2:4])
