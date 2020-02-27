

def fact(n):
	fact = 1
	for i in range(1,n+1): 
	    fact = fact * i 
	print ("The factorial of " + str(n) + " is : " + str(fact)) 


# Reading the value of n from input file
f = open("input.txt", "r")
for n in f:
  fact(int(n.strip()))
