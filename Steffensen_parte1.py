import math

def f(x):
    return (x*x)-(2*x)-56

p0 = 0.7
tol = 0.0005
n0 = 10000

def Steffensen(f,p0,tol):
   
    for i in range(1,n0) :
        p1 = p0 + f(p0)
        p2 = p1 + f(p1)
        #print(pow((p2 - p1),2))
        #print(p2 - (2*p1) + p0)
        p = p2 - (pow((p2 - p1),2)/(p2 - (2*p1) + p0))
        #print(p-p0)
        if abs(p-p0) < tol:
            print("Converge despues de %f iteraciones"%i)
            return p
        p0 = p
    print('no se pudo converger en %f iteraciones' %n0)
    return p

ans = Steffensen(f,p0,tol)
print("value is: %f"%ans)

print("Checking Result: %f"%f(-6.549831825767762))