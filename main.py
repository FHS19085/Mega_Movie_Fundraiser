import Ticket_Price_V1
print(Ticket_Price_V1)
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
name = ""
count = 0
Total_tickets = 5

while name != "xxx" and count < Total_tickets:
	if Total_tickets - count == 1: 
		print("There is {} seat left".format(Total_tickets - count))
	else:
		print("There are {} seats left".format(Total_tickets - count))
	# Get name
	name = Ticket_Name("Name?\n")  
	if name == "xxx":
	  break
	# Get age
	age = age_check ("Age: ")

	# Check that the age is valid
	if age < 12:
		print("You are too young to be seeing this movie")
		continue
	elif age > 130:
		print("This is an abnormal age please try again")
		continue
	count += 1

if count == Total_tickets:
	print("All avalable tickets have been sold")
else:
 print("You have sold {} tickets. \nThere are still {} seats available".format(count, Total_tickets - count))

# Calculate ticket price

# Loop for snacks

# Snack price

# Payment method

# Sales and profit

# Output data to text file

