import numpy

def neville(datax, datay, x):
    """
    Finds an interpolated value using Neville's algorithm.
    """
    n = len(datax)
    p = n*[0]
    for k in range(n):
        for i in range(n-k):
            if k == 0:
                p[i] = datay[i]
                print(datay[i])
            else:
                p[i] = ((x-datax[i+k])*p[i]+ \
                        (datax[i]-x)*p[i+1])/ \
                        (datax[i]-datax[i+k])
    return p[0]


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


if __name__ == '__main__':
    x = [8.1, 8.3, 8.6, 8.7]
    y = [16.9446, 17.56492, 18.50515, 18.82091]
    arr=[[0.35,0.4,0.55,0.65,0.7,0.85,0.9],[-213.5991,-204.4417,-194.9375,-185.0256,-174.6711,-163.8656,-152.6271]]
    while True:
        print('1 - linar 2 - polynomial 3 - lagrange 4 - neville')
        print('Enter number 5 to exit!')
        t1 = input('please select one: ')
        if(t1 == '1'):
            print(linearInterpolation(arr,0.75))
        if(t1 == '2'):
            print('working')
        if(t1 == '3'):
            print(lagrangeInterpolation(arr,0.75))
        if(t1 == '4'):
            print(neville(x, y, 8.4))
        if(t1 == '5'):
            break;
