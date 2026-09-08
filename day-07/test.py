import sys

type = sys.argv[1]

if type == "t2.micro":
	print("It will charge you $2 per day")
elif  type == "t2.medium":
	print("It will charge you $4 per day")
elif type == "t2.large":
	print("It will charge you $8 per day")
else:
	print("Invalid Instance type!!!")
