'''
Created on 4 Apr 2016

@author: aml
'''


from Tkconstants import W
from Tkinter import Tk, Button, Entry, Text

from hangman import Hangman


class HangmanGUI(Tk):
    
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.hangman = Hangman()
        
        self.initialise()
        
    def initialise(self):
        self.geometry('{}x{}'.format(600, 600))
        
        
        self.grid()
        
        new_game = Button(self, command = self.hangman.begin_new_game, text = 'New game')
        new_game.grid(column = 2, row = 2, sticky = W)
        
        guess_letter = Button(self, command = lambda: self.guess(True), text = 'Guess letter')
        guess_letter.grid(column = 3, row = 3, sticky = W)
    
        
    def guess(self, guessing_letter):
        title = 'Guess a '
        if guessing_letter:
            title += 'letter'
        else:
            title += 'word'
        
        
        g_window = Tk()
        g_window.title(title)
        g_window.grid()
        
        entry = Entry(g_window)
        entry.grid(column = 1, row = 1)
        
        confirm = Button(g_window, command = lambda: 
                         self.send_input(guessing_letter, entry.get(), g_window), text = 'Confirm')
        confirm.grid(column = 1, row = 3)
     
    def send_input(self, guessing_letter, user_guess, g_window):
        message = Text(g_window, fg = 'red') #TODO
        message.insert('1.0', 'If an error occurs, it will be displayed here...')
        message.grid(column = 1, row = 5)
        
        if user_guess.isalpha():
            if (guessing_letter and len(user_guess) > 1):
                message.delete(0, 'end')
                message.insert('1.0', 'Please only guess a letter')
            else:
                if guessing_letter:
                    self.hangman.guess_letter(user_guess)
                else:
                    self.hangman.guess_word(user_guess)
        else:
            message.delete(0, 'end')
            message.insert('1.0', 'Please enter a valid guess')
            
        g_window.destroy()
            
             
        
    
if __name__ == "__main__":
    hg = HangmanGUI(None)
    hg.title('Hangman')
    hg.mainloop()
        





