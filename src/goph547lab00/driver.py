import numpy as np 

array_1 = np.ones((3, 5)) 

array_2 = np.zeros((6, 3)) 

array_3 = np.arange(44, 75, 2).reshape(-1,1) 

array_3_sum = np.sum(array_3) 

array_4 = [[5, 7, 2],[1, -2, 3], [4, 4, 4]] 

array_5 = np.identity(3)  

array_6 = np.multiply(array_4, array_5) 

dot_product = np.dot(array_4, array_5) 

cross_product = np.cross(array_4, array_5)

print("Array 1:\n", array_1)
print("Array 2:\n", array_2)
print("Array 3:\n", array_3)
print("Sum of Array 3:", array_3_sum)
print("Array 4:\n", array_4)
print("Array 5:\n", array_5) 
print("Array 6 (Element-wise multiplication of Array 4 and Array 5):\n", array_6)
print("Dot Product of Array 4 and Array 5:\n", dot_product) 
print("Cross Product of Array 4 and Array 5:\n", cross_product)