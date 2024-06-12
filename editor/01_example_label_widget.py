# tkinter library
import tkinter as tk

# Create a default window using the Tk() method.
window = tk.Tk()

# Write some text inside the window has 2 steps:
# Step 1: Create a Label widget with the text "Hello, Tkinter"
'''
  greeting = tk.Label(text="Hello, Tkinter")
'''

# Here we can pass multiple parameters
greeting = tk.Label(
  text="Hello, Tkinter",
  foreground="white", # Set tet to white
  background="black", # Set background to balck
  # Set width and height of the label, the label become bigger nwo and the container means the widow also become bigger.
  width = 20,
  height = 20
)

# Step 2: There are several ways to add widgets to a window. Right now, you can use the Label widget’s .pack() method:
greeting.pack()




# To excute every tkinter codes this script also needs to be added at the end.
window.mainloop()