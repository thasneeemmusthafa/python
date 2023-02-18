n=int(input("Enter the number:"))
sum=0
for i in range(1,n):
	if(n%i==0):
		print(i,"is a factor of",n)

		sum=sum+i

if(sum==n):
	print("Perfect number")
else:
	print("Not perfect number")