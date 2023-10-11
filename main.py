# Import the app module
from app import *

# If this file is being run as the main program
if __name__ == "__main__":
    
    # Create an instance of the App class
    app = App()
    
    # Create an instance of the CardFrame class, passing in the app instance
    card_frame = CardFrame(app)
    
    # Create an instance of the ButtonFrame class, passing in the app instance and the card_frame instance
    ButtonFrame(app, card_frame)
    
    # Start the main event loop of the app
    app.mainloop()
