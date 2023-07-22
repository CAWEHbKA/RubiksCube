


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

    def check_neighbours(self):
        neighbors = []
        neighbors.append(sorted([self.faces['U'][1], self.faces['B'][1]]))
        neighbors.append(sorted([self.faces['U'][3], self.faces['L'][1]]))
        neighbors.append(sorted([self.faces['U'][5], self.faces['R'][1]]))
        neighbors.append(sorted([self.faces['U'][7], self.faces['F'][1]]))
        neighbors.append(sorted([self.faces['L'][3], self.faces['B'][5]]))
        neighbors.append(sorted([self.faces['F'][3], self.faces['L'][5]]))
        neighbors.append(sorted([self.faces['R'][3], self.faces['F'][5]]))
        neighbors.append(sorted([self.faces['B'][3], self.faces['R'][5]]))
        neighbors.append(sorted([self.faces['D'][1], self.faces['F'][7]]))
        neighbors.append(sorted([self.faces['D'][3], self.faces['L'][7]]))
        neighbors.append(sorted([self.faces['D'][5], self.faces['R'][7]]))
        neighbors.append(sorted([self.faces['D'][7], self.faces['B'][7]]))
        neighbors.append(sorted([self.faces['U'][0], self.faces['L'][0], self.faces['B'][2]]))
        neighbors.append(sorted([self.faces['U'][2], self.faces['R'][2], self.faces['B'][0]]))
        neighbors.append(sorted([self.faces['U'][6], self.faces['L'][2], self.faces['F'][0]]))
        neighbors.append(sorted([self.faces['U'][8], self.faces['F'][2], self.faces['R'][0]]))
        neighbors.append(sorted([self.faces['D'][0], self.faces['L'][8], self.faces['F'][6]]))
        neighbors.append(sorted([self.faces['D'][2], self.faces['F'][8], self.faces['R'][6]]))
        neighbors.append(sorted([self.faces['D'][6], self.faces['L'][6], self.faces['B'][8]]))
        neighbors.append(sorted([self.faces['D'][8], self.faces['R'][8], self.faces['B'][6]]))
        neighbors = sorted(neighbors)


        neighbors2 = []
        neighbors2.append(sorted(['W1', 'G1']))
        neighbors2.append(sorted(['W3', 'R1']))
        neighbors2.append(sorted(['W5', 'O1']))
        neighbors2.append(sorted(['W7', 'B1']))
        neighbors2.append(sorted(['R3', 'G5']))
        neighbors2.append(sorted(['B3', 'R5']))
        neighbors2.append(sorted(['O3', 'B5']))
        neighbors2.append(sorted(['G3', 'O5']))
        neighbors2.append(sorted(['Y1', 'B7']))
        neighbors2.append(sorted(['Y3', 'R7']))
        neighbors2.append(sorted(['Y5', 'O7']))
        neighbors2.append(sorted(['Y7', 'G7']))
        neighbors2.append(sorted(['W0', 'R0', 'G2']))
        neighbors2.append(sorted(['W2', 'O2', 'G0']))
        neighbors2.append(sorted(['W6', 'R2', 'B0']))
        neighbors2.append(sorted(['W8', 'B2', 'O0']))
        neighbors2.append(sorted(['Y0', 'R8', 'B6']))
        neighbors2.append(sorted(['Y2', 'B8', 'O6']))
        neighbors2.append(sorted(['Y6', 'R6', 'G8']))
        neighbors2.append(sorted(['Y8', 'O8', 'G6']))
        neighbors2 = sorted(neighbors2)

        print("check: ", neighbors==neighbors2)
        if neighbors != neighbors2:
            print(neighbors)
            print(neighbors2)
        return neighbors==neighbors2
    
    
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
        keep = self.faces['U'][8::-3]
        self.faces['U'][8::-3] = self.faces['B'][0:9:3]
        self.faces['B'][0:9:3] = self.faces['D'][8::-3]
        self.faces['D'][8::-3] = self.faces['F'][8::-3]
        self.faces['F'][8::-3] = keep

    def move_B(self):
        self.internal_rotate_face('B')
        keep = self.faces['U'][2::-1]
        self.faces['U'][2::-1] = self.faces['L'][0:9:3]
        self.faces['L'][0:9:3] = self.faces['D'][6:9:1]
        self.faces['D'][6:9:1] = self.faces['R'][8::-3]
        self.faces['R'][8::-3] = keep

    def move_D(self):
        self.internal_rotate_face('D')
        keep = self.faces['F'][6:9:1]
        self.faces['F'][6:9:1] = self.faces['R'][6:9:1]
        self.faces['R'][6:9:1] = self.faces['B'][6:9:1]
        self.faces['B'][6:9:1] = self.faces['L'][6:9:1]
        self.faces['L'][6:9:1] = keep
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

cube.check_neighbours()
cube.print_cube()
cube.move_D()
cube.check_neighbours()
cube.print_cube()
cube.move_D()
cube.check_neighbours()
cube.print_cube()
cube.move_D()
cube.check_neighbours()
cube.print_cube()
cube.move_D()
cube.check_neighbours()
cube.print_cube()
