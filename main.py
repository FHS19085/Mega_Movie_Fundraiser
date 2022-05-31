import Looping_Code_V3
print(Looping_Code_V3)
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

# Main

# Lists needed to hold data

# Ask if user has used before and show instructions

# Loop for ticket details

# Get name
name = Ticket_Name("Name?\n")
# Get age

# Calculate ticket price

# Loop for snacks

# Snack price

# Payment method

# Sales and profit

# Output data to text file

