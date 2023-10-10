from tkinter import Tk

class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("Flashcards - Computer Hardware")
        self.geometry("500x500")
        self.resizable(False, False)
        self.configure(bg="black")
