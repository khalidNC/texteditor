import tkinter as tk


# Create a button effect with label widget:
# create a label widget and pass parameters
# then pack the widget
# then use a method called bind() to make the label act as button, here we pass <Button-1> agrument as syntax 
# and the second argument is reference of the action, like i want to print label_button clicked text while i click on the button 
# So i created a function called on_click(), and it prints the text. Adn just reference this function as 2nd arg in bind funtion.

def on_click(event):
    print("Label button clicked!")

window = tk.Tk()

label_button = tk.Label(
    text="Click me!",
    width=20,
    height=5,
    bg="blue",
    fg="yellow",
    cursor="arrow",
    relief="raised",
    bd=2
)
label_button.pack()

label_button.bind("<Button-1>", on_click)

window.mainloop()
