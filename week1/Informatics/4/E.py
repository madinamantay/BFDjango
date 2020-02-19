n = int(input())
a = input().split(' ')
s=True
for i in range(0,n-1):
	if (int(a[i+1])> 0 and int(a[i]) >0) or (int(a[i+1])< 0 and int(a[i])<0):
		s = False
if s == False:
	print("YES")
else:
	print("NO")
	