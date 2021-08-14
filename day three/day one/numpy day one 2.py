import numpy as np

arr1 = np.random.rand(5,4)
arr2 = np.random.rand(5,4)

print("First Array :\n",arr1)
print("\nSecond Array :\n",arr2)

sum = arr1+arr2
print("\nSum of first and second\n",sum)
mean_0 = sum.mean(axis=0)
mean_1 = sum.mean(axis=1)
print("\nMean of each columns : \n",mean_0)
print("\nMean of each rows : \n",mean_1)