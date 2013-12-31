'''
12/31/2013
Author: Joshua Milas
Python Version: 3.3.2

The Jacchia 77 atmospheric model ported to python
based off of the j77sri.for from nasa at
http://nssdcftp.gsfc.nasa.gov/models/atmospheric/jacchia/jacchia-77/

This is the test program that generates a similar output to testj77.for
Note, this output will not match the exact output since there are rounding differences
C*********************************************************************C
C*                                                                   *C
C*  testj77.for                                                      *C
C*                                                                   *C
C*  Written by:  David L. Huestis, Molecular Physics Laboratory      *C
C*                                                                   *C
C*  Copyright (c) 1999  SRI International                            *C
C*  All Rights Reserved                                              *C
C*                                                                   *C
C*  This software is provided on an as is basis; without any         *C
C*  warranty; without the implied warranty of merchantability or     *C
C*  fitness for a particular purpose.                                *C
C*                                                                   *C
C*********************************************************************C
C*
C*	Main program to test j77sri.for
C*
C*	The user should choose values of mz (maximim altitude in km)
C*	and Tinf (exospheric temperature in K).
C*
C*	Number densities are listed as log10( molecules/cubic-meter )
C*
C*  EDIT HISTORY:
C*
C*	10-10-99  DLH	Original testj77.for
C*
C*	09-xx-99  DLH	various test versions
C*
C**********************************************************************
'''
from j77sri import *
from math import *
mz = 2500
Tinf = 1000


'''z = [0 for _ in range(mz)]
T = [0 for _ in range(mz)]
CM = [0 for _ in range(mz)]
WM = [0 for _ in range(mz)]
CN2 = [0 for _ in range(mz)]
CO2 = [0 for _ in range(mz)]
CO = [0 for _ in range(mz)]
CAr = [0 for _ in range(mz)]
CHe = [0 for _ in range(mz)]
CH = [0 for _ in range(mz)]
'''
v = [0 for _ in range(7)]

test = j77sri(mz, Tinf)

def printStuff(i):
    for j in range(2,9):
        if( test[j][i] > 1.26E-16):
            test[j][i] = log10(test[j][i]) + 6
        else:
            test[j][i] = -9.9
    print(str(i).rjust(4), end='')
    print('%8.2f'.rjust(4) % test[1][i], end='')
    print('%8.4f'.rjust(4) % test[2][i], end='')
    print('%8.4f'.rjust(4) % test[3][i], end='')
    print('%8.4f'.rjust(4) % test[4][i], end='')
    print('%8.4f'.rjust(4) % test[5][i], end='')
    print('%8.4f'.rjust(4) % test[6][i], end='')
    print('%8.4f'.rjust(4) % test[7][i], end='')
    print('%8.4f'.rjust(4) % test[8][i], end='')
    print('%7.3f'.rjust(4) % test[9][i])
    #print('%d %2.4f %2.4f %2.4f %2.4f %2.4f %2.4f %2.4f %2.4f %2.4f' % ( i,
    #        test[1][i], test[2][i], test[3][i], test[4][i], test[5][i],
    #      test[6][i], test[7][i], test[8][i], test[9][i]))
    

for i in range(0, mz+1):
    if(i <= 80):
        if not(i % 5):
            printStuff(i)
            
    elif(i <= 100):
        printStuff(i)
        
    elif(i <= 110):
        if not(i % 2):
            printStuff(i)
            
    elif(i <= 160):
        if not(i % 5):
            printStuff(i)

    elif(i <= 400):
        if not(i % 10):
            printStuff(i)

    elif(i <= 1000):
        if not(i % 20):
            printStuff(i)

    elif(i <= 1500):
        if not(i % 50):
            printStuff(i)

    else:
        if not(i % 100):
            printStuff(i)



def printStuff(i):
    for j in range(2,9):
        if( test[j][i] > 1.26E-16):
            test[j][i] = log10(test[j][i]) + 6
        else:
            test[j][i] = -9.9
    print('%d %2.4f %2.4f %2.4f %2.4f %2.4f %2.4f %2.4f %2.4f %2.4f' % ( i, test[1][i], test[2][i], test[3][i], test[4][i], test[5][i],
          test[6][i], test[7][i], test[8][i], test[9][i]))
