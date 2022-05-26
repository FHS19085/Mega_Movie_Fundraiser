def Ticket_Name(question):
	valid = False
	while not valid:
		response = input(question)
		if response != "":
			return response
		else:
			print("This is not a valid name")	
name = Ticket_Name("Name?\n")
print("Name:",name)