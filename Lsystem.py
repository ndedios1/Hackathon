import turtle
import random
class Lsystem:
    """
        Reads through a file to initialize an L-system
        args: filename (str)
        return: None
    """
    def __init__(self,filename):
        try:
            self.lsys = open(filename, "r")
        except FileNotFoundError:
            print("File Doesn't Exist")
        else:
            self.angle = int(self.lsys.readline())
            self.iteration = int(self.lsys.readline())
            self.distance = int(self.lsys.readline())
            self.axiom = self.lsys.readline()
            self.rules = {}
            self.state = []
            while True:
                rul = self.lsys.readline()
                if not rul:
                    break
                symbol = rul[0]
                sub = rul[4:(len(rul)-1)]
                self.rules[symbol] = sub
            self.lsys.close()

    """
        Creates an L-System
        args: None
        return: None
    """
    def createLsystem(self):
        self.result = self.axiom
        for i in range(self.iteration):
            accum = ""
            for c in self.result:
                ch = self.applyRules(c)
                if ch == None:
                    accum += c
                else:
                    accum += ch
            self.result = accum

    """
        Returns the corresponding rule to string passed
        args: string
        return: The value of self.rules[string]
    """
    def applyRules(self,string):
        return self.rules.get(string)

    """
        Draws a visualization of the L-system
        args: snap (turtle)
        return: None
    """
    def drawLSystem(self,snap,listOfColors):
        for ch in self.result:
            if(ch == "F"):
                snap.forward(self.distance)
                snap.pencolor(listOfColors[random.randint(0, len(listOfColors)-1)])
            elif(ch == "+"):
                snap.right(self.angle)
            elif(ch == "-"):
                snap.left(self.angle)
            elif(ch == "["):
                self.state.append({k:v for (k,v) in snap.__dict__.items()})
            elif(ch == "]"):
                snap.__dict__ = self.state.pop()
