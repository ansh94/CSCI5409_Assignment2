  
def fibonacci(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibonacci(n-1) + fibonacci(n-2))  

  

  
# Reading the value of n from input file
f = open("input.txt", "r")
for n in f:
	inputN = int(n)
	a = 0
	b = 1
	print(a,b,end=" ")
	while(inputN - 2):
	    c = a + b
	    a,b = b,c
	    print(c, end=" ")
	    inputN = inputN-1

	print()


  