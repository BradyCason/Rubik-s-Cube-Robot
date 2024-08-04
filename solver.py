import twophase.solver  as sv
import tkinter as tk
import re
from camera_input import Camera_Input
# UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB

class Solver:
    def __init__(self):
        self.cube = "WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB"
        self.ctr_color = "W"
        self.get_cube()

        # Solve Cube
        solution = sv.solve(self.cube_formatted(),19,2)

        # Send to Arduino code
        self.print_arduino_input(solution)

    def print_arduino_input(self, solution):
        move_string = r'String moves[] = {"'
        move_string += re.sub("\(.*\)", "", solution).strip().replace(" ", '", "')
        move_string += r'"};'

        num_moves = re.findall(r'[0-9]+f', solution)[-1][:-1]
        num_string = "int numMoves = " + num_moves + ";"

        print("\nCopy the following into the Arduino Code =================================\n")
        print(move_string)
        print(num_string)
        print("\n==========================================================================")

        root = tk.Tk()
        root.title("Rubik's Cube Solver - Solution")

        # Set the size of the window
        root.geometry("500x250")

        label = tk.Label(root, text=f"Copy the following into the Arduino Code\n==================================================")
        label.pack(pady=20)

        text_widget = tk.Text(root, height=5, width=50)
        text_widget.pack(pady=0)
        
        # Insert text into the Text widget
        text_widget.insert(tk.END, f"{move_string}\n{num_string}")
        
        # Make the Text widget read-only
        text_widget.config(state=tk.DISABLED)

        label = tk.Label(root, text=f"==================================================")
        label.pack(pady=20)

        # Run the main event loop
        root.mainloop()

    def cube_formatted(self):
        return self.cube.replace("Y","D").replace("G","F").replace("O","L").replace("W","U")

    def change_ctr_color(self, button_obj):
        if self.ctr_color == "W":
            button_obj.config(bg="red")
            self.ctr_color = "R"
        elif self.ctr_color == "R":
            button_obj.config(bg="orange")
            self.ctr_color = "O"
        elif self.ctr_color == "O":
            button_obj.config(bg="yellow")
            self.ctr_color = "Y"
        elif self.ctr_color == "Y":
            button_obj.config(bg="green")
            self.ctr_color = "G"
        elif self.ctr_color == "G":
            button_obj.config(bg="blue")
            self.ctr_color = "B"
        elif self.ctr_color == "B":
            button_obj.config(bg="white")
            self.ctr_color = "W"

    def change_color(self, button_obj, index):
        colors = {"W":"white","R":"red","O":"orange","Y":"yellow","G":"green","B":"blue"}
        button_obj.config(bg=colors[self.ctr_color])
        self.cube = self.cube[:index] + self.ctr_color + self.cube[index + 1:]

    def manual_input(self):
        window = tk.Tk()

        ctr_button = tk.Button(bg="white",width=5, height=2,padx=0,pady=0,command=lambda: self.change_ctr_color(ctr_button))
        ctr_button.grid(row = 0, column = 0)
        submit_button = tk.Button(text="Submit", bg="white",command=window.destroy)
        submit_button.grid(row = 9, column = 11, columnspan = 2)

        button1y = tk.Button(bg="yellow",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button1y, 27))
        button2y = tk.Button(bg="yellow",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button2y, 28))
        button3y = tk.Button(bg="yellow",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button3y, 29))
        button4y = tk.Button(bg="yellow",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button4y, 30))
        button5y = tk.Button(bg="yellow",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button5y, 31))
        button6y = tk.Button(bg="yellow",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button6y, 32))
        button7y = tk.Button(bg="yellow",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button7y, 33))
        button8y = tk.Button(bg="yellow",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button8y, 34))
        button9y = tk.Button(bg="yellow",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button9y, 35))

        button1r = tk.Button(bg="red",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button1r, 9))
        button2r = tk.Button(bg="red",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button2r, 10))
        button3r = tk.Button(bg="red",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button3r, 11))
        button4r = tk.Button(bg="red",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button4r, 12))
        button5r = tk.Button(bg="red",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button5r, 13))
        button6r = tk.Button(bg="red",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button6r, 14))
        button7r = tk.Button(bg="red",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button7r, 15))
        button8r = tk.Button(bg="red",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button8r, 16))
        button9r = tk.Button(bg="red",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button9r, 17))

        button1g = tk.Button(bg="green",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button1g, 18))
        button2g = tk.Button(bg="green",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button2g, 19))
        button3g = tk.Button(bg="green",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button3g, 20))
        button4g = tk.Button(bg="green",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button4g, 21))
        button5g = tk.Button(bg="green",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button5g, 22))
        button6g = tk.Button(bg="green",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button6g, 23))
        button7g = tk.Button(bg="green",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button7g, 24))
        button8g = tk.Button(bg="green",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button8g, 25))
        button9g = tk.Button(bg="green",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button9g, 26))

        button1w = tk.Button(bg="white",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button1w, 0))
        button2w = tk.Button(bg="white",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button2w, 1))
        button3w = tk.Button(bg="white",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button3w, 2))
        button4w = tk.Button(bg="white",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button4w, 3))
        button5w = tk.Button(bg="white",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button5w, 4))
        button6w = tk.Button(bg="white",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button6w, 5))
        button7w = tk.Button(bg="white",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button7w, 6))
        button8w = tk.Button(bg="white",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button8w, 7))
        button9w = tk.Button(bg="white",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button9w, 8))

        button1b = tk.Button(bg="blue",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button1b, 45))
        button2b = tk.Button(bg="blue",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button2b, 46))
        button3b = tk.Button(bg="blue",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button3b, 47))
        button4b = tk.Button(bg="blue",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button4b, 48))
        button5b = tk.Button(bg="blue",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button5b, 49))
        button6b = tk.Button(bg="blue",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button6b, 50))
        button7b = tk.Button(bg="blue",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button7b, 51))
        button8b = tk.Button(bg="blue",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button8b, 52))
        button9b = tk.Button(bg="blue",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button9b, 53))

        button1o = tk.Button(bg="orange",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button1o, 36))
        button2o = tk.Button(bg="orange",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button2o, 37))
        button3o = tk.Button(bg="orange",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button3o, 38))
        button4o = tk.Button(bg="orange",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button4o, 39))
        button5o = tk.Button(bg="orange",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button5o, 40))
        button6o = tk.Button(bg="orange",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button6o, 41))
        button7o = tk.Button(bg="orange",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button7o, 42))
        button8o = tk.Button(bg="orange",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button8o, 43))
        button9o = tk.Button(bg="orange",width=5, height=2,padx=0,pady=0,command=lambda: self.change_color(button9o, 44))
        
        button1y.grid(row = 7, column = 4)
        button2y.grid(row = 7, column = 5)
        button3y.grid(row = 7, column = 6)
        button4y.grid(row = 8, column = 4)
        button5y.grid(row = 8, column = 5)
        button6y.grid(row = 8, column = 6)
        button7y.grid(row = 9, column = 4)
        button8y.grid(row = 9, column = 5)
        button9y.grid(row = 9, column = 6)

        button1r.grid(row = 4, column = 7)
        button2r.grid(row = 4, column = 8)
        button3r.grid(row = 4, column = 9)
        button4r.grid(row = 5, column = 7)
        button5r.grid(row = 5, column = 8)
        button6r.grid(row = 5, column = 9)
        button7r.grid(row = 6, column = 7)
        button8r.grid(row = 6, column = 8)
        button9r.grid(row = 6, column = 9)

        button1g.grid(row = 4, column = 4)
        button2g.grid(row = 4, column = 5)
        button3g.grid(row = 4, column = 6)
        button4g.grid(row = 5, column = 4)
        button5g.grid(row = 5, column = 5)
        button6g.grid(row = 5, column = 6)
        button7g.grid(row = 6, column = 4)
        button8g.grid(row = 6, column = 5)
        button9g.grid(row = 6, column = 6)

        button1o.grid(row = 4, column = 0)
        button2o.grid(row = 4, column = 1)
        button3o.grid(row = 4, column = 2)
        button4o.grid(row = 5, column = 0)
        button5o.grid(row = 5, column = 1)
        button6o.grid(row = 5, column = 2)
        button7o.grid(row = 6, column = 0)
        button8o.grid(row = 6, column = 1)
        button9o.grid(row = 6, column = 2)

        button1b.grid(row = 4, column = 10)
        button2b.grid(row = 4, column = 11)
        button3b.grid(row = 4, column = 12)
        button4b.grid(row = 5, column = 10)
        button5b.grid(row = 5, column = 11)
        button6b.grid(row = 5, column = 12)
        button7b.grid(row = 6, column = 10)
        button8b.grid(row = 6, column = 11)
        button9b.grid(row = 6, column = 12)

        button1w.grid(row = 0, column = 4)
        button2w.grid(row = 0, column = 5)
        button3w.grid(row = 0, column = 6)
        button4w.grid(row = 1, column = 4)
        button5w.grid(row = 1, column = 5)
        button6w.grid(row = 1, column = 6)
        button7w.grid(row = 2, column = 4)
        button8w.grid(row = 2, column = 5)
        button9w.grid(row = 2, column = 6)

        window.mainloop()

    def camera_input(self):
        ci = Camera_Input()
        self.cube = ci.cube

    def get_cube(self):
        # Create the main window
        global root
        root = tk.Tk()
        root.title("Rubik's Cube Solver")

        # Set the size of the window
        root.geometry("300x200")

        label = tk.Label(root, text="Please choose a method to input the cube:")
        label.pack(pady=20)

        # Create and place the first button
        button1 = tk.Button(root, text="Camera Input", command=self.camera_input_clicked)
        button1.pack(pady=10)

        # Create and place the second button
        button2 = tk.Button(root, text="Manual Input", command=self.manual_input_clicked)
        button2.pack(pady=10)

        # Run the main event loop
        root.mainloop()

    def camera_input_clicked(self):
        root.destroy()
        self.camera_input = Camera_Input()

    def manual_input_clicked(self):
        root.destroy()
        self.manual_input()

if __name__ == "__main__":
    solver = Solver()