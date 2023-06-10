"""
Project 1 - Number Guessing Game
--------------------------------
"""
from game_state import GameState

def startGame():
    
#The Game's Control Structure
    gameState = GameState()
    gameState.printOpeningMessage()
    while(gameState.globalPlayFlag):
        gameState.initializeSession()
        gameState.printLowScore()
        while(gameState.sessionPlayFlag):
            guess(gameState)
        gameState.calculateAndPrintStatistics()
        gameState.playAgain()

# Kick off the program by calling the startgame function.

def guess(gameState):
    #Get valid guess
    while True:
      try:
        guess = int(input("Enter your guess: "))
        inBounds = guess > 0 and guess <=100
        if (inBounds):
          break
        print("Please enter a number between 1 and 100! Thanks!")
      except ValueError:
        print("Input is not an integer")
        continue
        
    sessions = gameState.getSessions()
    latestSession = len(sessions) - 1
    sessionGuesses = sessions[latestSession].getGuesses()
    sessionGuesses.append(guess)
    sessions[latestSession].setGuesses(sessionGuesses)
    gameState.setSessions(sessions)

    target = sessions[latestSession].getTarget()

    if guess > target:
        print("It's lower\n")
    elif guess < target:
        print("It's higher\n")
    else:
        print(f"You guessed it in {len(sessionGuesses)} tries!\n")
        gameState.sessionPlayFlag=False

startGame()
