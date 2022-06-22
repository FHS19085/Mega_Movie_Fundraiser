import String_Checker_V1
print(String_Checker_V1)
profit = 0
# Functions here

# Checks for the users name and checks if it is left blank
def Ticket_Name(question):
	valid = False
	while not valid:
		response = input(question)
		# If name not blank program continues
		if response != "":
			return response
		# If name is blank print message and loop function
		else:
			print("Your name cannot be blank")	
# Checks for an integer more than 0 
def age_check (question):
	error = "please enter a whole number between 12 and 130"
	valid = False
	while not valid:
		# Ask the user for a number and checks if it is valid
		try:
			response = int(input(question))
			if response < 0:
				print(error)
			else:
				return response
		except ValueError:
			print(error)
# Main routine
Total_tickets = 5
name = ""
Ticket_count = 0
Ticket_sales = 0


while name != "xxx" and Ticket_count < Total_tickets:
	if Total_tickets - Ticket_count == 1: 
		print("There is {} seat left".format(Total_tickets - Ticket_count))
	else:
		print("There are {} seats left".format(Total_tickets - Ticket_count))
	# Get name
	name = Ticket_Name("Name?\n")  
	if name == "xxx":
	  break
	# Get age
	age = age_check ("Age: ")
	# Check ticket price based on age
	if age < 16:
		Ticket_price = 7.50
	elif age > 64:
		Ticket_price = 6.50
	else:
		Ticket_price = 10.50
	# Check that the age is valid
	if age < 12:
		print("You are too young to be seeing this movie")
		continue
	elif age > 130:
		print("This is an abnormal age please try again")
		continue
  # Calculate ticket price
	# Check ticket price based on age
	if age < 16:
		Ticket_price = 7.50
	elif age > 64:
		Ticket_price = 6.50
	else:
		Ticket_price = 10.50
	profit_made = Ticket_price - 5
	profit += profit_made
	print("{} : ${:.2f}".format(name, Ticket_price))
	Ticket_count += 1

if Ticket_count == Total_tickets:
	print("All avalable tickets have been sold")
elif Ticket_count == 4:
	print("You have sold {} tickets. \nThere is still {} seat available".format(Ticket_count, Total_tickets - Ticket_count))
else:
 print("You have sold {} tickets. \nThere are still {} seats available".format(Ticket_count, Total_tickets - Ticket_count))


# Loop for snacks

# Snack price

# Payment method

# Sales and profit
# Show total profit from tickets
print("Profit from tickets: ${:.2f}".format(profit))
# Output data to text file

