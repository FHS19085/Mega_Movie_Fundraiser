#import Looping_Code_V3
#print(Looping_Code_V3)
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
# Start the loop to make it run at least once
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
	count += 1
	if name == "xxx":
	  count -= 1
	print()

if count == Total_tickets:
	print("All avalable tickets have been sold")
else:
 print("You have sold {} tickets. \nThere are still {} seats available".format(count, Total_tickets - count))
# Get age

# Calculate ticket price

# Loop for snacks

# Snack price

# Payment method

# Sales and profit

# Output data to text file

