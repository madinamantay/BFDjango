import math
def f(a,b,c,d):
	return min(min(a,b),min(c,d))	
a,b,c,d = input().split()
print(f(a,b,c,d))