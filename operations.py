# Class containing information from the "enchantments.txt" file.
class Enchantment:
	
	def __init__(self, enchantment_name, max_level, description):
		self.enchantment_name = enchantment_name
		self.description = description
		self.max_level = max_level

	def view_description():
		print(self.description)


# Class to count amount of enchantment books. The book is identified with an ID number.
class Item_counter:

	def __init__(self, ID_number, count):
		self.ID_number = ID_number
		self.count = count

	def increase_count(self):
		self.count += 1
		update_table(self.ID_number, self.count)

	def decrease_count(self):
		error = False

		if self.count > 0:
			self.count -= 1

		else:
			print("Amount can't be decreased.")
			print()
			error = True
			return error


		update_table(self.ID_number, self.count)


# Change numbers 1, 2, 3, 4 and 5 to I, II, III, IV and V.
def change_number_to_roman(enchantment_level):
	if enchantment_level == 0:
		return "I"
	elif enchantment_level == 1:
		return "II"
	elif enchantment_level == 2:
		return "III"
	elif enchantment_level == 3:
		return "IV"
	elif enchantment_level == 4:
		return "V"
	else:
		print("[invalid level]" + "\n")


# Read the "enchantments.txt" file and save the enchantment name, its maximum level and description
# to a dictionary.
def save_enchantment_with_attributes_to_dict():
	# Creating an empty dictionary: [enchantment_name]: enchantment_name, max_level, description.
	enchantments_dict = {}

	# Opening and reading the file line by line dismissing comment lines and empty lines.
	enchantments_file = open("enchantments.txt", "r")

	for line in enchantments_file.readlines():
		line.strip()

		if line.startswith("#") or len(line.strip()) == 0:
			continue
		else:
			row = line.split(":")
			enchantment_name, max_level, description = row
			enchantment_with_attributes = Enchantment(enchantment_name, max_level, description)
			enchantments_dict[enchantment_name] = enchantment_with_attributes

	# Close the file
	enchantments_file.close()

	return enchantments_dict


# Create a list containing all possible enchantments with levels, the corresponding (book) count and ID number. 
def save_all_enchantments_to_list(enchantments_dict):

	# Creating an empty list containing enchantments from all skill levels.
	list_of_enchantments = []

	ID = 0
	for enchantment_key in enchantments_dict:
		for enchantment_level in range(int(enchantments_dict[enchantment_key].max_level)):
			ID += 1
			if int(enchantments_dict[enchantment_key].max_level) == 1:
				enchantment = [enchantment_key, Item_counter(ID, 0)]
				list_of_enchantments.append(enchantment)

			else:
				enchantment = [(enchantment_key + " " + (change_number_to_roman(enchantment_level))), Item_counter(ID, 0)]
				list_of_enchantments.append(enchantment)

	return list_of_enchantments


# Update the list of enchantments.
def update_table(ID, count):
	for enchantment in list_of_enchantments:
		if ID == enchantment[1].ID_number:
			enchantment[1].count = count

	return


# Print columns with headlines "ID", "enchantment name" and "count".
# Print the list of enchantments.
def print_table(list_of_enchantments):
	print()
	print(f"{'ID':<4} {'Enchantment name':<26} {'Count'}")
	print()
	for enchantment in list_of_enchantments:
		print(f"{enchantment[1].ID_number:<4} {enchantment[0]:<26} {enchantment[1].count}")
	print()


# Ask the user to select an enchantment from the list by giving the corresponding ID number.
# The user may also quit and save the created list of enchantments.
def select_enchantment_from_list(list_of_enchantments):

	ID_flag = False

	while not ID_flag:
		try:
			print("Select an enchantment by writing the corresponding ID number.")
			print("Quit and save the current list of enchantments by writing '0'")
			ID = int(input("Please select an enchantment with the corresponding ID or quit: "))

			# Quit and save list of enchantments.
			if ID == 0:
				quit_and_save_list(list_of_enchantments)

			# If the given ID number is not in the list of enchantments ID column, print error and ask for the ID again.
			elif ID not in range(1, (len(list_of_enchantments) + 1)):
				print("No enchantment match the given ID." + "\n")
				continue

			ID_flag = True

		except ValueError:
			print("Invalid ID. You need to provide an ID number." + "\n")


	# Return ID, enchantment name and enchantment count for the ask_count_operation function.
	for enchantment in list_of_enchantments:
		if ID == enchantment[1].ID_number:
			return enchantment[1].ID_number, enchantment[0], enchantment[1].count

	raise Exception("Sorry, an unknown error occured with the ID. :(" + "\n")


# Ask the user if they would like to increase or decrease enchantment (book) count.
# The user may also return to the ID selection if they accidentally make a mistake.
def ask_count_operation(ID, name, count, list_of_enchantments, enchantments_dict):

	while True:

		print()
		print("Increase enchantment (book) count by 1 with 'i'.")
		print("Decrease enchantment (book) count by 1 with 'd'.")
		print("View the enchantment description with 'v'.")
		print("Return to enchantment selection with 'r'.")
		print()
		operation = input("Please make a selection: ")
		print()
		operation.lower().strip()
		selected_enchantment = Item_counter(ID, count)

		# Increase
		if operation == "i":
			selected_enchantment.increase_count()
			print_table(list_of_enchantments)
			return

		# Decrease
		elif operation == "d":
			error = selected_enchantment.decrease_count()

			if error:
				return

			print_table(list_of_enchantments)
			return

		# Return
		elif operation == "r":
			return

		# View description
		elif operation == "v":
			for enchantment_key in enchantments_dict:
				if enchantment_key in name:
					print(f"{enchantment_key}:" + enchantments_dict[enchantment_key].description)
					return
				else:
					continue

				raise Exception("Sorry, the description was not found. :(" + "\n")

		# None of the above.
		else:
			print("Invalid selection." + "\n")
			continue

	raise Exception("Sorry, an unknown error occured with the operation. :(" + "\n")



# This function saves the list of enchantments to an "enchantment_list.txt" file followed by
# a list of enchantments where the count is more than 0 in Minecraft book and quill format
# to be copied and pasted in the book.
def quit_and_save_list(list_of_enchantments):
	file_number = 0
	while True:
		try:
			saved_enchantments_file = open(f"enchantments_list{file_number}.txt", "x")
			saved_enchantments_file.write(f"{'ID':<4} {'Enchantment name':<26} {'Count'}" + "\n\n")
			for row in list_of_enchantments:
				saved_enchantments_file.write(f"{row[1].ID_number:<4} {row[0]:<26} {row[1].count}" + "\n")
			saved_enchantments_file.close()
			break

		except FileExistsError:	# If enchantment_list0.txt already exists, increase create file enchantments_list1.txt.
			file_number += 1
			continue

	print()
	print("File saved! Happy minecrafting!")
	print()

	quit()



if __name__ == "__main__":
	enchantments_dict = save_enchantment_with_attributes_to_dict()
	list_of_enchantments = save_all_enchantments_to_list(enchantments_dict)

	# Print the list of enchantments for the user and ask the user to select an enchantment from the list.
	# Then ask the user if they would like to increase or decrease the enchantment (book) count.
	print_table(list_of_enchantments)
	while True:
		enchantment_ID, enchantment_name, enchantment_count = select_enchantment_from_list(list_of_enchantments)
		ask_count_operation(enchantment_ID, enchantment_name, enchantment_count, list_of_enchantments, enchantments_dict)

	# When user is done, save the list and quit.
	quit_and_save_list(list_of_enchantments)
