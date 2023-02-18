low=int(input("Enter LOWER RANGE:"))
high=int(input("Enter HIGHER RANGE:"))

for num in range(low,high+1):
	if(num>1):
		for i in range(2,num):
			if((num%i)==0):
				break

		else:

				print(num)