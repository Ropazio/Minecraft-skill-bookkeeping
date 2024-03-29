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
	sorted_enchantments_file = sorted(enchantments_file.readlines())

	for line in sorted_enchantments_file:
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
	save = True
	while save:
		try:
			# Create "enchantments_list.txt" file.
			saved_enchantments_file = open(f"enchantments_list{file_number}.txt", "x")
			# Create empty list for minecraft book and quill.
			minecraft_enchantments_list = []

			# Print list of enchantments with labels on top.
			saved_enchantments_file.write(f"{'ID':<4} {'Enchantment name':<26} {'Count'}" + "\n\n")

			for row in list_of_enchantments:
				saved_enchantments_file.write(f"{row[1].ID_number:<4} {row[0]:<26} {row[1].count}" + "\n")

				# If number of enchantments is more than one, add it to the Minecraft list for the book and quill.
				if row[1].count > 0:
					line = f"- {row[0]} x {row[1].count}"
					minecraft_enchantments_list.append(line)

				else:
					continue

			# Print Minecraft enchantment list for book and quill.
			# Minecraft book and quill page maximum number of rows per page is 14.
			# It is possible to contain 19 standard sized characters per line (dot size = 5)
			saved_enchantments_file.write("\n\n" + "List to be printed in Minecraft book and quill in format '- [enchantment name] x [count]'" + "\n\n" )
			b_and_q_list = []

			# If the enchantment name with count is longer than 19 characters, divide it to two rows.
			# If the list containing multiline skill is longer than 12 rows, make an empty line
			# because it is not nice to have the skill divided onto different pages.


			for enchantment in minecraft_enchantments_list:
				too_long = check_enchantment_length(enchantment)
				# If the enchantment name is too long and the list is max. 12 rows long
				# divide the name and add it to the list.
				if too_long and len(b_and_q_list) < 13:
					divide_enchantment_to_two_and_add_to_list(enchantment, b_and_q_list)

				# If the enchantment name is too long and the list is 13 rows long
				# write existing list to the file, empty the list, divide the name and add it to the list.
				elif too_long and len(b_and_q_list) == 13:
					saved_enchantments_file.writelines(b_and_q_list)
					saved_enchantments_file.write("\n")
					b_and_q_list.clear()
					divide_enchantment_to_two_and_add_to_list(enchantment, b_and_q_list)

				# If the enchantment name not too long and the list is max. 13 rows long
				# add the enchantment to the list.
				elif len(b_and_q_list) < 14:
					b_and_q_list.append(enchantment + "\n")

				# If the page is full (list is 14 rows long), make empty line,
				# empty the list and add the enchantment to the empty list.
				else:
					saved_enchantments_file.writelines(b_and_q_list)
					saved_enchantments_file.write("\n")
					b_and_q_list.clear()
					if too_long:
						divide_enchantment_to_two_and_add_to_list(enchantment, b_and_q_list)
					else:
						b_and_q_list.append(enchantment + "\n")


			saved_enchantments_file.writelines(b_and_q_list)
			saved_enchantments_file.close()


		except FileExistsError:	# If enchantment_list0.txt already exists, increase create file enchantments_list1.txt.
			file_number += 1
			if file_number > 10:
				print("\n" + "Too many 'enchantment_list.txt' files. Please don't let there exist more than 10 at a time.")
				save = False
				break
			continue

		save = False

	print()
	print("File saved! Happy minecrafting!")
	print()

	quit()


# Check if the enchantment name is too long for Minecraft book and quill.
def check_enchantment_length(enchantment):
	if len(enchantment) > 19:
		return True
	
	else:
		return False


# Divide enchantment name and count to two lines to fit in Minecraft book and quill.
def divide_enchantment_to_two_and_add_to_list(enchantment, b_and_q_list):
	max_length_with_dash = 18
	for i in range(0, len(enchantment), max_length_with_dash):
		if i == 0:	
			b_and_q_list.append(enchantment[i:i+max_length_with_dash] + "-" + "\n")
		else:
			b_and_q_list.append(enchantment[i:i+max_length_with_dash] + "\n")



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
