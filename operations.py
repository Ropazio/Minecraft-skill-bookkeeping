# class with information from enchantments.txt.
class Enchantment:
	
	def __init__(self, enchantment_name, max_level, description):
		self.enchantment_name = enchantment_name
		self.description = description
		self.max_level = max_level

#	def increase_level():
#		if level < self.max_level:
#			level += 1
#		else:
#			print("Level can't be increased.")
#
#	def decrease_level():
#		if 1 < level < self.max_level:
#			level -= 1
#		else:
#			print("Level can't be decreased.")

	def view_description():
		print(self.description)


# class to count amount of enchantment books.
class Item_counter:

	def __init__(self, ID_number, count):
		self.ID_number = ID_number
		self.count = count

	def increase_count():
		count += 1

	def decrease_count():
		if count > 0:
			count -= 1
		else:
			print("Amount can't be decreased.")



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
		print("[invalid level]")


def save_enchantment_with_attributes_to_dict():
	# creating an empty dictionary: [enchantment_name]: enchantment_name, max_level, description.
	enchantments_dict = {}

	# opening and reading the file line by line dismissing comment lines and empty lines.
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

	# close the file
	enchantments_file.close()

	return enchantments_dict


def save_all_enchantments_to_list(enchantments_dict):
	# creating an empty list containing enchantments from all skill levels.
	list_of_enchantments = []

	ID = 0
	# print all possible enchantments.
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


# print ID_number, enchantment with level and count
def print_table(list_of_enchantments):
	for enchantment in list_of_enchantments:
		print(enchantment[1].ID_number, enchantment[0], enchantment[1].count)


def select_enchantment_from_list(list_of_enchantments):
	ID_flag = False

	while not ID_flag:
		try:
			ID = int(input("Select enchantment with ID_number: "))

			if ID not in range(1, 110):
				print("No enchantment match the given ID.")
				continue

			ID_flag = True

		except ValueError:
			print("Invalid ID. You need to provide an ID number.")

	for enchantment in list_of_enchantments:
		if ID == enchantment[1].ID_number:
			return enchantment[0], enchantment[1].count


def ask_count_operation():
	pass



enchantments_dict = save_enchantment_with_attributes_to_dict()
list_of_enchantments = save_all_enchantments_to_list(enchantments_dict)
print_table(list_of_enchantments)
enchantment_name, enchantment_count = select_enchantment_from_list(list_of_enchantments)
operation = ask_count_operation()
