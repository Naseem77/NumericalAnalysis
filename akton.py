import math
from random import randint
import numpy
from scipy.misc import derivative
import sympy as sp
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

def biggerBisection(starPoint, endPoint, error, f, jumpPoint):
    answer=[]
    x=starPoint
    itr=0
    while x < endPoint - jumpPoint:
        itr+=1
        if(f(x)* f(x + jumpPoint) <0):
            res = Bisection(x, x + jumpPoint, error, f)

            if (-0.000001 <= f(res) and f(res) <= 0.000001):
                answer.append(res)
        x=x+jumpPoint
    return answer
def trapez(f, a, b, n):
    h = (b - a) / n
    x = a
    s = f(a)
    for k in range(1, n):
        x  = x + h
        s += 2*f(x)
    return (s + f(b))*h*0.5
def romberg(f, a, b, n):
    matrix = numpy.zeros((n, n))
    for k in range(0, n):
        matrix[k, 0] = trapez(f, a, b, 2**k)
        for j in range(0, k):
            matrix[k, j+1] = (4**(j+1) * matrix[k, j] - matrix[k-1, j]) / (4**(j+1) - 1)
    return matrix

def simpson(f, a, b, n):
    h=(b-a)/n
    k=0.0
    x=a + h
    itr=0
    for i in range(1,int(n/2) + 1):
        k += 4*f(x)
        x += 2*h
        print("4*f(x):%.6f x: %.6f  i: %.f" % (k,x,itr))
        itr+=1
    x = a + 2*h
    for i in range(1,int(n/2)):
        k += 2*f(x)
        x += 2*h
        print("2*f(x):%.6f x: %.6f  i: %.f" % (k, x, itr))
        itr += 1
    return (h/3)*(f(a)+f(b)+k)
def isDm(arr,n):
    """Checking the len of arr, return true if less then 3, otherwise false"""
    for i in range(0, n):
        count = 0
        for j in range(0, n):
            count = count + abs(arr[i][j])
        count = count - abs(arr[i][i])
        if (abs(arr[i][i]) < count):
            return False
    return True

def jacobi(arr,e):
    """Jacobi function which accept the array and the e=0.0001, then returns x,y,z and prints x,y,z"""
    if(isDm(arr,3)):
        func1 = lambda x, y, z: (arr[0][3] - arr[0][1] * y - arr[0][2]) / arr[0][0]
        func2 = lambda x, y, z: (arr[1][3] - arr[1][0] * x - arr[1][2] * z) / arr[1][1]
        func3 = lambda x, y, z: (arr[2][3] - arr[2][0] * x - arr[2][1] * y) / arr[2][2]

        x0 = 0
        y0 = 0
        z0 = 0
        itr = 0
        flag = True
        while flag:
            x1 = func1(x0, y0, z0)
            y1 = func2(x0, y0, z0)
            z1 = func3(x0, y0, z0)
            e1 = abs(x0 - x1);
            e2 = abs(y0 - y1);
            e3 = abs(z0 - z1);
            itr += 1
            x0 = x1
            y0 = y1
            z0 = z1
            flag = e1 > e and e2 > e and e3 > e
        print("x:",x1,"y:",y1,"z:",z1)
        return [x1, y1, z1]
    else:
        print('Its not Diagonally Dominant Matrix ')
def gaussSeidel(arr,e):
    """gauss function which accept the array and the e=0.0001, then returns x,y,z cheks if the len of the array by isDm function, plus returns error message if len is uncorret"""
    if (isDm(arr, 3)):
        func1 = lambda x, y, z: (arr[0][3] - arr[0][1] * y - arr[0][2]) / arr[0][0]
        func2 = lambda x, y, z: (arr[1][3] - arr[1][0] * x - arr[1][2] * z) / arr[1][1]
        func3 = lambda x, y, z: (arr[2][3] - arr[2][0] * x - arr[2][1] * y) / arr[2][2]
        x0 = 0
        y0 = 0
        z0 = 0
        itr = 0
        flag = True
        while flag:
            x1 = func1(x0, y0, z0)
            y1 = func2(x1, y0, z0)
            z1 = func3(x1, y1, z0)

            e1 = abs(x0 - x1);
            e2 = abs(y0 - y1);
            e3 = abs(z0 - z1);

            x0 = x1
            y0 = y1
            z0 = z1
            itr += 1
            flag = e1 > e and e2 > e and e3 > e

        return [x1,y1,z1]
    else:
        print('Its not Diagonally Dominant Matrix ')

def lagrangeInterpolation(arr,point):
    """
    Finds an interpolated value using lagrange's algorithm.
    """
    answ = 0
    for i in range(len(arr[0])):
        x = 1
        for j in range(len(arr[0])):
            if i != j:
                x = x * (point - arr[0][j]) / (arr[0][i] - arr[0][j])
        answ = answ + x * arr[1][i]
        print(answ)
    return (answ)
"""
Finds an interpolated value using linear's algorithm.
"""
def linearInterpolation(arr,point):##done
    for i in range(0,len(arr[0])-1):
        if(arr[0][i]<= point and point<=arr[0][i+1]):
            saveIndex=i
            break
    fx=lambda x1,y1,x2,y2,point: (y1-y2)/(x1-x2)*point+(y2*x1-y1*x2)/(x1-x2)
    return fx(arr[0][saveIndex],arr[1][saveIndex],arr[0][saveIndex+1],arr[1][saveIndex+1],point)

'''func1 refer to question number 1, func2 refer to question number 2, etc.'''
def get_random_val(x):
    random=int(time.time()*1000)
    random %= x
    res = (random%10)
    if(res == 1 or res == 2):
        print('func1 working')
    if(res == 3):
        print('func2 working')
    if(res == 4 or res == 5):
        print('func3 working')
    if(res == 6):
        print('func4 working')
    if(res == 7 or res == 8):
        print('func5 working')
    if(res == 9):
        print('func6 working')

x=int(input('Enter your ID:'))

print(get_random_val(x))
f = lambda x: (x*(math.exp(1)**(-x**2-5*x-3)))*(3*x-1)
p_rows = 7
res = romberg(f,0,1.5,p_rows)
solution = res[p_rows - 1, p_rows - 1]
print("romberg result:",solution)
p = lambda x: x ** 2 - x * 5 + 2
f = lambda x: (sp.cos(x**2+5*x+6))/(2*(math.exp(1)**(-x)))
start = 0
end = 20
print(Bisection(-1.5,2,10**(-10),f))
print(newton(p,start,end,0.0001))
print(secant(p,start,end,0.0001))
arr=[[0.35,0.4,0.55,0.65,0.7,0.85,0.9],[-213.5991,-204.4417,-194.9375,-185.0256,-174.6711,-163.8656,-152.6271]]
print(linearInterpolation(arr,0.75))
print(lagrangeInterpolation(arr,0.75))
e = 0.0001
arr1 = [[10, 8, 1, -7], [4, 10, -5, 2], [5, 1, 10, 1.5]]
jacobi(arr1, e)
gaussSeidel(arr1, e)
e = 0.0001
arr2 =[[0.04, 0.01, -0.01, 0.06],[0.2, 0.5, -0.2, 0.3],[1, 2, 4, 11]]
jacobi(arr2, e)
gaussSeidel(arr2, e)
