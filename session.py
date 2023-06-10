class Session:
    def __init__(self):
        self.target = 0
        self.guesses = []

    def getTarget(self):
        return self.target

    def setTarget(self, target):
        self.target = target

    def getGuesses(self):
        return self.guesses

    def setGuesses(self, guesses):
        self.guesses = guesses