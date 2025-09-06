Board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
  #--------------------
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    #--------------------
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

Boxes = [
    [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]],
    [[0,3],[0,4],[0,5],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5]],
    [[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]],
    [[3,0],[3,1],[3,2],[4,0],[4,1],[4,2],[5,0],[5,1],[5,2]],
    [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]],
    [[3,6],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]],
    [[6,0],[6,1],[6,2],[7,0],[7,1],[7,2],[8,0],[8,1],[8,2]],
    [[6,3],[6,4],[6,5],[7,3],[7,4],[7,5],[8,3],[8,4],[8,5]],
    [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]
]

class Solver:
    def __init__(self, Board, Boxes):
        self.board = Board
        self.boxes = Boxes
        self.attempts = 0



    def print_board(self):
        print(f"""{self.board[0][0]} {self.board[0][1]} {self.board[0][2]} || {self.board[0][3]} {self.board[0][4]} {self.board[0][5]} || {self.board[0][6]} {self.board[0][7]} {self.board[0][8]}
{self.board[1][0]} {self.board[1][1]} {self.board[1][2]} || {self.board[1][3]} {self.board[1][4]} {self.board[1][5]} || {self.board[1][6]} {self.board[1][7]} {self.board[1][8]}
{self.board[2][0]} {self.board[2][1]} {self.board[2][2]} || {self.board[2][3]} {self.board[2][4]} {self.board[2][5]} || {self.board[2][6]} {self.board[2][7]} {self.board[2][8]}
========================
{self.board[3][0]} {self.board[3][1]} {self.board[3][2]} || {self.board[3][3]} {self.board[3][4]} {self.board[3][5]} || {self.board[3][6]} {self.board[3][7]} {self.board[3][8]}
{self.board[4][0]} {self.board[4][1]} {self.board[4][2]} || {self.board[4][3]} {self.board[4][4]} {self.board[4][5]} || {self.board[4][6]} {self.board[4][7]} {self.board[4][8]}
{self.board[5][0]} {self.board[5][1]} {self.board[5][2]} || {self.board[5][3]} {self.board[5][4]} {self.board[5][5]} || {self.board[5][6]} {self.board[5][7]} {self.board[5][8]}
========================
{self.board[6][0]} {self.board[6][1]} {self.board[6][2]} || {self.board[6][3]} {self.board[6][4]} {self.board[6][5]} || {self.board[6][6]} {self.board[6][7]} {self.board[6][8]}
{self.board[7][0]} {self.board[7][1]} {self.board[7][2]} || {self.board[7][3]} {self.board[7][4]} {self.board[7][5]} || {self.board[7][6]} {self.board[7][7]} {self.board[7][8]}
{self.board[8][0]} {self.board[8][1]} {self.board[8][2]} || {self.board[8][3]} {self.board[8][4]} {self.board[8][5]} || {self.board[8][6]} {self.board[8][7]} {self.board[8][8]}
""")


    def is_valid(self, number, pos):
        check1 = True
        check2 = True
        check3 = True

        #checks for number in the row
        for row in range(0, 9):

            if self.board[pos[0]][row] == number and row != pos[1]:

                check1 = False


        #checks for number in the column
        for column in range(0, 9):
            if self.board[column][pos[1]] == number and column != pos[1]:

                check2 = False
                break

        #Check which box it is in
        for box in self.boxes:
            for x in box:
                if x == pos:
                    currentBox = box
                    break

        #Checks through the values of each position in said box
        for x in currentBox:
            if number == self.board[x[0]][x[1]] and x != pos:

                check3 = False
                break


        return [check1, check2, check3]

    #attempts a number, and changes if successfull
    def trying(self, number, pos):
        attempt = self.is_valid(number, pos)
        self.attempts += 1
        if attempt[0] and attempt[1] and attempt[2]:
            return True

        else: return False


    def solving(self, pointer):
        if pointer[1] == 9:
            pointer[1] = 0
            pointer[0] += 1


        while self.board[pointer[0]][pointer[1]] != 0:
            pointer[1] += 1

            if pointer[1] == 9:
                pointer[1] = 0
                pointer[0] += 1
            if pointer[0] == 9: quit()




        else:
            for i in range(1, 10):
                if self.trying(i, pointer):
                    print(f"{i} has worked at {pointer}")
                    temp = self.board[pointer[0]][pointer[1]]
                    self.board[pointer[0]][pointer[1]] = i
                    self.print_board()
                    if pointer == [8,8]:
                        print(f"DONE\nAttempts taken for success = {self.attempts}")
                        quit()


                    if not (self.solving([pointer[0], pointer[1] + 1])):
                        self.board[pointer[0]][pointer[1]] = temp

                print(f"{i} not worked at {pointer}")

            return False



    def run(self):

        if self.solving([0,0]):
            self.print_board()









solver = Solver(Board, Boxes)
solver.print_board()
solver.run()
#solver.trying(2, [0,0])
