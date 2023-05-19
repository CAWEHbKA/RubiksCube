


faces_long = ["UP", "LEFT", "FRONT", "RIGHT", "BACK", "DOWN"]
colors_long = ["WHITE", "RED", "BLUE", "ORANGE", "GREEN", "YELLOW"]
class RubicsCubeInstance:
    def __init__(self):
        self.faces_names_long = ["UP", "LEFT", "FRONT", "RIGHT", "BACK", "DOWN"]
        self.colors_names_long = ["WHITE", "RED", "BLUE", "ORANGE", "GREEN", "YELLOW"]
        self.faces = {}
        #for a in zip(self.faces_names_long, self.colors_names_long):
        #    self.faces[a[0][0]] = []
        #    for i in range(9):
        #        self.faces[a[0][0]].append(a[1][0]+str(i))

        #self.faces['U'] = ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
        #self.faces['L'] = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
        #self.faces['F'] = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
        #self.faces['R'] = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        #self.faces['B'] = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']
        #self.faces['D'] = ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']

        self.faces['U'] = ['W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8']
        self.faces['L'] = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8']
        self.faces['F'] = ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8']
        self.faces['R'] = ['O0', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8']
        self.faces['B'] = ['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8']
        self.faces['D'] = ['Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8']

    def internal_rotate_face(self, face):
        keep = self.faces[face][0]
        self.faces[face][0] = self.faces[face][2]
        self.faces[face][2] = self.faces[face][8]
        self.faces[face][8] = self.faces[face][6]
        self.faces[face][6] = keep

        keep = self.faces[face][1]
        self.faces[face][1] = self.faces[face][5]
        self.faces[face][5] = self.faces[face][7]
        self.faces[face][7] = self.faces[face][3]
        self.faces[face][3] = keep

    def move_U(self):
        self.internal_rotate_face('U')
        keep = self.faces['F'][0:3:1]
        self.faces['F'][0:3:1] = self.faces['L'][0:3:1]
        self.faces['L'][0:3:1] = self.faces['B'][0:3:1]
        self.faces['B'][0:3:1] = self.faces['R'][0:3:1]
        self.faces['R'][0:3:1] = keep

    def move_F(self):
        self.internal_rotate_face('F')
        keep = self.faces['U'][6:9:1]
        self.faces['U'][6:9:1] = self.faces['R'][0:9:3]
        self.faces['R'][0:9:3] = self.faces['D'][2::-1]
        self.faces['D'][2::-1] = self.faces['L'][8::-3]
        self.faces['L'][8::-3] = keep

    def move_L(self):
        self.internal_rotate_face('L')
        keep = self.faces['U'][0:9:3]
        self.faces['U'][0:9:3] = self.faces['F'][0:9:3]
        self.faces['F'][0:9:3] = self.faces['D'][0:9:3]
        self.faces['D'][0:9:3] = self.faces['B'][8::-3]
        self.faces['B'][8::-3] = keep

    def move_R(self):
        self.internal_rotate_face('R')
        keep = self.faces['U'][2:9:3]
        self.faces['U'][2:9:3] = self.faces['B'][0:9:3]
        self.faces['B'][0:9:3] = self.faces['D'][8::-3]
        self.faces['D'][8::-3] = self.faces['F'][8::-3]
        self.faces['F'][8::-3] = keep

    def print_row_no_newline(self, face, row):
        for i in range(3):
            print(self.faces[face][3*row + i] + ' ', end='')
    def print_cube(self):
        print('-' * 36)
        for i in range(3):
            print(" " * 3 * (1 + len(self.faces['U'][0])), end='')
            self.print_row_no_newline('U',i)
            print()
        for i in range(3):
            self.print_row_no_newline('L',i)
            self.print_row_no_newline('F',i)
            self.print_row_no_newline('R',i)
            self.print_row_no_newline('B',i)
            print()
        for i in range(3):
            print(" " * 3 * (1 + len(self.faces['U'][0])), end='')
            self.print_row_no_newline('D',i)
            print()

cube = RubicsCubeInstance()
#cube.faces['U'][0] = 'GG'
cube.print_cube()
cube.move_R()
cube.print_cube()
cube.move_R()
cube.print_cube()
cube.move_R()
cube.print_cube()
cube.move_R()
cube.print_cube()
