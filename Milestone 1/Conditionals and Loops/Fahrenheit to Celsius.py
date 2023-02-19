# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), 
# you need to convert all Fahrenheit values from Start to End at the gap of W, 
# into their corresponding Celsius values and print the table.

S = int(input())
E = int(input())
W = int(input())

while E >= S:
    c = (5*(S-32))/9
    d = int(c)
    print(S, d)
    S = S+W
