n = int(input())
a = input().split(' ')
s=0
for i in range(0, n-2):
	if int(a[i+1])>int(a[i]) and  int(a[i+1])>int(a[i+2]):
		s = s+1
print(s)
