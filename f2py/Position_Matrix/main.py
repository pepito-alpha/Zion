#testing f2py

#import fortran module
from play import *


#code start
M = []
N = []
n = 0
for i in range(5):
    M.append([0]*5)
    
for i in range(5):
    for j in range(5):
        M[i][j] = j**(i+1)
print "============================================="    
print "M is square matrix of size 5 x 5"
print "============================================="
for i in range(5):
    N=[]
    for j in range(5):
        N.append(M[i][j])
    print N
print "============================================="    
print "\n"
print "============================================="    
print "Would you like choose number of matrix?"
print "1) yes"
print "2) No"
quest = input ("Choose number\n") 
if quest == 1:
    print "You only typing row and column"
    row = input ("Write row (remember 1 to 5):\n")
    column = input ("Write column:\n")
    print "============================================="
    print "            Python working                   "
    print "=============================================" 
    print "The position %i %i has number:\n"  %(row, column)
    print M[(row -1)][(column -1)]
    print "============================================="
    print "         Pyhon-Fortran working               "
    print "============================================="
    print "The position %i %i has number:\n"  %(row, column) 
    n = play.search(row, column, M)
    print n    
elif quest == 2:
    print "Thank you, good bye"
else:
    print "Are you Stupid? only 1 or 2, jajajaja"

print "============================================="
print "         Adiuu....               "
print "============================================="
