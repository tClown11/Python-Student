import numpy as np

'''import numpy as np
from numpy.eandom import randon
data = {i : randon() for i in range(7)}
print(data)'''


'''import sys
import array
numbers = arrary('h',[-2,-1,0,1,2])
octets = bytes(numbers)
print(octets)'''



'''import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr.dtype)
'''


'''
import numpy as np
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)
print(arr.astype(np.int32))
numeric_strings = np.array(['1.25', '-9.6', '342'], dtype = np.string_)
print(numeric_strings.astype(float))'''


'''
import numpy as np
int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype = np.float64)
print(int_array.astype(calibers.dtype))
empty_unit32 = np.empty(8, dtype = 'u4')
print(empty_unit32)'''


'''arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr*arr)
print(arr-arr)
print(1/arr)
print(arr ** 0.5)'''

'''arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])
arr[5:8] = 12
print(arr)'''

'''arr = np.arange(10)
arr_slice = arr[5:8]
arr_slice[1] = 12345
print(arr)
arr_slice[:] = 64
print(arr)
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])
print(arr2d[0][2])
print(arr2d[0,2])'''

'''
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])
old_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)
arr3d[0] = old_values
print(arr3d)
print(arr3d[1, 0])#arr3d[1, 0]可以访问索引以（1， 0）开头的那些值（以一维数组的形式返回）
#注意：在上面所有这些选取数组子集的例子中，返回的数组都是视图'''


#切片索引
#注意：“只有冒号”表示选取整个轴
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[:2])
print(arr2d[:2, 1:])
print(arr2d[1, :2])
print(arr2d[2, :1])
print(arr2d[1:,:])
print(arr2d[1, :])
print(arr2d[:1,:])