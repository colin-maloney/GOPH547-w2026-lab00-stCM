from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt 


array_1 = np.ones((3, 5)) 

array_2 = np.zeros((6, 3)) 

array_3 = np.arange(44, 75, 2).reshape(-1,1) 

array_3_sum = np.sum(array_3) 

array_4 = [[5, 7, 2],[1, -2, 3], [4, 4, 4]] 

array_5 = np.identity(3)  

array_6 = np.multiply(array_4, array_5) 

dot_product = np.dot(array_4, array_5) 

cross_product = np.cross(array_4, array_5)

# print("Array 1:\n", array_1)
# print("Array 2:\n", array_2)
# print("Array 3:\n", array_3)
# print("Sum of Array 3:", array_3_sum)
# print("Array 4:\n", array_4)
# print("Array 5:\n", array_5) 
# print("Array 6 (Element-wise multiplication of Array 4 and Array 5):\n", array_6)
# print("Dot Product of Array 4 and Array 5:\n", dot_product) 
# print("Cross Product of Array 4 and Array 5:\n", cross_product) 

rock_canyon = np.asarray(Image.open('src/goph547lab00/rock_canyon.jpg'))
img = plt.imshow(rock_canyon)
plt.show() 
rock_canyon_shape = rock_canyon.shape 
print("Rock Canyon Image Shape:", rock_canyon_shape) 

row, cols, _ = rock_canyon.shape 

center_col = cols // 2   
center_row = row // 2
collum_col = center_col - 112 

col_slice = rock_canyon[:, collum_col-10:collum_col + 10, :]

small_gray_img = np.dot(col_slice[...,:3], [0.2989, 0.5870, 0.1140]) 
plt.imshow(small_gray_img, cmap='gray')
plt.show()

y = np.arange(cols) 
x = np.arange(row) 

row_data = rock_canyon[center_row, :, :] 
col_data = rock_canyon[:, center_col, :] 

fig, axs = plt.subplots(1, 2, figsize=(12, 5)) 




# subplot for row data 
axs[0].plot(y, row_data[:, 0], color='red', label='Red') 
axs[0].plot(y, row_data[:, 1], color='green', label='Green') 
axs[0].plot(y, row_data[:, 2], color='blue', label='Blue') 
axs[0].set_title('Row Data at Center Row')
axs[0].set_xlabel('x-coordinate')
axs[0].set_ylabel('RGB colour') 
axs[0].legend() 

# subplot for column data 
axs[1].plot(x, col_data[:, 0], color='red', label=' Red') 
axs[1].plot(x, col_data[:, 1], color='green', label=' Green') 
axs[1].plot(x, col_data[:, 2], color='blue', label=' Blue') 
axs[1].set_title('Column Data at Center Column')    
axs[1].set_xlabel('y-coordinate')
axs[1].set_ylabel('RGB colour') 
axs[1].legend() 

plt.tight_layout() 
plt.show()