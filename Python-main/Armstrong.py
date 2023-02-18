n=int(input("Enter the number"))
temp1=n
temp2=n
s=0
while(n!=0):
	s=s+1
	n=n//10
print("no of digits is",s)
res=0
while(temp2!=0):

	r=temp2%10
	res=res+r**s
	temp2=temp2//10
if(res==temp1):
	print(res,"is an armstrong number")
else:
	print("Not an armstrong number")