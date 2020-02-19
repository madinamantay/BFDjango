n = int(input())
a = input().split(' ')
s=0
for i in range (n):
	if int(a[i])>0:
		s+=1
print(s)
	