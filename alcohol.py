age=input("Enter your age: ")
money=input("Enter your cash amount: ")

def alcohol(age, money):
	if (age>=18) and (money >= 5):
		return "Cheers!"
	elif (age>=18) and (money < 5):
		return "Come again"
	elif (age<18) and (money >= 5):
		return "Wait till you're older!"
	else:
		return "GTFO!"
		
print(alcohol(int(age), int(money)))