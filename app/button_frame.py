from tkinter import *
import random

from config import config

class ButtonFrame(Frame):
    
    def __init__(self, app, card_frame):
        # initialize the ButtonFrame with the app and card_frame
        super().__init__(app, **config["app"]["bg"])
        self.card_frame = card_frame
        
        # add buttons and their callbacks dynamically
        for label in config["questions"]:
            # create a button with the label and callback function
            button = Button(self, text=label, **config["button_options"], command=lambda label=label: self.callback(label))
            # pack the button to the top of the frame
            button.pack(side=TOP, **config["button_pack_options"])

        # add padding to the frame and show it
        self.grid(row=0, column=0, padx=10, pady=10)

    def callback(self, label):
        # choose a random question and answer from the config file
        question = random.choice(list(config["questions"][label].keys()))
        answer = config["questions"][label][question]

        # reset the card frame with the chosen question and answer
        self.card_frame.reset_card(question, answer)