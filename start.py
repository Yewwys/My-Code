import numpy as np 
ar1 = np.array([[43,335,11,46],
    [32 ,11 ,32 ,56],
    [10 ,9 ,8 ,7]])
ar2 = np.array([[99, 235 ,110  ,26],
 [245 ,55 ,23 ,18],
 [13 ,67 ,9 ,10]])
sm = ar1+ar2
sum_result = np.sum(sm,axis=0)
print(f"This is max result of sum == {max(sum_result)}")

a1r = ar1.reshape(2,6)

array1T = ar1.T

mult_result = np.dot(array1T,ar2).mean()

print(f"This is the matrix multiplication of Transpored array1 and array2 == {mult_result}")