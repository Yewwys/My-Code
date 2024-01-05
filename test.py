import numpy as np 
#Truss

def truss(d1,d2,F1,F2):
    z = np.arctan(d1/d2)
    A = np.array([[np.sin(z),0,0,0,0,0,1,0],
                  [np.cos(z),1,0,0,0,1,0,0],
                  [0,0,1,0,0,0,0,0],
                  [0,-1,0,1,0,0,0,0],
                  [0,0,0,0,np.sin(z),0,0,1],
                  [0,0,0,-1,-np.cos(z),0,0,0],
                  [-np.sin(z),0,-1,0,-np.sin(z),0,0,0],
                  [-np.cos(z),0,0,0,np.cos(z),0,0,0]]
                  )
    b = np.array([0,0,F1,0,0,0,0,-F2])
    x = np.linalg.solve(A,b)
    print(f"T2 = {x[1]:.2f}")
    return x
ans = truss(1.5, 2, 3, 0)
if not isinstance(ans, np.ndarray):
    raise ValueError('You have to use Numpy for this question')
print(ans)
