# Function 
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
age = age_check("Age: ")