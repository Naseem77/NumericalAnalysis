import numpy
import math
import sympy as sp
from scipy.misc import derivative
#Naseem ali - 312343668 & artor mslti - 206327181

def Bisection(starPoint, endPoint, error, f):
    maxIterations=((-1)*math.log(error/(endPoint-starPoint),math.exp(1)))/math.log(2,math.exp(1))
    maxIterations=int(maxIterations+1)
    condition=True
    itr = 0
    while condition:
        c=(starPoint+endPoint)/2
        itr += 1
        if((f(starPoint)*f(c))>0):
            starPoint=c
        else:
            endPoint=c
        maxIterations=maxIterations-1
        condition = abs(f(c)) > error  and maxIterations > 0
    print('solution found after',itr, 'iterations')
    return c


def newton(f,start,end,e):
    xr = 4
    for n in range(start,end):
        fxr = f(xr)
        if abs(fxr) < e:
            print('solution found after',n, 'iterations')
            return xr
        xr = xr - fxr / derivative(f,xr)

def secant(f,a,b,e):
    x0=a
    x1=b
    for n in range(a, b):
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        if abs(f(x2)) < e:
            print('Found solution after',n, 'iterations.')
            return x2


if __name__ == '__main__':
    p = lambda x: x ** 2 - x * 5 + 2
    f = lambda x: (sp.cos(x**2+5*x+6))/(2*(math.exp(1)**(-x)))
    start = 0
    end = 20
    while True:
        print('1 - bisection 2 - newton 3 - secant')
        print('Enter number 4 to exit!')
        t1 = input('please select one: ')
        if(t1 == '1'):
            print(Bisection(-1.5,2,10**(-10),f))
        if(t1 == '2'):
            print(newton(p,start,end,0.0001))
        if(t1 == '3'):
            print(secant(p,start,end,0.0001))
        if(t1 == '4'):
            break;
