import math

def f(x):
    return (2*x*x)+(9*x)-100 #la ecuacion aca


p0 = 0.5 #aproximacion inicial
tol = 0.0001 #tolerancia
n0 = 10000 #max de iteraciones

def Steffensen(f,p0,tol):
   
    for i in range(1,n0) :
        p1 = p0 + f(p0)
        p2 = p1 + f(p1)
        #print(pow((p2 - p1),2))
        print(p2 - (2*p1) + p0)
        p = p2 - (pow((p2 - p1),2)/(p2 - (2*p1) + p0))
        #print(p-p0)
        if abs(p-p0) < tol:
            print("Converge despues de %f iteraciones"%i)
            return p
        p0 = p
    print('no se pudo converger en %f iteraciones' %n0)
    return p

ans = Steffensen(f,p0,tol)
print("valor es: %f" %ans)