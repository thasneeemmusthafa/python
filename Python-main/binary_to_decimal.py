def conv(n):
	s=0
	i=0
	while(0<n):
		r=n%10
		s=s+r*(2**i)
		print(s)
		i=i+1
		n=n//10
	print("final output: ",s)
f=int(input("Enter the binary value:"))
conv(f)