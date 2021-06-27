#successive over-relaxation

#Defining equations
#Diagonally dominant form
func1 = lambda x,y,z: (-1+y-z)/3
func2 = lambda x,y,z: (7+x+z)/3
func3 = lambda x,y,z: (-7-x+y)/3
#initial
x0 = 0
y0 = 0
z0 = 0
count = 1
#Getting tolerable error
te = float(input('Enter error: '))
#Getting relaxation
re = float(input("Enter relaxation: "))

#implementation successive over-relaxation
flag = True

while flag:
    x1 = (1 - re) * x0 + re * func1(x0,y0,z0)
    y1 = (1 - re) * y0 + re * func2(x1,y0,z0)
    z1 = (1 - re) * z0 + re * func3(x1,y1,z0)
    print('%d ->\tx= %f\ty= %f\tz= %f\n' %(count,x1, y1, z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    flag = e1>te and e2>te and e3>te

print('\nSolution: x = %f, y = %f and z = %f\n'% (x1,y1,z1))
