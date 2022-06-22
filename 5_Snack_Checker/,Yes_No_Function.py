# Functions
def yes_no(question):

	error = "please answer with yes or no"
	Valid = False
	while not Valid:

		# Ask a question and put response into lowercase
		response = input(question).lower()

		if response == "yes" or response == "y":
			return "yes"
		elif response == "no" or response == "n":
			return "no"
		else:
			print(error)

# Main routine
for item in range (0,6):
	want_snacks = yes_no("Do you want any snacks?\n")
	print("You answered", want_snacks ,"to snacks")