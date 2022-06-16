profit = 0 

name = ""
while name != "xxx":
	name = input("Name: ")
	
	if name == "xxx":
		break
	age = int(input("Age: "))
	if age < 16:
		Ticket_price = 7.50
	elif age > 64:
		Ticket_price = 6.50
	else:
		Ticket_price = 10.50
	profit_made = Ticket_price - 5
	profit += profit_made
	print("{} : ${:.2f}".format(name, Ticket_price))

print("Profit from tickets: ${:.2f}".format(profit))