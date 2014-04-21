import bob
import math as m
np = bob.ip.numpy
pi = float('%.4f' %  m.pi)
pi2 = float('%.4f' % float(pi/2))
floor = m.floor


#given a specific index value of an element in the image of size sizexsize, returns which sector the element would belong in.
def findsector(index, size):
    N = size
    #determines column number
    x = index%N
    #determines row number
    y = floor(index/N)
    
    #sets center points to 0,0
    x = x - floor(N/2)
    y = y- floor(N/2)

    rad = (x*x)+(y*y)
    #print(rad)
    if rad <144:
        sector_num = 48
        return sector_num

    if rad >=8464:
        sector_num = 49
        return sector_num

    if x != 0:
        theta = m.atan(y/x)
    else:
        if y>0:
            theta = pi2
        else:
            theta = -pi2
    
    if x<0:
        theta = theta + pi
    else:
        if theta < 0:
            theta = theta+(2*pi)

    if theta < 0:
        theta = theta + (2*pi)

    r = floor(rad**.5)
    ring = floor((r-12)/20)
    arc = floor(theta/(pi/6))

    sector_num = (ring*12) + arc
    return sector_num
