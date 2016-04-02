'''
Created on 31 Mar 2016

@author: aml
'''

import random
from sys import stdin

class Hangman:
    possible_words = ['car', 'hanged', 'lackadaisical', 'start', 'random']
    max_number_of_guesses = 10
    
    def __init__(self):
        self.number_of_guesses = 0
        self.word_to_guess = self.random_word_to_guess()
        self.word_guessed = False
        self.my_word = self.word_of_underlines(len(self.word_to_guess))
        
    def word_of_underlines(self, l):
        wd = ''
        for i in range (0, l):
            wd += '_'
        return wd
    
    def recompute_my_word(self, letter):
        word_as_list = list(self.my_word)
        
        for pos in self.find_letter_positions_in_word(letter, self.word_to_guess):
            word_as_list[pos] = letter
            
        self.my_word = ''.join(word_as_list)
            
        
    def find_letter_positions_in_word(self, letter, word):
        pos_list = []

        for i in range (0, len(word)):
            if word[i] == letter:
                pos_list.append(i)
        
        return pos_list
        
        
    def random_word_to_guess(self):
        return Hangman.possible_words[random.randint(0, 4)]
    
    def begin_new_game(self):
        print('New game has begun.')
        self.play()
        
    
    def play(self):
        if self.word_guessed:
            self.award_win()
            return
            
        
        if self.number_of_guesses == Hangman.max_number_of_guesses:
            self.notify_loser()
            return
            
         
        else:
            # Keep playing TODO
            print('Please either guess a letter or the whole word:')
            print('gl your_letter for letter guess')
            print('gw your_word for word guess')
            print('===============================================')
            
            user_input = stdin.readline()
            
            if len(user_input.split(' ')) > 0 and user_input.split(' ')[0] == 'gl':
                self.guess_letter(user_input.split(' ')[1].rstrip())
                
            elif len(user_input.split(' ')) > 0 and user_input.split(' ')[0] == 'gw':
                self.guess_word(user_input.split(' ')[1].rstrip())    
            
            else:
                print('Invalid input. Please see usage.')
                
           
                
    def guess_letter(self, letter):
        print ('You have guessed a letter: ' + letter)
        
        self.recompute_my_word(letter)
        
        
        if self.my_word == self.word_to_guess:
            self.word_guessed = True
        self.show_my_word()    
        
        self.number_of_guesses += 1
        self.play()
        
    def guess_word(self, word):
        print('You have guessed the whole word: ' + word)
        
        if word == self.word_to_guess:
            self.word_guessed = True
        else:   
            self.show_my_word()
        
        self.number_of_guesses += 2
        self.play()
        
    def show_my_word(self):
        print('The word looks like this at the moment: ' + self.my_word)
        print('===============================================')
                    
              
    def award_win(self):
        print('You won.')
        
        
    def notify_loser(self):
        print('You lost.')
        
        
          
         
                   
        
            
