import random,string,time
req=list(input("enter a 5 digit number to generate of your choice\n"))
if len(req)>5:
	raise ValueError("pls enter only 5 digit number")
else:
	print(f"this program will generate random 5 digit numbers until {req} is generated:.......\n")

	num=[]
	count=0
	while num != req:
		num=random.choices(range(10),k=5)
		print(num)
		count+=1


	print(f"here is your requested number:{num}")
	print("this was generated in {} times".format(count))