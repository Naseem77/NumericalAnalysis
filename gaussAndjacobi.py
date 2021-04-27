#Naseem Ali
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


e = 0.0001
arr1 = [[10, 8, 1, -7], [4, 10, -5, 2], [5, 1, 10, 1.5]]
jacobi(arr1, e)
gaussSeidel(arr1, e)

e = 0.0001
arr2 =[[0.04, 0.01, -0.01, 0.06],[0.2, 0.5, -0.2, 0.3],[1, 2, 4, 11]]
jacobi(arr2, e)
gaussSeidel(arr2, e)
