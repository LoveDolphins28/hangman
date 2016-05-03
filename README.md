# Hangman v1.0 by AML

## Simple GUI Hangman written in Python
This is my first program (if you can call it that) written in python from
scratch.

## Functionality
For now it is quite limited.
* There are 5 hard-coded possible words one out of
which is chosen when a new game begins.
* Players can either guess a letter at a time or the whole word.
* A drawback would be that a word-guess and a letter-guess have the same cost
 (i.e. 1 guess taken).
* The player can guess up to 10 times before he loses the game.
* Basic Turtle Graphics were used in order to provide an animated visualisation
of the hanged man.

## How to run
`python hangman_gui.py`
* You can edit the list of possible words which is found inside hangman.py
* This is tested and working under Python 2.7 and OSX El Capitan

## To do
* Document the code
* Add different levels of difficulty
* Make it work with input from a text file that contains possible words
* More beautiful graphics
