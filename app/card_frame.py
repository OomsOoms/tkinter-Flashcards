from tkinter import *
from config import config

class CardFrame(Frame):
    
    def __init__(self, app):
        # Initialize the frame
        super().__init__(app, **config["app"]["bg"])
        
        # Set default question and answer text
        self.question = "Click to reveal the answer"
        self.answer = "But select a topic on the left first!"
        self.showing_question = True

        # Create button to toggle between question and answer
        self.toggle_button = Button(self, text=self.question, **config["card_options"], command=self.toggle_question_answer)
        self.toggle_button.pack(fill=BOTH, expand=True, **config["button_pack_options"])
        self.grid(row=0, column=1, rowspan=5, padx=10, pady=10, columnspan=10, sticky="NSEW")

    def reset_card(self, question, answer):
        # Reset the question and answer text
        self.question = question
        self.answer = answer
        self.showing_question = True
        self.toggle_button.config(text=self.question)

    def toggle_question_answer(self):
        # Toggle between showing the question and showing the answer
        self.showing_question = not self.showing_question
        if self.showing_question:
            self.toggle_button.config(text=self.question)
        else:
            self.toggle_button.config(text=self.answer)
