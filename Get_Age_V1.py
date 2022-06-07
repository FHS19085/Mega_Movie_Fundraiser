# Function 

def age_check (question, low_num, high_num):
	error = "Enter a whole number between{}\n" "and {}".format(low_num, high_num)
	valid = False
	while not valid:
		# Ask the user for their age and check if it is valid
		try:
			response = int(input)
			return response
		except ValueError:
			print(error)
# Main routine
age = age_check ("Age: ", 12, 130)
if age < 12 or age > 130 :
	print("you are not of a valid age")
else:
	print ("Age accepted")
