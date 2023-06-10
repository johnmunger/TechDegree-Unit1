from random import randint
import statistics
from session import Session
class GameState:
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
        while True:
            try:
                answer =str(input("Do you want play again?\nEnter (Y)es or (N)o\n\n"))
                if not(answer.upper() == 'Y' or answer.upper() == 'N'):
                    raise ValueError("Please Enter the letter 'y' or 'n'\n\n")
                break
            except ValueError as err:
                print(err)
                continue
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
        
        allGuesses.sort()

        self.mean = round(statistics.mean(allGuesses), 1)
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
        bar="#############"
        welcome="Welcome to Number Guessing Game!"
        description="In this game you can test your skills by quickly guessing a random number bewteen 1 and 100."
        enticement="A number has been generated."
        provocation="Are you ready?"
        messageList=[bar, welcome, description, enticement, provocation, bar]
        for message in messageList:
            print(f"{message}\n")

    def printLowScore(self):
        firstSession = len(self.sessions) == 1
        if(not firstSession):
           print(f'Can you guess in less than {self.lowScore} tries?! Go for broke!\n\n')
