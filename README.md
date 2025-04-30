# Games-for-fun
### Author: Vlad Digori

---
# Contents :

- [Summary](#summary)
- [Descriptions about the games](#description-about-the-game) 

---

# Summary

I made some games using python to help me learn some aspects like `while` loops, using the `random` library.
The games are :

- [Guess the number](https://github.com/glemiu6/Games-for-fun/blob/master/Games/guessnum.py) 
- [Hangman](https://github.com/glemiu6/Games-for-fun/blob/master/Games/hangman.py)
- [Pig](https://github.com/glemiu6/Games-for-fun/blob/master/Games/pig%20game.py)
- [Rock Paper Scissors](https://github.com/glemiu6/Games-for-fun/blob/master/Games/rock%20paper.py)

---

# Description about the game

## - [Guess the number](https://github.com/glemiu6/Games-for-fun/blob/master/Games/guessnum.py)  

### Main objective: Guessing the number 

---

For starters , we import the `random` library so the computer can generate a random number between 1 and `n`.  
Then we start guessing.  
If the number is higher than the one the computer generated it shows : `To big, the number is smaller`.  
If it's too small, we get this message : `To small , the number is bigger`.  
If we guess the number correctly , the message will be this : `You guessed correctly`.

---

## - [Hangman](https://github.com/glemiu6/Games-for-fun/blob/master/Games/hangman.py)

### Main objective: Guessing the word in 7 tries.  

---

We have a file with random words and the computer chooses a word using the `random` library.  
Replace the word with the `_` symbol so the word would be unknown till we guess it or run out of tries.  
By using a `set()` we make sure that we don't repeat letters and don't discount the tries by that.  

---

## - [Pig](https://github.com/glemiu6/Games-for-fun/blob/master/Games/pig%20game.py)

### Main objective: Reach the target score first.

---

Using the `random` library we can generate random numbers so the game won't be one-sided.  
You and the computer roll a dice from 1-10. The first person reaching the target score `target=30` , wins.  
But there's catch, if you roll 1 , you go back to 0.

---

## - [Rock Paper Scissors](https://github.com/glemiu6/Games-for-fun/blob/master/Games/rock%20paper.py)

### Main objective: Beat the robot

---

We all know the game rock paper scissors.  
To make it we import the `random` library and make a list with our weapons(rock,paper,scissor).  
We have the `user` function where we select our choice and the `computer` function where the computer selects randomly.






