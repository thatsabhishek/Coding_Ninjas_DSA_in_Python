# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), 
# you need to convert all Fahrenheit values from Start to End at the gap of W, 
# into their corresponding Celsius values and print the table.
# Input Format : 3 integers - S, E and W respectively

# Input :
# 0 
# 100 
# 20
# Output :
# 0   -17
# 20  -6
# 40  4
# 60  15
# 80  26
# 100 37

def printTable(start,end,step):
	while end >= start:
		c = (5*(start-32))/9
		d = int(c)   
		print(start, d)
		start+=step

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)
