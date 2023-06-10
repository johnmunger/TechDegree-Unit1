#Requirements
---
Acceptance Criteria copied from initial code guessing_game.py

When the program starts, we want to:

    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Save their attempt number to a list.
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    7. Ask the player if they want to play again.
    

#Disclaimer
---
Hello, my name is John.  私はジョンです。Je m'appelle John.

https://www.jdmunger.com/

* I have been a professional software developer for 5 years.  
* I have a programming style, already.
* I use camelCase.
* I learned Python, C++, and C in college.  I am now a fullstack dev where I do React.js, Java, and PostGreSQL
* I am always open to learn.
* I just welcomed my first child, Kirin!

#Design
---
I approached the solution through the lens of OOP.  Implicit in my design pattern was the concept behind React reducer.  A reducer processes actions by taking the state, applying logic, and returning the state anew.  In this way, a game is set of actions that be applied to a set of variables.

Naturally, GameState is the first class.

GameState keeps track of all the relevant variables.

I imagined the gamestate as containing the statistics data we would present to the user, and session data i.e. individual game data.

Therefore GameState initially contained:

    mean, median, mode, sessions[]


I knew each session would contain:

    targetnumber, guesses[]

From there I built my classes and my getter/setter functions.

The expansion of the classes came from implementing the control structures in guessing_game.py

I iterated from there until I met the acceptance criteria. 
