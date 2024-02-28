from rubiks_cube_functions import Cube

Cube = Cube()

print("Play around with this cube using the following commands:\n -r\n -r'\n -r2\n -l\n -l'\n -l2\n -f\n -f'\n -f2\n -d\n -d'\n -d2\n -u\n -u'\n -u2\n -b\n -b'\n -b2\n -scramble\n -solve\n -input cube\n -end\n")

input("Press Enter to start\n")
Cube.printCube()

while True:
    move = input("Move: ")
    if move == "end":
        break
    else:
        Cube.move(move)
        Cube.printCube()
