def rec(n):
	if(n==1):
		return 1
	else:
		return n*rec(n-1)
num=int(input("Enter the number:"))
if(num<0):
	print("Factorial does not exist")
elif(num==0):
	print("Factorial is 1")
else:
	print("The factorial is ",rec(num))