import numpy as np

arr = np.arange(20)
print("Numpy generated array = ",arr)

print("Current shape of array : ",arr.shape)
arr= arr.reshape(5,4)
print("\nReshaped the array to 5x4 \n",arr)

print("\nCurrent shape of array : ",arr.shape)
