'''
Created on 4 Apr 2016

@author: aml
'''


from Tkconstants import W
from Tkinter import Tk, Button, Entry

from hangman import Hangman
import tkMessageBox


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
        new_game.grid(column = 2, row = 5, sticky = W)
        
        guess_letter = Button(self, command = lambda: self.guess(True), text = 'Guess letter')
        guess_letter.grid(column = 3, row = 5, sticky = W)
        
        guess_button = Button(self, command = lambda: self.guess(False), text = 'Guess word')
        guess_button.grid(column = 4, row = 5, sticky = W)
    
        
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
        
        
        if user_guess.isalpha():
            if (guessing_letter and len(user_guess) > 1):
                tkMessageBox.showerror('Error', 'Please only guess a letter')
            else:
                if guessing_letter:
                    self.hangman.guess_letter(user_guess)
                else:
                    self.hangman.guess_word(user_guess)
                g_window.destroy()
        else:
            tkMessageBox.showerror('Error', 'Please make a valid guess')
            
        
            
             
        
    
if __name__ == "__main__":
    hg = HangmanGUI(None)
    hg.title('Hangman')
    hg.mainloop()
        





