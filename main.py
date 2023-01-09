class Enchnantment:
	
	def __init__(self, enchantment_name, max_level, description):
		self.enchantment_name = enchantment_name
		self.description = description
		self.max_level = max_level


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
		enchantment_with_attributes = Enchnantment(enchantment_name, max_level, description)
		enchantments_dict[enchantment_name] = enchantment_with_attributes


# close the file
enchantments_file.close()

for enchantment_key in enchantments_dict:
	print(enchantment_key, enchantments_dict[enchantment_key].max_level)