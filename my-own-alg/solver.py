from rubiks_cube_functions import Cube
from collections import deque
import time
import copy
import csv

oppSides = {"r":"l","l":"r","b":"f","f":"b","u":"d","d":"u"}

def reverseActions(actions):
    reversedActions = []
    for a in reversed(actions):
        if a[-1] == "2":
            reversedActions.append(a)
        elif a[-1] == "'":
            reversedActions.append(a[0])
        else:
            reversedActions.append(a + "'")
    return reversedActions

def getSolution(cube, targetCube, maxNumMoves, moves=["r","r'","l","l'","u","u'","d","d'","f","f'","b","b'","r2","l2","u2","f2","d2","b2"]):
    ''' Breadth first search of all possible moves. '''

    if cube == targetCube:
        return [""]

    # Create target Cubes
    targetCubes = [targetCube]
    targetCubesMoves = [[]]
    queue = deque([[x] for x in moves])
    while queue:
        actions = queue.popleft()

        # Do the actions
        for action in actions:
            targetCube.move(action)

        # Check if solved
        if cube == targetCube:
            return reverseActions(actions)

        # Add new target cube
        reversedActions = reverseActions(actions)
        if len(targetCubesMoves[-1]) < len(reversedActions):
            targetCubes = [copy.deepcopy(targetCube)]
            targetCubesMoves = [reversedActions]
        else:
            targetCubes.append(copy.deepcopy(targetCube))
            targetCubesMoves.append(reversedActions)

        # Undo the actions
        for action in reversedActions:
            targetCube.move(action)

        # Add new cases to the queue
        for move in moves:
            if move[0] != actions[-1][0] and len(actions) < min(maxNumMoves, 3):
                if len(actions) >= 2:
                    if move[0] != actions[-2][0] or oppSides[move[0]] != actions[-1][0]:
                        queue.append(actions + [move])
                else:
                    queue.append(actions + [move])
    
    queue = deque([[x] for x in moves])
    while queue:
        actions = queue.popleft()

        # Do the actions
        for action in actions:
            cube.move(action)

        # Check if solved
        for tCube in targetCubes:
            if cube == tCube:
                return actions + targetCubesMoves[targetCubes.index(tCube)]

        # Undo the actions
        for action in reverseActions(actions):
            cube.move(action)

        # Add new cases to the queue
        for move in moves:
            if move[0] != actions[-1][0] and len(actions) < maxNumMoves - 3:
                if len(actions) >= 2:
                    if move[0] != actions[-2][0] or oppSides[move[0]] != actions[-1][0]:
                        queue.append(actions + [move])
                else:
                    queue.append(actions + [move])



def oll(cube, csvFileName):
    cubeMap = [cube.frontColors[0], cube.frontColors[1], cube.frontColors[2], cube.rightColors[6], cube.rightColors[3],
               cube.rightColors[0], cube.backColors[8], cube.backColors[7], cube.backColors[6], cube.leftColors[2],
               cube.leftColors[5], cube.leftColors[8]]
    cubePattern = ""
    for i in range(12):
        if cubeMap[i] == "w":
            cubePattern += "1"
        else:
            cubePattern += "0"
    print(cubePattern)

    with open(csvFileName, "r") as csvFile:
        reader = csv.DictReader(csvFile)
        algs = [x for x in reader]
        for alg in algs:
            alg["alg"] = eval(alg["alg"])

        for alg in algs:
            if alg["pattern"] == cubePattern:
                return alg["alg"]
            
def pll(cube, csvFileName):
    cubeMap = [cube.frontColors[0], cube.frontColors[1], cube.frontColors[2], cube.rightColors[6], cube.rightColors[3],
               cube.rightColors[0], cube.backColors[8], cube.backColors[7], cube.backColors[6], cube.leftColors[2],
               cube.leftColors[5], cube.leftColors[8]]
    cubePatterns = [""] * 24
    # 0:grbo 1:grob 2:gbro 3:gbor 4:gorb 5:gobr 6:rgob 7:rgbo 8:rogb 9:robg 10:rbog 11:rbgo 12:bgro 13:bgor 14:brgo 15:brog 16:bogr 17:borg 18:ogbr 19:ogrb 20:orbg 21:orgb 22:obgr 23:obrg
    for i in range(12):
        if cubeMap[i] == "g":
            cubePatterns[0] += "0"
            cubePatterns[1] += "0"
            cubePatterns[2] += "0"
            cubePatterns[3] += "0"
            cubePatterns[4] += "0"
            cubePatterns[5] += "0"
            cubePatterns[6] += "1"
            cubePatterns[7] += "1"
            cubePatterns[8] += "2"
            cubePatterns[9] += "3"
            cubePatterns[10] += "3"
            cubePatterns[11] += "2"
            cubePatterns[12] += "1"
            cubePatterns[13] += "1"
            cubePatterns[14] += "2"
            cubePatterns[15] += "3"
            cubePatterns[16] += "2"
            cubePatterns[17] += "3"
            cubePatterns[18] += "1"
            cubePatterns[19] += "1"
            cubePatterns[20] += "3"
            cubePatterns[21] += "2"
            cubePatterns[22] += "2"
            cubePatterns[23] += "3"
        elif cubeMap[i] == "r":
            cubePatterns[0] += "1"
            cubePatterns[1] += "1"
            cubePatterns[2] += "2"
            cubePatterns[3] += "3"
            cubePatterns[4] += "2"
            cubePatterns[5] += "3"
            cubePatterns[6] += "0"
            cubePatterns[7] += "0"
            cubePatterns[8] += "0"
            cubePatterns[9] += "0"
            cubePatterns[10] += "0"
            cubePatterns[11] += "0"
            cubePatterns[12] += "3"
            cubePatterns[13] += "3"
            cubePatterns[14] += "1"
            cubePatterns[15] += "1"
            cubePatterns[16] += "3"
            cubePatterns[17] += "2"
            cubePatterns[18] += "3"
            cubePatterns[19] += "2"
            cubePatterns[20] += "1"
            cubePatterns[21] += "1"
            cubePatterns[22] += "3"
            cubePatterns[23] += "2"
        elif cubeMap[i] == "o":
            cubePatterns[0] += "3"
            cubePatterns[1] += "2"
            cubePatterns[2] += "3"
            cubePatterns[3] += "2"
            cubePatterns[4] += "1"
            cubePatterns[5] += "1"
            cubePatterns[6] += "2"
            cubePatterns[7] += "3"
            cubePatterns[8] += "1"
            cubePatterns[9] += "1"
            cubePatterns[10] += "2"
            cubePatterns[11] += "3"
            cubePatterns[12] += "3"
            cubePatterns[13] += "2"
            cubePatterns[14] += "3"
            cubePatterns[15] += "2"
            cubePatterns[16] += "1"
            cubePatterns[17] += "1"
            cubePatterns[18] += "0"
            cubePatterns[19] += "0"
            cubePatterns[20] += "0"
            cubePatterns[21] += "0"
            cubePatterns[22] += "0"
            cubePatterns[23] += "0"
        else:
            cubePatterns[0] += "2"
            cubePatterns[1] += "3"
            cubePatterns[2] += "1"
            cubePatterns[3] += "1"
            cubePatterns[4] += "3"
            cubePatterns[5] += "2"
            cubePatterns[6] += "3"
            cubePatterns[7] += "2"
            cubePatterns[8] += "3"
            cubePatterns[9] += "2"
            cubePatterns[10] += "1"
            cubePatterns[11] += "1"
            cubePatterns[12] += "0"
            cubePatterns[13] += "0"
            cubePatterns[14] += "0"
            cubePatterns[15] += "0"
            cubePatterns[16] += "0"
            cubePatterns[17] += "0"
            cubePatterns[18] += "2"
            cubePatterns[19] += "3"
            cubePatterns[20] += "2"
            cubePatterns[21] += "3"
            cubePatterns[22] += "1"
            cubePatterns[23] += "1"

    with open(csvFileName, "r") as csvFile:
        reader = csv.DictReader(csvFile)
        algs = [x for x in reader]
        for alg in algs:
            alg["alg"] = eval(alg["alg"])

        for alg in algs:
            if alg["pattern"] in cubePatterns:
                return alg["alg"]

def reduceDups(lst):
    firstList = []
    for i in range(0, len(lst), 2):
        if len(lst) == i + 1:
            firstList.append(lst[i])
        elif lst[i][0] == lst[i+1][0]:
            if lst[i][-1] == "2":
                if lst[i+1][-1] == "'":
                    firstList.append(lst[i][0])
                elif lst[i+1][-1] != "2":
                    firstList.append(lst[i][0] + "'") 
            elif lst[i][-1] == "'":
                if lst[i+1][-1] == "'":
                    firstList.append(lst[i][0] + "2")
                elif lst[i+1][-1] == "2":
                    firstList.append(lst[i][0])
            else:
                if lst[i+1][-1] == "'":
                    pass
                elif lst[i+1][-1] == "2":
                    firstList.append(lst[i][0] + "'")
                else:
                    firstList.append(lst[i][0] + "2")
        else:
            firstList.append(lst[i])
            firstList.append(lst[i+1])

    returnList = [firstList[0]]
    for i in range(1, len(firstList), 2):
        if len(firstList) == i + 1:
            returnList.append(firstList[i])
        elif firstList[i][0] == firstList[i+1][0]:
            if firstList[i][-1] == "2":
                if firstList[i+1][-1] == "'":
                    returnList.append(firstList[i][0])
                elif firstList[i+1][-1] != "2":
                    returnList.append(firstList[i][0] + "'") 
            elif firstList[i][-1] == "'":
                if firstList[i+1][-1] == "'":
                    returnList.append(firstList[i][0] + "2")
                elif firstList[i+1][-1] == "2":
                    returnList.append(firstList[i][0])
            else:
                if firstList[i+1][-1] == "'":
                    pass
                elif firstList[i+1][-1] == "2":
                    returnList.append(firstList[i][0] + "'")
                else:
                    returnList.append(firstList[i][0] + "2")
        else:
            returnList.append(firstList[i])
            returnList.append(firstList[i+1])

    if returnList == lst:
        return returnList
    else:
        return reduceDups(returnList)

def combineSolutions(*args):
    origList = []
    for list in args:
        if origList:
            if list:
                origList.extend(list)
        else:
            origList = list
    return reduceDups(origList)

if __name__ == "__main__":
    # cube = Cube()
    # cube.move("r")
    # cube.move("u")
    # cube.move("r'")
    # cube.move("u'")
    # cube.move("r")
    # cube.move("u")
    # cube.move("r'")
    # print(getSolution(cube, Cube(), 8))

    # for i in range(1,9):
    #     times = []
    #     for j in range(5):
    #         start = time.perf_counter()
    #         getSolution(Cube(), Cube(right=["w","w","w","w","w","w","w","w","w"]), i)
    #         end = time.perf_counter()
    #         times.append(end - start)
    #     print(f"Avgerage time for {i} moves: {sum(times) / len(times)}")
    
    start = time.perf_counter()
    cube = Cube()
    cube.alg("U' L2 D' F2 U2 F2 U R2 U2 B2 L2 U2 F' U' R2 U L B2 L B' U2")
    originalCube = copy.deepcopy(cube)
    crossCube = Cube(front=["x","x","x","x","g","x","x","g","x"],
                     left=["x","x","x","o","o","x","x","x","x"],
                     right=["x","x","x","x","r","r","x","x","x"],
                     back=["x","b","x","x","b","x","x","x","x"],
                     top=["x","x","x","x","x","x","x","x","x"],
                     bottom=["x","y","x","y","y","y","x","y","x"],)
    crossSolution = getSolution(cube, crossCube, 8)
    print(crossSolution)
    
    for move in crossSolution:
        originalCube.move(move)
    originalCube.printCube()

    f2l1Cube = Cube(front=["x","x","x","x","g","g","x","g","g"],
                     left=["x","x","x","o","o","x","x","x","x"],
                     right=["x","x","x","x","r","r","x","r","r"],
                     back=["x","b","x","x","b","x","x","x","x"],
                     top=["x","x","x","x","x","x","x","x","x"],
                     bottom=["x","y","y","y","y","y","x","y","x"],)
    f2l1Sol = getSolution(copy.deepcopy(originalCube), f2l1Cube, 7)
    corner1Sol = []
    if not f2l1Sol:
        corner1Cube = Cube(front=["x","x","x","x","g","x","x","g","g"],
                         left=["x","x","x","o","o","x","x","x","x"],
                         right=["x","x","x","x","r","r","x","x","r"],
                         back=["x","b","x","x","b","x","x","x","x"],
                         top=["x","x","x","x","x","x","x","x","x"],
                         bottom=["x","y","y","y","y","y","x","y","x"],)
        corner1Sol = getSolution(copy.deepcopy(originalCube), corner1Cube, 7)
        print(corner1Sol)
        for move in corner1Sol:
            originalCube.move(move)
        f2l1Sol = getSolution(copy.deepcopy(originalCube), f2l1Cube, 7)
    print(f2l1Sol)
    for move in f2l1Sol:
        originalCube.move(move)
    originalCube.printCube()

    f2l2Cube = Cube(front=["x","x","x","g","g","g","g","g","g"],
                     left=["x","x","x","o","o","x","o","o","x"],
                     right=["x","x","x","x","r","r","x","r","r"],
                     back=["x","b","x","x","b","x","x","x","x"],
                     top=["x","x","x","x","x","x","x","x","x"],
                     bottom=["y","y","y","y","y","y","x","y","x"],)
    f2l2Sol = getSolution(copy.deepcopy(originalCube), f2l2Cube, 7)
    corner2Sol = []
    if not f2l2Sol:
        corner2Cube = Cube(front=["x","x","x","x","g","g","g","g","g"],
                         left=["x","x","x","o","o","x","o","x","x"],
                         right=["x","x","x","x","r","r","x","r","r"],
                         back=["x","b","x","x","b","x","x","x","x"],
                         top=["x","x","x","x","x","x","x","x","x"],
                         bottom=["y","y","y","y","y","y","x","y","x"],)
        corner2Sol = getSolution(copy.deepcopy(originalCube), corner2Cube, 7)
        print(corner2Sol)
        for move in corner2Sol:
            originalCube.move(move)
        f2l2Sol = getSolution(copy.deepcopy(originalCube), f2l2Cube, 7)
    print(f2l2Sol)
    for move in f2l2Sol:
        originalCube.move(move)
    originalCube.printCube()

    f2l3Cube = Cube(front=["x","x","x","g","g","g","g","g","g"],
                     left=["o","o","x","o","o","x","o","o","x"],
                     right=["x","x","x","x","r","r","x","r","r"],
                     back=["b","b","x","b","b","x","x","x","x"],
                     top=["x","x","x","x","x","x","x","x","x"],
                     bottom=["y","y","y","y","y","y","y","y","x"],)
    f2l3Sol = getSolution(copy.deepcopy(originalCube), f2l3Cube, 7)
    corner3Sol = []
    if not f2l3Sol:
        corner3Cube = Cube(front=["x","x","x","g","g","g","g","g","g"],
                         left=["o","x","x","o","o","x","o","o","x"],
                         right=["x","x","x","x","r","r","x","r","r"],
                         back=["b","b","x","x","b","x","x","x","x"],
                         top=["x","x","x","x","x","x","x","x","x"],
                         bottom=["y","y","y","y","y","y","y","y","x"],)
        corner3Sol = getSolution(copy.deepcopy(originalCube), corner3Cube, 7)
        print(corner3Sol)
        for move in corner3Sol:
            originalCube.move(move)
        f2l3Sol = getSolution(copy.deepcopy(originalCube), f2l3Cube, 7)
    print(f2l3Sol)
    for move in f2l3Sol:
        originalCube.move(move)
    originalCube.printCube()

    f2l4Cube = Cube(front=["x","x","x","g","g","g","g","g","g"],
                     left=["o","o","x","o","o","x","o","o","x"],
                     right=["x","r","r","x","r","r","x","r","r"],
                     back=["b","b","b","b","b","b","x","x","x"],
                     top=["x","x","x","x","x","x","x","x","x"],
                     bottom=["y","y","y","y","y","y","y","y","y"],)
    f2l4Sol = getSolution(copy.deepcopy(originalCube), f2l4Cube, 7)
    corner4Sol = []
    if not f2l4Sol:
        corner4Cube = Cube(front=["x","x","x","g","g","g","g","g","g"],
                     left=["o","o","x","o","o","x","o","o","x"],
                     right=["x","x","r","x","r","r","x","r","r"],
                     back=["b","b","b","b","b","x","x","x","x"],
                     top=["x","x","x","x","x","x","x","x","x"],
                     bottom=["y","y","y","y","y","y","y","y","y"],)
        corner4Sol = getSolution(copy.deepcopy(originalCube), corner4Cube, 7)
        print(corner4Sol)
        for move in corner4Sol:
            originalCube.move(move)
        f2l4Sol = getSolution(copy.deepcopy(originalCube), f2l4Cube, 7)
    print(f2l4Sol)
    for move in f2l4Sol:
        originalCube.move(move)
    originalCube.printCube()

    ollSol = oll(originalCube, "olls2.csv")
    if ollSol:
        print(ollSol)
        for move in ollSol:
            originalCube.move(move)
        originalCube.printCube()

    pllSol = pll(originalCube, "plls2.csv")
    if pllSol:
        print(pllSol)
        for move in pllSol:
            originalCube.move(move)
        originalCube.printCube()

    aufSol = getSolution(copy.deepcopy(originalCube), Cube(), 2)
    print(aufSol)
    if aufSol:
        for move in aufSol:
            originalCube.move(move)
        originalCube.printCube()

    sol = combineSolutions(crossSolution,corner1Sol,f2l1Sol,corner2Sol,f2l2Sol,corner3Sol,f2l3Sol,corner4Sol,f2l4Sol,ollSol,pllSol,aufSol)

    print(f"Solution ({len(sol)} moves): {sol}")

    end = time.perf_counter()
    print(f"Time: {end-start}")
