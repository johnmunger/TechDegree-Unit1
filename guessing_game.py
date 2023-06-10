"""
Project 1 - Number Guessing Game
--------------------------------

For this first project you can use Workspaces. 

NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
from game_state import GameState

def startGame():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
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
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    gameState = GameState()
    gameState.printOpeningMessage()
    while(gameState.globalPlayFlag):
        firstSession = len(gameState.sessions) == 0
        gameState.initializeSession()
        if(not firstSession):
           print(f'Can you guess in less than {gameState.lowScore} tries?! Go for broke!\n\n')
        while(gameState.sessionPlayFlag):
            guess(gameState)
        gameState.calculateAndPrintStatistics()
        gameState.playAgain()

# Kick off the program by calling the startgame function.

def guess(gameState):
    #retrive input
    #add to latest session
    #add to gamestate
    #print feedback
    #updateFlag
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
