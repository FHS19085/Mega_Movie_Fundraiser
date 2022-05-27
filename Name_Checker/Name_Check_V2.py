# Functions
def Ticket_Name(question, error):
	valid = False
	while not valid:
		response = input(question)
		if response != "":
			return response
		else:
			print(error)	
# Main things
name = Ticket_Name("What is your name?\n", "Your name cannot be blank")
print("Name:",name)