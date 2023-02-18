def sumn(num):
	sum=0
	for i in range(1,num+1):
		sum=sum+i
	return sum
num=int(input("Enter the number:"))
print("The sum till",num," is ",sumn(num))