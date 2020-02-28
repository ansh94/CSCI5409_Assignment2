#!/usr/bin/env python3
import csv
import time

fib_results = open("fib_results.csv", 'w+', encoding='utf-8')
headings = "Request Id,time,N,Result\n"
fib_results.write(headings)
  

  
# Reading the value of n from input file
f = open("input.txt", "r")
rId = 1
for n in f:
	start = time.time()

	strN = str(n)
	fibResult = []

	inputN = int(n)
	a = 0
	b = 1
	print(a,b,end=" ")
	fibResult.append(a)
	fibResult.append(b)
	while(inputN - 2):
	    c = a + b
	    a,b = b,c
	    print(c, end=" ")
	    fibResult.append(c)
	    inputN = inputN-1

	strArray = ''.join(str(e) for e in fibResult)

	stop = time.time()
	duration = stop - start
	row = str(rId) + ',' + str(duration)[:-13] + ',' + str(int(n)) + ',' + strArray +  '\n'
	fib_results.write(row)
	rId = rId + 1


	print()


  