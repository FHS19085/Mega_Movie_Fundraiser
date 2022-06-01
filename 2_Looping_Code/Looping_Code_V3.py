# Start of loop

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
	name = input("Name:")
	count += 1
	if name == "xxx":
		count -= 1
	print()

if count == Total_tickets:
	print("All avalable tickets have been sold")
else:
 print("You have sold {} tickets. \nThere are still {} seats available".format(count, Total_tickets - count))