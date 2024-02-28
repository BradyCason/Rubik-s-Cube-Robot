from rubiks_cube_functions import Cube
from colorama import init, Back, Style, Fore
init(autoreset=True)
import copy

Cube = Cube()
moves = ["r","f","u","b","l","d","d'","l'","b'","u'","f'","r'"]

def GetCubePositions():
    Cube.frontColors = [" ", " ", " ", " ", "g", " ", " ", " ", " "]
    Cube.leftColors = [" ", " ", " ", " ", "o", " ", " ", " ", " "]
    Cube.rightColors = [" ", " ", " ", " ", "r", " ", " ", " ", " "]
    Cube.backColors = [" ", " ", " ", " ", "b", " ", " ", " ", " "]
    Cube.topColors = [" ", " ", " ", " ", "w", " ", " ", " ", " "]
    Cube.bottomColors = [" ", " ", " ", " ", "y", " ", " ", " ", " "]
    
    print("Type the letter of the color that is on the X.")
    #Get back colors
    for i in range(9):
        if i != 4:
            moveOn = False
            while moveOn == False:
                Cube.backColors[i] = "X"
                Cube.printCube()
                
                letter = input("Color of X: ")
                if letter in ["g","o","r","b","w","y"]:
                    Cube.backColors[i] = letter
                    moveOn = True
    #Get left colors
    for i in range(9):
        if i != 4:
            moveOn = False
            while moveOn == False:
                Cube.leftColors[i] = "X"
                Cube.printCube()
                
                letter = input("Color of X: ")
                if letter in ["g","o","r","b","w","y"]:
                    Cube.leftColors[i] = letter
                    moveOn = True
    #Get top colors
    for i in range(9):
        if i != 4:
            moveOn = False
            while moveOn == False:
                Cube.topColors[i] = "X"
                Cube.printCube()
                
                letter = input("Color of X: ")
                if letter in ["g","o","r","b","w","y"]:
                    Cube.topColors[i] = letter
                    moveOn = True
    #Get right colors
    for i in range(9):
        if i != 4:
            moveOn = False
            while moveOn == False:
                Cube.rightColors[i] = "X"
                Cube.printCube()
                
                letter = input("Color of X: ")
                if letter in ["g","o","r","b","w","y"]:
                    Cube.rightColors[i] = letter
                    moveOn = True
    #Get front colors
    for i in range(9):
        if i != 4:
            moveOn = False
            while moveOn == False:
                Cube.frontColors[i] = "X"
                Cube.printCube()
                
                letter = input("Color of X: ")
                if letter in ["g","o","r","b","w","y"]:
                    Cube.frontColors[i] = letter
                    moveOn = True
    #Get bottom colors
    for i in range(9):
        if i != 4:
            moveOn = False
            while moveOn == False:
                Cube.bottomColors[i] = "X"
                Cube.printCube()
                
                letter = input("Color of X: ")
                if letter in ["g","o","r","b","w","y"]:
                    Cube.bottomColors[i] = letter
                    moveOn = True
    
def CubeIsTarget(Cube, targetTop, targetBottom, targetFront, targetBack, targetLeft, targetRight):
    equalsTarget = True
    
    for i in range(9):
        if Cube.topColors[i] != targetTop[i] and targetTop[i] != " ":
            equalsTarget = False
    for i in range(9):
        if Cube.bottomColors[i] != targetBottom[i] and targetBottom[i] != " ":
            equalsTarget = False
    for i in range(9):
        if Cube.frontColors[i] != targetFront[i] and targetFront[i] != " ":
            equalsTarget = False
    for i in range(9):
        if Cube.backColors[i] != targetBack[i] and targetBack[i] != " ":
            equalsTarget = False
    for i in range(9):
        if Cube.rightColors[i] != targetRight[i] and targetRight[i] != " ":
            equalsTarget = False
    for i in range(9):
        if Cube.leftColors[i] != targetLeft[i] and targetLeft[i] != " ":
            equalsTarget = False
    
            
    return equalsTarget

def Simulate(depth, targetTop, targetBottom, targetFront, targetBack, targetLeft, targetRight):
    depth -= 1
    
    currentBottom = copy.copy(Cube.bottomColors)
    currentTop = copy.copy(Cube.topColors)
    currentRight = copy.copy(Cube.rightColors)
    currentLeft = copy.copy(Cube.leftColors)
    currentFront = copy.copy(Cube.frontColors)
    currentBack = copy.copy(Cube.backColors)
    
    #Do all moves
    for move in moves:
        Cube.move(move)
        
        #Check if at target
        if CubeIsTarget(Cube, targetTop, targetBottom, targetFront, targetBack, targetLeft, targetRight):
            return move
        else:
            #Repeat
            if depth > 0:
                result = Simulate(depth, targetTop, targetBottom, targetFront, targetBack, targetLeft, targetRight)
                if result != "":
                    return move + result
        
        #undo move
        Cube.bottomColors = copy.copy(currentBottom)
        Cube.topColors = copy.copy(currentTop)
        Cube.rightColors = copy.copy(currentRight)
        Cube.leftColors = copy.copy(currentLeft)
        Cube.frontColors = copy.copy(currentFront)
        Cube.backColors = copy.copy(currentBack)
    
    #Return solution up until here
    return ""

GetCubePositions()

#Find Cross
print("Searching for cross solution")
solution = Simulate(8, [" ", " ", " ", " ", "w", " ", " ", " ", " "], [" ", "y", " ", "y", "y", "y", " ", "y", " "], [" ", " ", " ", " ", "g", " ", " ", "g", " "], 
        [" ", "b", " ", " ", "b", " ", " ", " ", " "], [" ", " ", " ", "o", "o", " ", " ", " ", " "], [" ", " ", " ", " ", "r", "r", " ", " ", " "])
if solution == "":
    solution = "No Solution"
else:
    print("Cross Solution: " + solution)
    
    #Find first pair
    print("Searching for first f2l piece")
    solution = Simulate(8, [" ", " ", " ", " ", "w", " ", " ", " ", " "], ["y", "y", " ", "y", "y", "y", " ", "y", " "], [" ", " ", " ", " ", "g", " ", "g", "g", " "], 
            [" ", "b", " ", " ", "b", " ", " ", " ", " "], [" ", " ", " ", "o", "o", " ", "o", " ", " "], [" ", " ", " ", " ", "r", "r", " ", " ", " "])
    if solution == "":
        solution = "No Solution"
    else:
        print("First f2l piece Solution: " + solution)

'''
o
b
y
w
y
r
b
o
b
g
b
r
g
w
r
g
w
r
b
o
r
o
w
g
y
b
b
w
o
r
b
o
w
o
y
y
o
r
g
y
g
y
g
g
y
w
w
r
'''
