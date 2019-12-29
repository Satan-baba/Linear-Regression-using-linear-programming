# Linear-Regression-using-linear-programming
Linear Regression using linear programming

This problem is based on the linear regression. It fits a linear function to data provided in dataLR.txt. The dataset contains N = 10000 rows and 11 columns(comma separated). The first column in every row i gives the label (yi) and the remaining 10 columns are
features (xi). 

In read.py, there is a code snippet that can read the dataLR.txt file in order to
populate arrays x and y, x being the 10000*10 array of features and y being the 10000 dimensional array of labels.

The python script myMatrixLpSolver:py provides a function lp optimize that
takes LP model in matrix notation and solves it (it also automatically writes the lp file).

The image file uploaded shows the two equations that are solved using this code. The Linear Program gives the extimates for Wi and b.
