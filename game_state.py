from random import randint
import statistics
from session import Session
class GameState:
    openingMessage = '#############\n\nWelcome to Number Guessing Game!\n\nIn this game you can test your skills by quickly guessing a random number bewteen 1 and 100.\n\nA number has been generated.\n\nAre you ready?\n\n#############\n'
    def __init__(self):
        self.mean = 0
        self.median = 0
        self.mode = 0
        self.lowScore = 100
        self.globalPlayFlag=True
        self.sessionPlayFlag=True
        self.sessions = []

    def getSessions(self):
        return self.sessions

    def setSessions(self, session):
        self.sessions = session
    
    def initializeSession(self):
        self.sessionPlayFlag=True
        newSession = Session()
        newSession.setTarget(randint(1,100))
        self.sessions.append(newSession)

    def playAgain(self):
        answer =str(input("Do you want play again?\nEnter (Y)es or (N)o\n\n"))
        if(answer.upper() == 'N'):
            self.globalPlayFlag = False
            print('Thank you for playing!\n\nHere are your final statistics')
            self.calculateAndPrintStatistics()
            

    def calculateAndPrintStatistics(self):
        allGuesses = []
        for session in self.sessions:
            guesses = session.getGuesses()
            if(len(guesses) < self.lowScore):
                self.lowScore = len(guesses)
        for session in self.sessions:
            allGuesses.extend(session.getGuesses())

        self.mean = statistics.mean(allGuesses)
        self.median = statistics.median(allGuesses)
        self.mode = statistics.mode(allGuesses)

        statisticsDict = {
            'Total Attempts':len(allGuesses),
            'Mean': self.mean,
            'Median': self.median,
            'Mode': self.mode,
            'Low Score': self.lowScore
        }

        print("Statistics:")
        for key, value in statisticsDict.items():
            print(f"{key}: {value}")
    
    def printOpeningMessage(self):
        print(self.openingMessage)