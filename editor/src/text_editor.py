'''
    Here in the page the application layout is built.
    We built 
    2 buttons: 
    1. Open - which will iventually open a file from the user's computer.
    2. Save as... button save the a text file in the user's computer.
    and 1 text input field. In this area users can able to write text and can able to save.

'''
import tkinter as tk

from tkinter import *

# Created a window and having a title
window = Tk()
window.title("Simple Text Editor")

#Specify the size of the window
window.geometry("1150x750")


# Using rowconfigure and columnconfigure methods to have the row and column proportionatly along with the window size.
# To set this we keep the weight=1 as second agrument. And row 0 column 1 as first argument. Since row and column index start from 0.
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


# User wants to insert mulptiple text fileds, so created Text widget
text_field = Text(window)
# Create a frame instance inside the window for the buttons. The frame section will be raised with 2 border 
frame_for_buttons = Frame(window, relief=RAISED, border=2)


# Created button instances for Open and Save As buttons inside the button frame
btn_open = Button(frame_for_buttons, text="Open")
btn_save = Button(frame_for_buttons, text="Save As...")
# edit_save = Button(frm_buttons, text="Edit and Save")

# Now use the grid function to layout the buttons. Button are on East-West corner in 2 rows and in 1 coumn.
# And having padding 5 around the buttons.
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
# edit_save.grid(row=2, column=0, sticky="ew", padx=5)

# Finally show the frames(Buttons and Text field) are shown with grid. Buttons are on column 1 from North to South end.
# And text input field is on 2nd coulmn spreading North South East West.
frame_for_buttons.grid(row=0, column=0, sticky="ns")
text_field.grid(row=0, column=1, sticky="nsew")


window.mainloop()
