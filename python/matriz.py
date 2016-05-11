#How make matrix

M = []
N = []
for i in range(5):
    M.append([0]*5)
    
for i in range(5):
    for j in range(5):
        M[i][j] = j**(i+1)
    
print "M is square matrix of size 5 x 5"
for i in range(5):
    N=[]
    for j in range(5):
        N.append(M[i][j])
    print N
    
print "Would you like choose number of matrix?"
print "1) yes\n 2) No"
quest = input ("Choose number\n") 
if quest == 1:
    print "You only typing row and column"
    row = input ("Write row (remember 1 to 5):\n")
    column = input ("Write column:\n")
    print row
    print column
    print "The position has number:\n"
    print M[(row -1)][(column -1)]    
elif quest == 2:
    print "Thank you, good bye"
else:
    print "Are you Stupid? only 1 or 2, jajajja"

print M
