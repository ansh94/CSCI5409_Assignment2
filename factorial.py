#!/usr/bin/env python3
import csv
import time


fact_results = open("fact_results.csv", 'w+', encoding='utf-8')
headings = "Request Id,time,N,Result\n"
fact_results.write(headings)



def fact(n,rId):
	start = time.time()
	fact = 1
	for i in range(1,n+1): 
	    fact = fact * i 
	print (str(fact)) 
	stop = time.time()
	duration = stop - start
	row = str(rId) + ',' + str(duration)[:-15] + ',' + str(n) + ',' + str(fact) +  '\n'
	fact_results.write(row)



# Reading the value of n from input file
f = open("input.txt", "r")
rId = 1
for n in f:

  fact(int(n.strip()),rId)
  rId = rId + 1


