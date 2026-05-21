import numpy as np

array = np.array([1,2,3,4])



array = array * 2
print(array)

print(type(array))


#multidimensional


arrays = np.array([["A" , "B" , "C"],
                   ["D" , "E" , "F"],
                   ["H" , "H" , "I"]])


print(arrays.ndim)

print(arrays.shape)

print(type(arrays))