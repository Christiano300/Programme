import time


class Cube:
    def __init__(self):
        self.faces = []
        self.rotations = []
        self.colors = ["W", "Y", "G", "B", "R", "O"]
        self.faces_to_move_outer = []
        self.faces_to_move_inner = []
        self.temp = []
        for i in self.colors:
            for j in range(9):
                self.faces.append(i)
        for i in range(6):
            self.rotations.append(0)

    def turn(self, move):
        
        if move.startswith("U"):
            if move == "U":
                self.faces_to_move_outer = {20: 47, 47: 29, 29: 38, 38: 20, 19: 46, 46: 28, 28: 37, 37: 19, 18: 45, 45: 27, 27: 36, 36: 18}
                self.faces_to_move_inner = {0: 2, 2: 8, 8: 6, 6: 0, 1: 5, 5: 7, 7: 3, 3: 1}
            
            elif move == "U'":
                self.faces_to_move_outer = {47: 20, 29: 47, 38: 29, 20: 38, 46: 19, 28: 46, 37: 28, 19: 37, 45: 18, 27: 45, 36: 27, 18: 36}
                self.faces_to_move_inner = {2: 0, 8: 2, 6: 8, 0: 6, 5: 1, 7: 5, 3: 7, 1: 3}
            
            elif move == "U2":
                self.faces_to_move_outer = {20: 29, 29: 20, 19: 28, 28: 19, 18: 27, 27: 18, 36: 45, 45: 36, 37: 46, 46: 37, 38: 47, 47: 38}
                self.faces_to_move_inner = {0: 8, 8: 0, 1: 7, 7: 1, 2: 6, 6: 2, 5: 3, 3: 5}
        
        elif move.startswith("D"):
            if move == "D":
                self.faces_to_move_outer = {24: 42, 42: 33, 33: 51, 51: 24, 25: 43, 43: 34, 34: 52, 52: 25, 26: 44, 44: 35, 35: 53, 53: 26}
                self.faces_to_move_inner = {9: 11, 11: 17, 17: 15, 15: 9, 10: 14, 14: 16, 16: 12, 12: 10}
            
            elif move == "D'":
                self.faces_to_move_outer = {42: 24, 33: 42, 51: 33, 24: 51, 43: 25, 34: 43, 52: 34, 25: 52, 44: 26, 35: 44, 53: 35, 26: 53}
                self.faces_to_move_inner = {11: 9, 17: 11, 15: 17, 9: 15, 14: 10, 16: 14, 12: 16, 10: 12}
            
            elif move == "D2":
                self.faces_to_move_outer = {24: 33, 33: 24, 25: 34, 34: 25, 26: 35, 35: 26, 42: 51, 51: 42, 43: 52, 52: 43, 44: 53, 53: 44}
                self.faces_to_move_inner = {9: 17, 17: 9, 10: 16, 16: 10, 11: 15, 15: 11, 14: 12, 12: 14}

        elif move.startswith('F'):
            if move == 'F':
                self.faces_to_move_outer = {6: 36, 36: 11, 11: 53, 53: 6, 7: 10, 10: 39, 39: 50, 50: 7, 8: 42, 42: 9, 9: 47, 47: 8}
                self.faces_to_move_inner = {18: 20, 20: 26, 26: 24, 24: 18, 19: 23, 23: 25, 25: 21, 21: 19}
            
            elif move == "F'":
                self.faces_to_move_outer = {36: 6, 11: 36, 53: 11, 6: 53, 10: 7, 39: 10, 50: 39, 7: 50, 42: 8, 9: 42, 47: 9, 8: 47}
                self.faces_to_move_inner = {20: 18, 26: 20, 24: 26, 18: 24, 23: 19, 25: 23, 21: 25, 19: 21}
                
            elif move == "F2":
                self.faces_to_move_outer = {18: 26, 26: 18, 19: 25, 25: 19, 20: 24, 24: 20, 23: 21, 21: 23}
                self.faces_to_move_inner = {6: 11, 11: 6, 7: 10, 10: 7, 8: 9, 9: 8, 47: 42, 42: 47, 50: 39, 39: 50, 53: 36, 36: 53}
        
        elif move.startswith("B"):
            if move == "B":
                self.faces_to_move_outer = {}
                self.faces_to_move_inner = {27:  29, 29: 35, 53: 33, 33: 27, 28: 32, 32: 34, 34: 30}
        self.temp = self.faces[:]
        for i in self.faces_to_move_inner:
            self.faces[self.faces_to_move_inner[i]] = self.temp[i]
        
        self.temp = self.faces[:]
        for i in self.faces_to_move_outer:
            self.faces[self.faces_to_move_outer[i]] = self.temp[i]

    def print_faces(self):
        self.temp = []
        for i in range(len(self.faces)):
            self.temp.append(self.faces[i])
            if (i + 1) % 9 == 0:
                print(self.temp)
                self.temp = []
        for i in range(len(self.rotations)):
            self.rotations[i] = self.rotations[i] % 4
        print(self.rotations)
        print("\n")

    def move(self,moves,print=False):
        if print:
            self.print_faces()
        for i in moves:
            self.turn(i)
            if print:
                self.print_faces()
            


Wurfel = Cube()
time_a = time.time()
Wurfel.print_faces()
Wurfel.move(["U'"])
time_b = time.time()

Wurfel.print_faces()
"""
print("Done. Took " + str((time_b - time_a)*1000) + " milliseconds. Thats " + str(((time_b - time_a)/20)*1000) + " milliseconds per turn.\n")
"""