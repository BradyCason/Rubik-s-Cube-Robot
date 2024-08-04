# Rubik's Cube Solver
This is the code for a Rubik's Cube Robot. I created a UI using [tkinter](), and I used the [twophase]() library to solve the cube in 21 moves or less in less than 0.5 seconds. Additionally, I set up the solver to output code that I copy into the arduino file. The Arduino file controls the motors in the robot, and solves the physical cube.

# solver.py
The `solver.py` file is the main brains of the program. It uses [tkinter]() to create a GUI to either manually input the cube or use `camera_input.py` to get input the cube. After that, it uses the [twophase]() library to find the solution to the cube and output two lines of Arduino code (C++) to paste into `RubiksSolver.ino`.

# camera_input.py
The `camera_input.py` file uses cv2 to use the computer's camera to input the cube. It takes 6 images (1 for each side of the cube) and converts the colors into a string that `solver.py` can use.

# RubiksSolver.ino
The `RubiksSolver.ino` file is an arduino file (C++) that is uploaded to the Arduino Uno in my Rubik's Cube Solving Robot. The Arduino controls 6 individual stepper motors that turn each face and solve the cube in under 3 seconds.

# How to use
In order to solver your Rubik's Cube, run `solver.py`. It will take about 30 minutes to run the first time, as the twhophase library needs to create tables on your local computer to assist with the solving algorithm. After the first run, the solving will be almost instantaneous.

After running `solver.py`, choose if you'd like to input your cube with your computer's camera or manually input the cube (using a GUI). After you input the cube, the solution will appear. If you have access to a robot, copy and paste the Arduino code that is outputed into `RubiksSolver.ino` and upload the code to your Arduino Uno.

# Robot Design Video
[put video link here]