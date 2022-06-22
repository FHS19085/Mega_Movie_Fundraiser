# Functions
# String checker function takes in the question and the list of valid responses
def string_checker(question, to_check):

	Valid = False
	while not Valid:

		# Ask a question and put response into lowercase
		response = input(question).lower()

		if response in to_check:
			return response

		else:
			for item in to_check:
				# Checks if response is the first letter of an item in the list
				if response == item[0]:
					return item

		print("Please answer with either yes or no")
# Main routine
for item in range (0,6):
	want_snacks = string_checker("Do you want any snacks?\n", ["yes", "no"])
	print("You answered", want_snacks ,"to snacks")