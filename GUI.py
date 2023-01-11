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


	def create_frames(self):
		frame = tk.Frame(master = window)
		frame.pack()
		grid_frame = tk.Frame(master = window)
		grid_frame.pack()
		
		return frame, grid_frame


	def add_labels(self, frame):
		enchantment_name = tk.Label(master = frame, text = "Enchantment")
		amount = tk.Label(master = frame, text = "Amount")
		description = tk.Label(master = frame, text = "Description")

		enchantment_name.grid(row = 0, column = 0)
		amount.grid(row = 0, column = 1, columnspan = 3)
		description.grid(row = 0, column = 4)


	def add_enchantment_with_counter(self, grid_frame):
		number = 0
		number_label = tk.Label(master = grid_frame, text = f"{number}")
		for line, enchantment in enumerate(op.list_of_enchantments):
			fixed_line = line + 1
			enchantment_label = tk.Label(master = grid_frame, text = f"{enchantment}")
			enchantment_label.grid(row = fixed_line, column = 0)
			#decrease_button = Decrease_button(grid_frame)
			#decrease_button.grid(row = fixed_line, column = 3)
			number_label.grid(row = fixed_line, column = 2)
			#increase_button = Increase_button(grid_frame)
			#increase_button.grid(row = fixed_line, column = 1)

'''
class Button():

	def __init__(self, window, *args, **kwargs):
		tk.Button.__init__(self, window, *args, **kwargs)


class Decrease_button(Button):

	def __init__(self):
		super().__init__(window)
		decrease_button = Button(self.window, text = "-")

		return decrease_button


class Increase_button(Button):

	def __init__(self, window):
		super().__init__(window)
		increase_button = Button(self.window, text = "+")

		return increase_button
'''


if __name__ == '__main__':
	GUI(window)
	frame, grid_frame = GUI.create_frames(window)
	GUI.add_labels(window, frame)
	GUI.add_enchantment_with_counter(window, grid_frame)
	window.mainloop()
