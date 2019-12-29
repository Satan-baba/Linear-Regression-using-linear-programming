import sys
from gurobipy import *
from myMatrixLpSolver import lp_optimize


# Open a file
f = open('dataLR.txt', 'r')
N=10000
C=10
x = [[0 for j in range(C)] for i in range(N)] 
y = [0 for i in range(N)] 
# Loop over lines and extract variables of interest
i=-1
for line in f:
		i=i+1
		line = line.strip()
		columns = line.split(',')
		y[i]=float(columns[0])
		for j in range(0,10):
			x[i][j] = float(columns[j+1])

f.close()



############ Write you code from here #################

# Put model data into matrices/vectors and call lp_optimize







