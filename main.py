# class with information from enchantments.txt.
class Enchantment:
	
	def __init__(self, enchantment_name, max_level, description):
		self.enchantment_name = enchantment_name
		self.description = description
		self.max_level = max_level

	def increase_level():
		if level < self.max_level:
			level += 1
		else:
			print("Level can't be increased.")

	def decrease_level():
		if 1 < level < self.max_level:
			level -= 1
		else:
			print("Level can't be decreased.")

	def view_description():
		print(self.description)


# class to count amount of enchantment books.
class Item_counter(Enchantment):

	def __init__(self, amount):
		Enchantment.__init(self, enchantment_name, max_level, description)
		self.amount = 0

	def increase_amount():
		self.amount += 1

	def decrease_amount():
		if self.amount > 0:
			self.amount -= 1
		else:
			print("Amount can't be decreased.")


# creating an empty dictionary.
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

# print all possible enchantments.
for enchantment_key in enchantments_dict:
	for enchantment_level in range(int(enchantments_dict[enchantment_key].max_level)):
		if int(enchantments_dict[enchantment_key].max_level) == 1:
			print(enchantment_key)
		else:
			print(enchantment_key, enchantment_level+1)

