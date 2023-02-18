f = open("recu_factorial.txt")
print("File Name: ",f.name)

r = f.readlines()
print(r)

fw = open("write.txt","w")

for x in range(0,len(r)):
	
	fw.write(str(r))
fw.close()
