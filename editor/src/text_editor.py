import tkinter as tk

# Created a window and having a title
window = tk.Tk()
window.title("Simple Text Editor")

# Using a rowconfigure and columnconfigure methods to alocate row and column for the window.
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)



window.mainloop()