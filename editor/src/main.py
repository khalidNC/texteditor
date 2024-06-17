'''
  This page will responsible to run the application.
  It create the TK instance.
  Then call the class and statr main function.
'''

from tkinter import *
from text_editor import SimpleTextEditor


if __name__ == "__main__":
    window = Tk()
    SimpleTextEditor(window)
    window.mainloop()