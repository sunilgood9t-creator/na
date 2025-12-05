import numpy as np
def simpson_double(f,a,b,c,d,nx,ny):
    if nx%2!=0 or ny%2!=0:
        raise ValueError ("both nx and ny must be even for simpson rule:")
    h_x = (b-a)/nx
    h_y = (d-c)/ny
    total = 0
    for i in range(nx+1):
        x = a+i*h_x
        wx=1
        if i==0 or i==nx:
            wx=1
        elif i%2==1:
            wx=4
        else:
            wx=2
    for j in range(ny+1):
        y =c+j*h_y
        wx=1
        if j==0 or j==ny:
            wy = 1
        elif j%2==1:
            wy=4

        else:
            wy=2
    total+= wx*wy*f(x,y)
    return((nx*ny/9)*total)
f = lambda x,y : x**2 + y**2 +2
result = simpson_double(f,0,1,0,1, nx=6 , ny =6)
print("approx integral",result)


   
