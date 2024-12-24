

#Creating the array
import numpy as npy
a=npy.array([1,2,3,4,5])
print(a)
#defining number of dimesnions
b=npy.array([1,2,3],ndmin=2)
print(b)
#check dimension of array
print("dimensions of array",b.ndim)



#Numpy indexing 1D 2D 3D Arrays
ar1=npy.array([1,2,3,4,5])
ar2=npy.array([[1,2,3,4,5],[1,2,3,4,5]])
ar3=npy.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('1st element',ar1[1])
print(ar3[1,0,1])
print(ar2[1,0])
print(ar1[-1])

#Slicing the array
import numpy as np1
a=np1.array([1,2,3,4,5,6,7])
print(a[:2])
arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[1:4])
print(arr[2:4])
print(arr[1:5:2])
print(arr[::2])

#Shape of an array
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr.shape)

#COPY AND View
import numpy as np
original_array = np.array([1, 2, 3])
x=original_array.copy()
x[0]=5
print(original_array)

#Iterating arrays
import numpy as np
arr = np.array(['a', 'b', 'c'])
for x in arr:
  print("Hello"+x)
arr=np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

#Split array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
new=np.array_split(arr,3)
print(new[0])

#numpy where
import numpy as np
arr = np.array([15, 38, 41, 46])
new=np.where(arr%2==1)
print(new)

#sorted array
import numpy as np
arr = np.array([True,False,True,False])
print(np.sort(arr))
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

#filter
import numpy as np
arr = np.array(['a', 'b', 'c'])
x=arr[[True,False,True]]
print(x)
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
filter=arr>3
print(filter)
import numpy as np
arr = np.array([7, 8, 9, 10])
filter = arr > 9
new=arr[filter]
print(new)