# tkinter library
import tkinter as tk

'''
  Eaxmple 2: Create clickable button with button widget.
  Button widgets are used to display clickable buttons.
'''
# Create a default window using the Tk() method.
window = tk.Tk()

# Again, 2 steps to do:
# Step 1: Create a  button widget with the text "Click, Me!"
# Step 2: to add widgets to a window we use the widget .pack() method:
button = tk.Button(
  window,
  text="Click me!",
  width=25,
  height=5,
  bg="blue", # On this platfrom, background color customization does not work. So to make this happen need to create button with lable widget
  fg="yellow",
)

button.configure(bg="blue")
button.pack()




# To excute every tkinter codes this script also needs to be added at the end.
window.mainloop()
