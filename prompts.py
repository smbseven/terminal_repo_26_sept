nombre = input("what is your name? ")
months_you_coded = input("How many monthe have you been coding? ")
months_your_neighbor_coded = input("How many months has your neighbor been coding? ")
#welcome_message = "Hello world " + nombre
#There are different ways to concatenate text, the f is very helpful to create templates (whatever a template means right now .. jeje)
welcome_message = f"Hello world {nombre}"
total_months_coded = int(months_you_coded) + int(months_your_neighbor_coded)
print(welcome_message)
#print("Together we have been coding for " + str(total_months_coded) + "months")
#Be sure to check both ways to concatenate text
print(f"together we have beenb coding for {total_months_coded} months")