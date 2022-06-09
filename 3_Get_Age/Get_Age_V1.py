# Function 

def age_check (question, low_num, high_num):
	error = "Enter a whole number between {} and {}".format(low_num, high_num)
	valid = False
	while not valid:
		# Ask the user for their age and check if it is valid
		try:
			response = int(input(question))
			if low_num <= response <= high_num:
				return response
			else:
				print(error)
		except ValueError:
			print(error)
# Main routine
age = age_check ("Age: ", 12, 130)