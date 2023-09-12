from tkinter import *
import tkinter
import tkinter as tk
from tkinter import messagebox
import random
import time




def generate(event=None):
	try:
		output.delete(1.0, END)
		a = int(toEntryBox.get())
		b = int(fromEntryBox.get())

		number = random.randint(b, a)

		# Insert the generated number in the center of the Text widget
		text = str(number)
		center_line = output.index(tk.END).split(".")[0]  # Calculate the center line
		output.insert(f"{center_line}.0", text + "\n")
	except:
		
		errorLabel.grid(row=10,column=2)
		root.after(800, lambda: errorLabel.grid_forget())
		







#-------------------------
root = tk.Tk()
root.title('RNG')
root.geometry('411x483')
root.minsize(411,483)
root.maxsize(411,483)
root.config(bg='#212121')

label1 = Label(root, text='pick a random number from:', bg='#212121',fg='white', font='verdena, 22')
label1.grid(row=0, column=2)



fromEntryBox = Entry(root,font='verdena 24',bg='#3b3b3b',width=10 ,fg='white')
fromEntryBox.grid(row=1, column=2)



label2 = Label(root, text='to:', bg='#212121', font = 'verdena 20',fg='white')
label2.grid(row=2, column=2)

toEntryBox = Entry(root,font='verdena 24',bg='#3b3b3b',width=10 ,fg='white')
toEntryBox.grid(row=3, column=2)
toEntryBox.get()

spacer1 = tk.Label(root, text="", bg='#212121')
spacer1.grid(row=4, column=0)
spacer2 = tk.Label(root, text="", bg='#212121')
spacer2.grid(row=7, column=0)

output = Text(root,width=18, height=4,bg = '#212121',fg='white',font='Helvetica 30')
output.grid(row=10, column=2)



global errorLabel
errorLabel= Label(root, text='ERROR.',font='Helvetica 70', fg='#8a0a0a',bg='#212121')

root.bind('<Return>', generate)

generate_button = Button(root, text='generate',padx = 50, pady=30,bg='#5a0091',fg='white',command = generate, font='Helvetica 14', borderwidth=0, activebackground='#7d1cba', activeforeground='#c9c9c9')
generate_button.grid(row=6, column=2)
#-----------------------------------------







root.mainloop()
