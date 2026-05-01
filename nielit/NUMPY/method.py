import numpy as np
arr2=np.array([[1,2,3],[4,5,6]])
arr3=np.array([[[88,99],[44,55]],[[00,88],[33,55]]])

# shape: tells you the size of each dimensions like row Aand cloumn
# ndim: tell you how many dimensions the array has
# dtype: shows the type of data in the array
# size: total number of elements present in the array
# itemsize: how many bytes take each element in the array

#Type conversion
new_arr=arr2.astype(float)
print("2D Array")
print(arr2)
print("shape",arr2.shape)
print("No. of dimension: ",arr2.ndim)
print("No of element in array: ",arr2.size)
print("type of the element in array: ",arr2.dtype)
print("No. of bytes take each element: ",arr2.itemsize)
print("type of the element in New array: ",new_arr.dtype)

print("3D Array")
print(arr3)
print("shape",arr3.shape)
print("No. of dimension: ",arr3.ndim)
print("No of element in array: ",arr3.size)
print("type of the element in array: ",arr3.dtype)
print("No. of bytes take each element: ",arr3.itemsize)