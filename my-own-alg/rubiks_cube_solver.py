from rubiks_cube_functions import Cube

Cube = Cube()

def get_start_and_end_cubes(Cube):
    print("Starting point:")
    #Cube.inputCube()
    Cube.startFrontColors = Cube.frontColors.copy()
    Cube.startLeftColors = Cube.leftColors.copy()
    Cube.startRightColors = Cube.rightColors.copy()
    Cube.startBackColors = Cube.backColors.copy()
    Cube.startTopColors = Cube.topColors.copy()
    Cube.startBottomColors = Cube.bottomColors.copy()
    
    print("Desired end point:")
    #Cube.inputCube()
    Cube.endFrontColors = Cube.frontColors.copy()
    Cube.endLeftColors = Cube.leftColors.copy()
    Cube.endRightColors = Cube.rightColors.copy()
    Cube.endBackColors = Cube.backColors.copy()
    Cube.endTopColors = Cube.topColors.copy()
    Cube.endBottomColors = Cube.bottomColors.copy()

def get_max_number_of_turns(Cube):
    while True:
        try:
            Cube.maxNumMoves = int(input("\nMost moves you would like: "))
            break
        except:
            print("Invalid number of moves")

def get_turns_to_use(Cube):
    print('\nWhat moves would you like to allow? (Type "done" when all are selected)')
    line = "Possible moves are:"
    Cube.keys_turns = list(Cube.turns)
    for turn in Cube.keys_turns:
        line += " " + turn + ","
    print(line)
    
    Cube.usedTurns = [" "]
    while True:
        move = input("Move: ")
        valid = False
        for turn in Cube.keys_turns:
            if turn == move:
                valid = True
        for usedTurn in Cube.usedTurns:
            if usedTurn == move:
                valid = False
        if valid:
            Cube.usedTurns.append(move)
        elif move == "done":
            break
        else:
            print("Invalid Move")

def reset_cube(Cube):
    Cube.frontColors = Cube.startFrontColors.copy()
    Cube.leftColors = Cube.startLeftColors.copy()
    Cube.rightColors = Cube.startRightColors.copy()
    Cube.backColors = Cube.startBackColors.copy()
    Cube.topColors = Cube.startTopColors.copy()
    Cube.bottomColors = Cube.startBottomColors.copy()

def cube_equals_end(Cube):
    if Cube.frontColors == Cube.endFrontColors and Cube.backColors == Cube.endBackColors and Cube.topColors == Cube.endTopColors and Cube.bottomColors == Cube.endBottomColors and Cube.leftColors == Cube.endLeftColors and Cube.rightColors == Cube.endRightColors:
        return(True)
    else:
        return(False)

def create_all_sequences(Cube):
    
    for turnA in Cube.usedTurns:
        reset_cube(Cube)
        
        Cube.turnA()
        
        if cube_equals_end(Cube):
            Cube.solutions.append([turnA])
            
        if 1 < Cube.maxNumMoves:
            for turnb in Cube.usedTurns:
                Cube.turnB()
               
                if cube_equals_end(Cube):
                   Cube.solutions.append([turnA,turnB])
                
                if 2 < Cube.maxNumMoves:
                    for turnC in Cube.usedTurns:
                        Cube.turnC()
                        
                        if cube_equals_end(Cube):
                            Cube.solutions.append([turnA,turnB,turnC])
                            
                        if 3 < Cube.maxNumMoves:
                            for turnD in Cube.usedTurns:
                                Cube.turnD()
                                    
                                if cube_equals_end(Cube):
                                    Cube.solutions.append([turnA,turnB,turnC,turnD])
                                        
                                if 4 < Cube.maxNumMoves:
                                    pass

get_start_and_end_cubes(Cube)

get_max_number_of_turns(Cube)

get_turns_to_use(Cube)

print("\nSimulating\n")

Cube.solutions = []

Cube.numMoves = 1
create_all_sequences(Cube)
    
print(Cube.solutions)
