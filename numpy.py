

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

#Universal Funtions arthimetic operations
import numpy as np
x = [2, 5, 5, 1]
y = [1, 4, 3, 1]
z = np.subtract(x, y)

#Universal Funtions rounding decimals
import numpy as np
arr = np.trunc([5.998, 1.455])
print(arr)
import numpy as np
arr = np.around(5.93)
print(arr)
import numpy as np
arr = np.ceil([5.998, 1.455])
print(arr)

#datatypes
import numpy as np
arr = np.array([-1, 0, 1])
newarr = arr.astype(bool)
print(newarr)
arr = np.array([1, 2, 3, 4])
print(arr.dtype)
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.
astype('i')


#reshape array
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(6)
print(newarr)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
arr = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
newarr = arr.reshape(-1)

#ufunc logs
log2()  --> #preform log at base 2
log10() --> # perform log at base 10
log()   --> #perform log at base e

#ufunc summations
import numpy as np
arr1 = np.array([5, 1, 2])
arr2 = np.array([3, 2, 2])
newarr = np.sum([arr1, arr2])
import numpy as np
arr1 = np.array([5, 1, 2])
arr2 = np.array([3, 2, 2])
newarr = np.sum([arr1, arr2], axis=1)
import numpy as np
arr1 = np.array([5, 1, 2])
newarr = np.cumsum(arr1)
#ufunc product
import numpy as np
arr1 = np.array([5, 2, 3])
newarr = np.prod(arr1)
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 2, 1])
newarr = np.prod([arr1, arr2], axis=1)
newarr = np.sum([arr1, arr2], axis=1)
import numpy as np
arr = np.array([1, 2, 3])
newarr = np.cumprod(arr)
# ufunc differences
import numpy as np
arr = np.array([1, 2, 3, 4])
newarr = np.diff(arr)
import numpy as np
arr = np.array([5, 7, 3, 4])
newarr = np.diff(arr)
import numpy as np
arr = np.array([1, 2, 3, 4])
newarr = np.diff(arr, n=2)
# U func lcm
import numpy as np
num1 = 4
num2 = 6
x = np.lcm(num1, num2)

#Trionometric 
np.pi / 180 * 50 --> convert 50 degrees into radians
np.hypot() -->  finding the hypotenues

#Hyperbolic
np.sinh() -->  finding the hyperbolic sine value
np.tanh() -->  finding the hyperbolic tan value
np.cosh() -->  finding the hyperbolic cos value

# random distribution
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5)) --> 2d array

