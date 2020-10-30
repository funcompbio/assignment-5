import numpy as np

## define here below this comment a function
## called 'f()' that calculates the value of
## the differential equation of the system
## for values of variables and constants given
## through its function arguments
## begin function 'f()'


## end function 'f()'

## define here below this comment a function
## called 'euler()' that performs the numerical
## integration of the previous function 'f()'
## using Euler's method
## begin function 'euler()'


## end function 'euler()'

## this 'main()' function takes two arguments 'rho' and
## 'alpha', which are constants associated to the system
## and return the solutions of the system for a given
## set of time points. DO NOT EDIT THE NEXT LINE
def main(t, rho, alpha) :

	## DO NOT EDIT THE NEXT TWO LINES
	## initial value
	I0 = 0.001

	## REPLACE THIS AND THE NEXT TWO LINES
	## by a proper call to the 'euler()' function
	I = t

	## DO NOT EDIT THE NEXT LINE
	return(I)

## DO NOT EDIT THESE LINES TILL THE END OF THE SCRIPT
if __name__ == "__main__" :
	import sys

	if (len(sys.argv) != 3) :
		print("error: sir.py <rho> <alpha>")
	else :
		## set time points between 0 and 30 in steps (h) of 1
		t = np.arange(0, 30, 1)

		## call the 'main()' function
		I = main(t, float(sys.argv[1]), float(sys.argv[2]))

		## print resulting values for each time point
		print("t,dI")
		i = 0
		while (i < len(I)) :
			print("%.3f,%.3f" %(t[i], I[i]))
			i = i + 1