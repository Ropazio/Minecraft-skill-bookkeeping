import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import operations as op

W, H = 800, 600
window = tk.Tk()

class GUI:

	def __init__(self, window):
		self.window = window
		self.window.wm_title("Enchantment bookkeeping")
		self.window.geometry(f"{W}x{H}")


	def add_labels(self):
		enchantment_name = tk.Label(master = self.window, text = "Enchantment")
		amount = tk.Label(master = self.window, text = "Amount")
		description = tk.Label(master = self.window, text = "Description")

		enchantment_name.grid(row = 0, column = 0)
		amount.grid(row = 0, column = 1, columnspan = 3)
		description.grid(row = 0, column = 4)


	def add_counter(self):
		number = 0
		number_label = tk.Label(master = self.window, text = f"{number}")
		# for line in len()
		#	define_decrease_button()
		#	decrease_button.grid(row = line, column = 3)
		#	number_label.grid(row = line, column = 2)
		#	define_increase_button()
		#	increase_button.grid(row = line, column = 1)
		#	
		pass



class Button(GUI):

	def __init__(self, window, *args, **kwargs):
		GUI().__init__(window)
		tk.Button.__init__(self, *args, **kwargs)

	def define_increase_button(self):
		increase_button = tk.Button(self.window, text = "+", command = op.Item_counter.increase_amount())

	def define_decrease_button(self):
		increase_button = tk.Button(self.window, text = "-", command = op.Item_counter.decrease_amount())



if __name__ == '__main__':
	GUI = GUI(window)
	GUI.add_labels()
	GUI.add_counter()
	window.mainloop()
