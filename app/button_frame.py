from tkinter import *
import random

from config import config

class ButtonFrame(Frame):
    
    def __init__(self, app):
        super().__init__(app, **config["app"]["bg"])
        # add buttons and their callbacks dynamically
        for label, value in config["buttons"].items():
            button = Button(self, text=label, command=lambda label=label: self.callback(value), **config["button_options"])
            button.pack(side=TOP, **config["button_pack_options"])

        # add padding to the frame and show it
        self.grid(padx=10, pady=10)

    def callback(self, value):
        random_key = random.choice(list(value.keys()))

        print(random_key)
        print(value[random_key])