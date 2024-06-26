'''
    Here in the page the application layout is built.
    We built 
    2 buttons: 
    1. Open - which will iventually open a file from the user's computer.
    2. Save as... button save the a text file in the user's computer.
    and 1 text input field. In this area users can able to write text and can able to save.

    We also created a class to encapsulates all the functionality of the text editor, 
    making it reusable and adaptable for different contexts.
'''

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

class SimpleTextEditor:
  
  def __init__(self, window):
    # Created a window and having a title
    self.window = window
    self.window.title("Simple Text Editor")

    #Specify the size of the window
    self.window.geometry("1150x750")


    # Using rowconfigure and columnconfigure methods to have the row and column proportionatly along with the window size.
    # To set this we keep the weight=1 as second agrument. And row 0 column 1 as first argument. Since row and column index start from 0.
    self.window.rowconfigure(0, weight=1)
    self.window.columnconfigure(1, weight=1)


    # User wants to insert mulptiple text fileds, so created Text widget
    self.text_field = Text(self.window)
    # Create a frame instance inside the window for the buttons. The frame section will be raised with 2 border 
    self.frame_for_buttons = Frame(self.window, relief=RAISED, border=2)


    # Created button instances for Open and Save As buttons inside the button frame
    self.btn_open = Button(self.frame_for_buttons, text="Open", command=self.open_file)
    self.btn_save = Button(self.frame_for_buttons, text="Save As...", command=self.save_as)
    # edit_save = Button(frm_buttons, text="Edit and Save")

    # Now use the grid function to layout the buttons. Button are on East-West corner in 2 rows and in 1 coumn.
    # And having padding 5 around the buttons.
    self.btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    self.btn_save.grid(row=1, column=0, sticky="ew", padx=5)
    # edit_save.grid(row=2, column=0, sticky="ew", padx=5)

    # Finally show the frames(Buttons and Text field) are shown with grid. Buttons are on column 1 from North to South end.
    # And text input field is on 2nd coulmn spreading North South East West.
    self.frame_for_buttons.grid(row=0, column=0, sticky="ns")
    self.text_field.grid(row=0, column=1, sticky="nsew")


  # Defined a funtion called open_file() to open a dialog box to open a file from the user's computer.
  def open_file(self):
    '''
        This function does:
        1. Open dialog box to open the file from the user's computer using a built-in function askopenfilename() and store the filepath in avariable,
        2. Check if filepath is none, means if user close the open file dialog box then it return nothing.
        3. Delete all the text in the text field to clear the current window.
        4. open the file as input_file using open(), a built-in function that takes filepath, read mode, and translate text to machine readable using utf-8
    '''
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return
    
    self.text_field.delete("1.0", END)

    with open(filepath, mode="r", encoding="utf-8") as input_file:
        # read the file that is opned and store in a variable, text
        text = input_file.read()
        # insert the text now into the text field, this is how the text from the file shows in the text editor text input area.
        self.text_field.insert(END, text)
    # Now make a dynamic change in the window title. Like when the file is open it show the filepath along with the title.
    self.window.title(f"Simple Text Editor - {filepath}")

  def save_as(self):
    '''
    This function does:
    1. Created asksaveasfilename class instance it returs filepath.
    2. Then check if filepath is flase, means if user close the window without saving. then this returns nothing.
    3. open the file as output_file using open(), a built-in function that takes filepath, read mode, and translate text to machine readable using utf-8
    '''
    filepath = asksaveasfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    with open(filepath, mode="w", encoding="utf-8") as output_file:
        # Get all the text in the input text editor and store in text variable.
        text = self.text_field.get("1.0", END)
        # Write the text to the output file
        output_file.write(text)
    # Now make a dynamic change in the window title. After the file is saved it show the filepath along with the title.
    self.window.title(f"Simple Text Editor - {filepath}")