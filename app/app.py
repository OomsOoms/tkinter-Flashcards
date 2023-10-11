from tkinter import Tk
from config import config

class App(Tk):

    def __init__(self):
        super().__init__()

        # Set the title of the application
        self.title(config["app"]["title"])

        # Set the window geometry (width x height)
        self.geometry(config["app"]["geometry"])

        # Set the window to be resizable (x, y)
        self.resizable(*config["app"]["resizable"])

        # Configure the background color
        self.configure(**config["app"]["bg"])
        
