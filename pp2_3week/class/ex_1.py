class String:
    def __init__(self):
        pass
    
    def getString(self):
        self.string = input()
    
    def printString(self):
        print(self.string.upper())

sh = String()
sh.getString()
sh.printString()