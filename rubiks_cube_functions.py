from colorama import init, Back, Style, Fore
init(autoreset=True)
import random

class Cube():
    
    def __init__(self, front = ["g", "g", "g", "g", "g", "g", "g", "g", "g"], left = ["o", "o", "o", "o", "o", "o", "o", "o", "o"], 
                right = ["r", "r", "r", "r", "r", "r", "r", "r", "r"], back = ["b", "b", "b", "b", "b", "b", "b", "b", "b"], 
                top = ["w", "w", "w", "w", "w", "w", "w", "w", "w"], bottom = ["y", "y", "y", "y", "y", "y", "y", "y", "y"]):
        self.frontColors = front.copy()
        self.leftColors = left.copy()
        self.rightColors = right.copy()
        self.backColors = back.copy()
        self.topColors = top.copy()
        self.bottomColors = bottom.copy()
        
        self.turns = {"r":self.r,"r'":self.rPrime,"r2":self.r2,"l":self.l,"l'":self.lPrime,"l2":self.l2,"f":self.f,"f'":self.fPrime,"f2":self.f2,"b":self.b,"b'":self.bPrime,"b2":self.b2,
                "u":self.u,"u'":self.uPrime,"u2":self.u2,"d":self.d,"d'":self.dPrime,"d2":self.d2}
    
    def printCube(self):
        printColors = {"g":Back.GREEN + " " + Back.RESET, "o":Back.YELLOW + " " + Back.RESET, "r":Back.RED + " " + Back.RESET,
                "b":Back.BLUE + " " + Back.RESET, "w":Back.WHITE + " " + Back.RESET, "y":Fore.YELLOW + Back.YELLOW + Style.BRIGHT + 
                "Y" + Back.RESET + Style.RESET_ALL + Fore.RESET, " ":" ", "X":"X", "x":"x"}
        
        print("       [" + printColors[self.backColors[0]] + " " + printColors[self.backColors[1]] + " " + printColors[self.backColors[2]] + "]")
        print("       [" + printColors[self.backColors[3]] + " " + printColors[self.backColors[4]] + " " + printColors[self.backColors[5]] + "]")
        print("       [" + printColors[self.backColors[6]] + " " + printColors[self.backColors[7]] + " " + printColors[self.backColors[8]] + "]")
        print("[" + printColors[self.leftColors[0]] + " " + printColors[self.leftColors[1]] + " " + printColors[self.leftColors[2]] + "]" +
                "[" + printColors[self.topColors[0]] + " " + printColors[self.topColors[1]] + " " + printColors[self.topColors[2]] + "]" +
                "[" + printColors[self.rightColors[0]] + " " + printColors[self.rightColors[1]] + " " + printColors[self.rightColors[2]] + "]")
        print("[" + printColors[self.leftColors[3]] + " " + printColors[self.leftColors[4]] + " " + printColors[self.leftColors[5]] + "]" +
                "[" + printColors[self.topColors[3]] + " " + printColors[self.topColors[4]] + " " + printColors[self.topColors[5]] + "]" +
                "[" + printColors[self.rightColors[3]] + " " + printColors[self.rightColors[4]] + " " + printColors[self.rightColors[5]] + "]")
        print("[" + printColors[self.leftColors[6]] + " " + printColors[self.leftColors[7]] + " " + printColors[self.leftColors[8]] + "]" +
                "[" + printColors[self.topColors[6]] + " " + printColors[self.topColors[7]] + " " + printColors[self.topColors[8]] + "]" +
                "[" + printColors[self.rightColors[6]] + " " + printColors[self.rightColors[7]] + " " + printColors[self.rightColors[8]] + "]")
        print("       [" + printColors[self.frontColors[0]] + " " + printColors[self.frontColors[1]] + " " + printColors[self.frontColors[2]] + "]")
        print("       [" + printColors[self.frontColors[3]] + " " + printColors[self.frontColors[4]] + " " + printColors[self.frontColors[5]] + "]")
        print("       [" + printColors[self.frontColors[6]] + " " + printColors[self.frontColors[7]] + " " + printColors[self.frontColors[8]] + "]")
        print("       [" + printColors[self.bottomColors[0]] + " " + printColors[self.bottomColors[1]] + " " + printColors[self.bottomColors[2]] + "]")
        print("       [" + printColors[self.bottomColors[3]] + " " + printColors[self.bottomColors[4]] + " " + printColors[self.bottomColors[5]] + "]")
        print("       [" + printColors[self.bottomColors[6]] + " " + printColors[self.bottomColors[7]] + " " + printColors[self.bottomColors[8]] + "]")
    
    def r(self):
        
        oldRightColors = self.rightColors.copy()
        oldFrontColors = self.frontColors.copy()
        oldBackColors = self.backColors.copy()
        oldTopColors = self.topColors.copy()
        oldBottomColors = self.bottomColors.copy()
        
        self.rightColors[0] = oldRightColors[6]
        self.rightColors[1] = oldRightColors[3]
        self.rightColors[2] = oldRightColors[0]
        self.rightColors[3] = oldRightColors[7]
        self.rightColors[5] = oldRightColors[1]
        self.rightColors[6] = oldRightColors[8]
        self.rightColors[7] = oldRightColors[5]
        self.rightColors[8] = oldRightColors[2]
        
        self.topColors[2] = oldFrontColors[2]
        self.topColors[5] = oldFrontColors[5]
        self.topColors[8] = oldFrontColors[8]
        
        self.frontColors[2] = oldBottomColors[2]
        self.frontColors[5] = oldBottomColors[5]
        self.frontColors[8] = oldBottomColors[8]
        
        self.bottomColors[2] = oldBackColors[2]
        self.bottomColors[5] = oldBackColors[5]
        self.bottomColors[8] = oldBackColors[8]
        
        self.backColors[2] = oldTopColors[2]
        self.backColors[5] = oldTopColors[5]
        self.backColors[8] = oldTopColors[8]
        
    def rPrime(self):
        
        oldRightColors = self.rightColors.copy()
        oldFrontColors = self.frontColors.copy()
        oldBackColors = self.backColors.copy()
        oldTopColors = self.topColors.copy()
        oldBottomColors = self.bottomColors.copy()
        
        self.rightColors[0] = oldRightColors[2]
        self.rightColors[1] = oldRightColors[5]
        self.rightColors[2] = oldRightColors[8]
        self.rightColors[3] = oldRightColors[1]
        self.rightColors[5] = oldRightColors[7]
        self.rightColors[6] = oldRightColors[0]
        self.rightColors[7] = oldRightColors[3]
        self.rightColors[8] = oldRightColors[6]
        
        self.topColors[2] = oldBackColors[2]
        self.topColors[5] = oldBackColors[5]
        self.topColors[8] = oldBackColors[8]
        
        self.frontColors[2] = oldTopColors[2]
        self.frontColors[5] = oldTopColors[5]
        self.frontColors[8] = oldTopColors[8]
        
        self.bottomColors[2] = oldFrontColors[2]
        self.bottomColors[5] = oldFrontColors[5]
        self.bottomColors[8] = oldFrontColors[8]
        
        self.backColors[2] = oldBottomColors[2]
        self.backColors[5] = oldBottomColors[5]
        self.backColors[8] = oldBottomColors[8]
    
    def r2(self):
        self.r()
        self.r()
    
    def l(self):
        
        oldLeftColors = self.leftColors.copy()
        oldFrontColors = self.frontColors.copy()
        oldBackColors = self.backColors.copy()
        oldTopColors = self.topColors.copy()
        oldBottomColors = self.bottomColors.copy()
        
        self.leftColors[0] = oldLeftColors[6]
        self.leftColors[1] = oldLeftColors[3]
        self.leftColors[2] = oldLeftColors[0]
        self.leftColors[3] = oldLeftColors[7]
        self.leftColors[5] = oldLeftColors[1]
        self.leftColors[6] = oldLeftColors[8]
        self.leftColors[7] = oldLeftColors[5]
        self.leftColors[8] = oldLeftColors[2]
        
        self.topColors[0] = oldBackColors[0]
        self.topColors[3] = oldBackColors[3]
        self.topColors[6] = oldBackColors[6]
        
        self.frontColors[0] = oldTopColors[0]
        self.frontColors[3] = oldTopColors[3]
        self.frontColors[6] = oldTopColors[6]
        
        self.bottomColors[0] = oldFrontColors[0]
        self.bottomColors[3] = oldFrontColors[3]
        self.bottomColors[6] = oldFrontColors[6]
        
        self.backColors[0] = oldBottomColors[0]
        self.backColors[3] = oldBottomColors[3]
        self.backColors[6] = oldBottomColors[6]
    
    def lPrime(self):
        
        oldLeftColors = self.leftColors.copy()
        oldFrontColors = self.frontColors.copy()
        oldBackColors = self.backColors.copy()
        oldTopColors = self.topColors.copy()
        oldBottomColors = self.bottomColors.copy()
        
        self.leftColors[0] = oldLeftColors[2]
        self.leftColors[1] = oldLeftColors[5]
        self.leftColors[2] = oldLeftColors[8]
        self.leftColors[3] = oldLeftColors[1]
        self.leftColors[5] = oldLeftColors[7]
        self.leftColors[6] = oldLeftColors[0]
        self.leftColors[7] = oldLeftColors[3]
        self.leftColors[8] = oldLeftColors[6]
        
        self.topColors[0] = oldFrontColors[0]
        self.topColors[3] = oldFrontColors[3]
        self.topColors[6] = oldFrontColors[6]
        
        self.frontColors[0] = oldBottomColors[0]
        self.frontColors[3] = oldBottomColors[3]
        self.frontColors[6] = oldBottomColors[6]
        
        self.bottomColors[0] = oldBackColors[0]
        self.bottomColors[3] = oldBackColors[3]
        self.bottomColors[6] = oldBackColors[6]
        
        self.backColors[0] = oldTopColors[0]
        self.backColors[3] = oldTopColors[3]
        self.backColors[6] = oldTopColors[6]
        
    def l2(self):
        self.l()
        self.l()
        
    def f(self):
        
        oldLeftColors = self.leftColors.copy()
        oldFrontColors = self.frontColors.copy()
        oldRightColors = self.rightColors.copy()
        oldTopColors = self.topColors.copy()
        oldBottomColors = self.bottomColors.copy()
        
        self.frontColors[0] = oldFrontColors[6]
        self.frontColors[1] = oldFrontColors[3]
        self.frontColors[2] = oldFrontColors[0]
        self.frontColors[3] = oldFrontColors[7]
        self.frontColors[5] = oldFrontColors[1]
        self.frontColors[6] = oldFrontColors[8]
        self.frontColors[7] = oldFrontColors[5]
        self.frontColors[8] = oldFrontColors[2]
        
        self.topColors[6] = oldLeftColors[6]
        self.topColors[7] = oldLeftColors[7]
        self.topColors[8] = oldLeftColors[8]
        
        self.leftColors[6] = oldBottomColors[2]
        self.leftColors[7] = oldBottomColors[1]
        self.leftColors[8] = oldBottomColors[0]
        
        self.bottomColors[2] = oldRightColors[6]
        self.bottomColors[1] = oldRightColors[7]
        self.bottomColors[0] = oldRightColors[8]
        
        self.rightColors[6] = oldTopColors[6]
        self.rightColors[7] = oldTopColors[7]
        self.rightColors[8] = oldTopColors[8]
        
    def fPrime(self):
        
        oldLeftColors = self.leftColors.copy()
        oldFrontColors = self.frontColors.copy()
        oldRightColors = self.rightColors.copy()
        oldTopColors = self.topColors.copy()
        oldBottomColors = self.bottomColors.copy()
        
        self.frontColors[0] = oldFrontColors[2]
        self.frontColors[1] = oldFrontColors[5]
        self.frontColors[2] = oldFrontColors[8]
        self.frontColors[3] = oldFrontColors[1]
        self.frontColors[5] = oldFrontColors[7]
        self.frontColors[6] = oldFrontColors[0]
        self.frontColors[7] = oldFrontColors[3]
        self.frontColors[8] = oldFrontColors[6]
        
        self.topColors[6] = oldRightColors[6]
        self.topColors[7] = oldRightColors[7]
        self.topColors[8] = oldRightColors[8]
        
        self.leftColors[6] = oldTopColors[6]
        self.leftColors[7] = oldTopColors[7]
        self.leftColors[8] = oldTopColors[8]
        
        self.bottomColors[2] = oldLeftColors[6]
        self.bottomColors[1] = oldLeftColors[7]
        self.bottomColors[0] = oldLeftColors[8]
        
        self.rightColors[6] = oldBottomColors[2]
        self.rightColors[7] = oldBottomColors[1]
        self.rightColors[8] = oldBottomColors[0]
    
    def f2(self):
        self.f()
        self.f()
    
    def b(self):
        
        oldLeftColors = self.leftColors.copy()
        oldBackColors = self.backColors.copy()
        oldRightColors = self.rightColors.copy()
        oldTopColors = self.topColors.copy()
        oldBottomColors = self.bottomColors.copy()
        
        self.backColors[0] = oldBackColors[6]
        self.backColors[1] = oldBackColors[3]
        self.backColors[2] = oldBackColors[0]
        self.backColors[3] = oldBackColors[7]
        self.backColors[5] = oldBackColors[1]
        self.backColors[6] = oldBackColors[8]
        self.backColors[7] = oldBackColors[5]
        self.backColors[8] = oldBackColors[2]
        
        self.topColors[0] = oldRightColors[0]
        self.topColors[1] = oldRightColors[1]
        self.topColors[2] = oldRightColors[2]
        
        self.leftColors[0] = oldTopColors[0]
        self.leftColors[1] = oldTopColors[1]
        self.leftColors[2] = oldTopColors[2]
        
        self.bottomColors[6] = oldLeftColors[2]
        self.bottomColors[7] = oldLeftColors[1]
        self.bottomColors[8] = oldLeftColors[0]
        
        self.rightColors[0] = oldBottomColors[8]
        self.rightColors[1] = oldBottomColors[7]
        self.rightColors[2] = oldBottomColors[6]
    
    def bPrime(self):
        
        oldLeftColors = self.leftColors.copy()
        oldBackColors = self.backColors.copy()
        oldRightColors = self.rightColors.copy()
        oldTopColors = self.topColors.copy()
        oldBottomColors = self.bottomColors.copy()
        
        self.backColors[0] = oldBackColors[2]
        self.backColors[1] = oldBackColors[5]
        self.backColors[2] = oldBackColors[8]
        self.backColors[3] = oldBackColors[1]
        self.backColors[5] = oldBackColors[7]
        self.backColors[6] = oldBackColors[0]
        self.backColors[7] = oldBackColors[3]
        self.backColors[8] = oldBackColors[6]
        
        self.topColors[0] = oldLeftColors[0]
        self.topColors[1] = oldLeftColors[1]
        self.topColors[2] = oldLeftColors[2]
        
        self.leftColors[0] = oldBottomColors[8]
        self.leftColors[1] = oldBottomColors[7]
        self.leftColors[2] = oldBottomColors[6]
        
        self.bottomColors[6] = oldRightColors[2]
        self.bottomColors[7] = oldRightColors[1]
        self.bottomColors[8] = oldRightColors[0]
        
        self.rightColors[0] = oldTopColors[0]
        self.rightColors[1] = oldTopColors[1]
        self.rightColors[2] = oldTopColors[2]
    
    def b2(self):
        self.b()
        self.b()
    
    def u(self):
        
        oldLeftColors = self.leftColors.copy()
        oldBackColors = self.backColors.copy()
        oldRightColors = self.rightColors.copy()
        oldTopColors = self.topColors.copy()
        oldFrontColors = self.frontColors.copy()
        
        self.topColors[0] = oldTopColors[6]
        self.topColors[1] = oldTopColors[3]
        self.topColors[2] = oldTopColors[0]
        self.topColors[3] = oldTopColors[7]
        self.topColors[5] = oldTopColors[1]
        self.topColors[6] = oldTopColors[8]
        self.topColors[7] = oldTopColors[5]
        self.topColors[8] = oldTopColors[2]
        
        self.frontColors[0] = oldRightColors[6]
        self.frontColors[1] = oldRightColors[3]
        self.frontColors[2] = oldRightColors[0]
        
        self.leftColors[2] = oldFrontColors[0]
        self.leftColors[5] = oldFrontColors[1]
        self.leftColors[8] = oldFrontColors[2]
        
        self.backColors[6] = oldLeftColors[8]
        self.backColors[7] = oldLeftColors[5]
        self.backColors[8] = oldLeftColors[2]
        
        self.rightColors[0] = oldBackColors[6]
        self.rightColors[3] = oldBackColors[7]
        self.rightColors[6] = oldBackColors[8]
        
    def uPrime(self):
        
        oldLeftColors = self.leftColors.copy()
        oldBackColors = self.backColors.copy()
        oldRightColors = self.rightColors.copy()
        oldTopColors = self.topColors.copy()
        oldFrontColors = self.frontColors.copy()
        
        self.topColors[0] = oldTopColors[2]
        self.topColors[1] = oldTopColors[5]
        self.topColors[2] = oldTopColors[8]
        self.topColors[3] = oldTopColors[1]
        self.topColors[5] = oldTopColors[7]
        self.topColors[6] = oldTopColors[0]
        self.topColors[7] = oldTopColors[3]
        self.topColors[8] = oldTopColors[6]
        
        self.frontColors[0] = oldLeftColors[2]
        self.frontColors[1] = oldLeftColors[5]
        self.frontColors[2] = oldLeftColors[8]
        
        self.leftColors[2] = oldBackColors[8]
        self.leftColors[5] = oldBackColors[7]
        self.leftColors[8] = oldBackColors[6]
        
        self.backColors[6] = oldRightColors[0]
        self.backColors[7] = oldRightColors[3]
        self.backColors[8] = oldRightColors[6]
        
        self.rightColors[0] = oldFrontColors[2]
        self.rightColors[3] = oldFrontColors[1]
        self.rightColors[6] = oldFrontColors[0]
    
    def u2(self):
        self.u()
        self.u()
    
    def d(self):
        
        oldLeftColors = self.leftColors.copy()
        oldBackColors = self.backColors.copy()
        oldRightColors = self.rightColors.copy()
        oldBottomColors = self.bottomColors.copy()
        oldFrontColors = self.frontColors.copy()
        
        self.bottomColors[0] = oldBottomColors[6]
        self.bottomColors[1] = oldBottomColors[3]
        self.bottomColors[2] = oldBottomColors[0]
        self.bottomColors[3] = oldBottomColors[7]
        self.bottomColors[5] = oldBottomColors[1]
        self.bottomColors[6] = oldBottomColors[8]
        self.bottomColors[7] = oldBottomColors[5]
        self.bottomColors[8] = oldBottomColors[2]
        
        self.frontColors[6] = oldLeftColors[0]
        self.frontColors[7] = oldLeftColors[3]
        self.frontColors[8] = oldLeftColors[6]
        
        self.leftColors[0] = oldBackColors[2]
        self.leftColors[3] = oldBackColors[1]
        self.leftColors[6] = oldBackColors[0]
        
        self.backColors[2] = oldRightColors[8]
        self.backColors[1] = oldRightColors[5]
        self.backColors[0] = oldRightColors[2]
        
        self.rightColors[8] = oldFrontColors[6]
        self.rightColors[5] = oldFrontColors[7]
        self.rightColors[2] = oldFrontColors[8]
    
    def dPrime(self):
        
        oldLeftColors = self.leftColors.copy()
        oldBackColors = self.backColors.copy()
        oldRightColors = self.rightColors.copy()
        oldBottomColors = self.bottomColors.copy()
        oldFrontColors = self.frontColors.copy()
        
        self.bottomColors[0] = oldBottomColors[2]
        self.bottomColors[1] = oldBottomColors[5]
        self.bottomColors[2] = oldBottomColors[8]
        self.bottomColors[3] = oldBottomColors[1]
        self.bottomColors[5] = oldBottomColors[7]
        self.bottomColors[6] = oldBottomColors[0]
        self.bottomColors[7] = oldBottomColors[3]
        self.bottomColors[8] = oldBottomColors[6]
        
        self.frontColors[6] = oldRightColors[8]
        self.frontColors[7] = oldRightColors[5]
        self.frontColors[8] = oldRightColors[2]
        
        self.leftColors[0] = oldFrontColors[6]
        self.leftColors[3] = oldFrontColors[7]
        self.leftColors[6] = oldFrontColors[8]
        
        self.backColors[2] = oldLeftColors[0]
        self.backColors[1] = oldLeftColors[3]
        self.backColors[0] = oldLeftColors[6]
        
        self.rightColors[8] = oldBackColors[2]
        self.rightColors[5] = oldBackColors[1]
        self.rightColors[2] = oldBackColors[0]
    
    def d2(self):
        self.d()
        self.d()
    
    def __eq__(self, other):
        for i in range(9):
            if self.frontColors[i] != other.frontColors[i] and other.frontColors[i] != "x":
                return False
            if self.leftColors[i] != other.leftColors[i] and other.leftColors[i] != "x":
                return False
            if self.rightColors[i] != other.rightColors[i] and other.rightColors[i] != "x":
                return False
            if self.backColors[i] != other.backColors[i] and other.backColors[i] != "x":
                return False
            if self.topColors[i] != other.topColors[i] and other.topColors[i] != "x":
                return False
            if self.bottomColors[i] != other.bottomColors[i] and other.bottomColors[i] != "x":
                return False
        return True
    
    def scramble(self):
        possibleMoves = ["r","r'","r2","l","l'","l2","u","u'","u2","d","d'","d2","f","f'","f2","b","b'","b2"]
        
        for i in range(0,35):
            n = random.randint(0,len(possibleMoves)-1)
            self.move(possibleMoves[n])
        
    def solve(self):
        self.frontColors = ["g", "g", "g", "g", "g", "g", "g", "g", "g"]
        self.leftColors = ["o", "o", "o", "o", "o", "o", "o", "o", "o"]
        self.rightColors = ["r", "r", "r", "r", "r", "r", "r", "r", "r"]
        self.backColors = ["b", "b", "b", "b", "b", "b", "b", "b", "b"]
        self.topColors = ["w", "w", "w", "w", "w", "w", "w", "w", "w"]
        self.bottomColors = ["y", "y", "y", "y", "y", "y", "y", "y", "y"]
    
    def inputCube(self):
        print('Type the first letter of the color of each piece starting from top to bottom. Type "cancel" to return to main cube.\n')
        
        startingFrontColors = self.frontColors.copy()
        startingLeftColors = self.leftColors.copy()
        startingRightColors = self.rightColors.copy()
        startingBackColors = self.backColors.copy()
        startingTopColors = self.topColors.copy()
        startingBottomColors = self.bottomColors.copy()
        
        colorsLeft = {"g":9, "o":9, "r":9, "b":9, "w":9, "y":9}
        self.frontColors = []
        self.leftColors = []
        self.rightColors = []
        self.backColors = []
        self.topColors = []
        self.bottomColors = []
        
        while True:
            numMissingFront = 9 - len(self.frontColors)
            for n in range(0, numMissingFront):
                self.frontColors.append(" ")
            numMissingLeft = 9 - len(self.leftColors)
            for n in range(numMissingLeft):
                self.leftColors.append(" ")
            numMissingRight = 9 - len(self.rightColors)
            for n in range(numMissingRight):
                self.rightColors.append(" ")
            numMissingBack = 9 - len(self.backColors)
            for n in range(numMissingBack):
                self.backColors.append(" ")
            numMissingTop = 9 - len(self.topColors)
            for n in range(numMissingTop):
                self.topColors.append(" ")
            numMissingBottom = 9 - len(self.bottomColors)
            for n in range(numMissingBottom):
                self.bottomColors.append(" ")
            self.printCube()
            del self.frontColors[9-numMissingFront:10]
            del self.leftColors[9-numMissingLeft:10]
            del self.rightColors[9-numMissingRight:10]
            del self.backColors[9-numMissingBack:10]
            del self.topColors[9-numMissingTop:10]
            del self.bottomColors[9-numMissingBottom:10]
            
            color = input("Next Color: ")
            if color == "cancel":
                self.frontColors = startingFrontColors.copy()
                self.leftColors = startingLeftColors.copy()
                self.rightColors = startingRightColors.copy()
                self.backColors = startingBackColors.copy()
                self.topColors = startingTopColors.copy()
                self.bottomColors = startingBottomColors.copy()
                break
            try:
                if colorsLeft[color] > 0:
                    if len(self.backColors) < 9:
                        self.backColors.append(color)
                    elif len(self.leftColors) < 9:
                        self.leftColors.append(color)
                    elif len(self.topColors) < 9:
                        self.topColors.append(color)
                    elif len(self.rightColors) < 9:
                        self.rightColors.append(color)
                    elif len(self.frontColors) < 9:
                        self.frontColors.append(color)
                    elif len(self.bottomColors) < 9:
                        self.bottomColors.append(color)
                    colorsLeft[color] -= 1
                else:
                    print("You have already used 9 of this this color.")
            except:
                print("Invalid Color")
            if len(self.backColors) == 9 and len(self.leftColors) == 9 and len(self.topColors) == 9 and len(self.rightColors) == 9 and len(self.frontColors) == 9 and len(self.bottomColors) == 9:
                break

    def alg(self, alg):
        for move in alg.split(" "):
            self.move(move)
    
    def move(self, move):
        try:
            if move[-1] == "'":
                getattr(self, move[0].lower() + "Prime")()
            else:
                getattr(self, move.strip().lower())()
            # self.turns[move.strip().lower()]()
        except:
            if move == "scramble":
                self.scramble()
            elif move == "solve":
                self.solve()
            elif move == "input cube":
                self.inputCube()
            else:
                print("Invalid Command")
