'''
  Here in this page will handle the functions of the buttons and the text input.
  We will create separate functions for the buttons.
'''

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import editor.src.text_editor as text_editor

# window = Tk()
# text_field = Text(window)


# Defined a funtion called open_file() to open a dialog box to open a file from the user's computer.
def open_file():
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
  
  text_editor.text_field.delete("1.0", END)

  with open(filepath, mode="r", encoding="utf-8") as input_file:
    # read the file that is opned and store in a variable, text
    text = input_file.read()
    # insert the text now into the text field, this is how the text from the file shows in the text editor text input area.
    text_editor.text_field.insert(END, text)
  # Now make a dynamic change in the window title. Like when the file is open it show the filepath along with the title.
  text_editor.window.title(f"Simple Text Editor - {filepath}")
  
