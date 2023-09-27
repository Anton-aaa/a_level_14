class Color:
    WHITE = "white"
    BLACK = "BLACK"
class Figure:
    def __init__(self, col, vert_arr, hor_arr):
        self.color = col
        self.vertical_arrangement = vert_arr
        self.horizontal_arrangement = hor_arr
    color = Color.WHITE
    vertical_arrangement = 2
    horizontal_arrangement = 5

    def set_color_change(self):
        if (self.color == "white"):
            self.color = "black"
        elif (self.color == "black"):
            self.color = "white"
        return None

    def set_position(self, vertical, horizontal):
        if 0 < vertical < 9 and 0 < horizontal < 9:
            self.vertical_arrangement = vertical
            self.horizontal_arrangement = horizontal
        return None

    def check_coordinate (self, coordinate):
        if 0 < coordinate < 9:
            return True
        else:
            return False

class Pawn (Figure):
    def get_check_new_move_pawn(self, vertical, horizontal):
        if not self.check_coordinate(vertical) or not self.check_coordinate(horizontal):
            return False
        if self.color == "white" and vertical - self.vertical_arrangement == 1 and horizontal - self.horizontal_arrangement == 0:
            return True
        elif self.color == "black" and self.vertical_arrangement - vertical == 1 and horizontal - self.horizontal_arrangement == 0:
            return True
        else:
            return False

class Rook (Figure):
    def get_check_new_move_rook(self, vertical, horizontal):
        if not self.check_coordinate(vertical) or not self.check_coordinate(horizontal):
            return False
        if (vertical != self.vertical_arrangement and horizontal == self.horizontal_arrangement) or (horizontal != self.horizontal_arrangement and vertical == self.vertical_arrangement):
            return True
        else:
            return False

class Knight (Figure):
    def get_check_new_move_knight(self, vertical, horizontal):
        if not self.check_coordinate(vertical) or not self.check_coordinate(horizontal):
            return False
        if ((abs(vertical - self.vertical_arrangement) == 2) and (abs(horizontal - self.horizontal_arrangement) == 1)) or ((abs(horizontal - self.horizontal_arrangement) == 2) and (abs(vertical - self.vertical_arrangement) == 1)):
            return True
        else:
            return False

class Bishop (Figure):
    def get_check_new_move_bishop(self, vertical, horizontal):
        if not self.check_coordinate(vertical) or not self.check_coordinate(horizontal):
            return False
        if abs(vertical - self.vertical_arrangement) == abs(horizontal - self.horizontal_arrangement):
            return True
        else:
            return False

class Queen(Figure):
    def get_check_new_move_queen(self, vertical, horizontal):
        if not self.check_coordinate(vertical) or not self.check_coordinate(horizontal):
            return False
        if abs(vertical - self.vertical_arrangement) == abs(horizontal - self.horizontal_arrangement) or ((vertical != self.vertical_arrangement and horizontal == self.horizontal_arrangement) or (horizontal != self.horizontal_arrangement and vertical == self.vertical_arrangement)):
            return True
        else:
            return False

class King(Figure):
    def get_check_new_move_king(self, vertical, horizontal):
        if not self.check_coordinate(vertical) or not self.check_coordinate(horizontal):
            return False
        if abs(vertical - self.vertical_arrangement) == abs(horizontal - self.horizontal_arrangement) == 1 or ((abs(vertical - self.vertical_arrangement) == 1 and horizontal == self.horizontal_arrangement) or (abs(horizontal - self.horizontal_arrangement) == 1 and vertical == self.vertical_arrangement)):
            return True
        else:
            return False

first_figure = Figure("white",3,5)
first_figure.set_color_change()
first_figure.set_position(1, 8)
print(first_figure.color, first_figure.vertical_arrangement, first_figure.horizontal_arrangement)

pawn = Pawn("white", 3,2)
pawn.set_color_change()
print(pawn.get_check_new_move_pawn(2, 2))

rook = Rook("white", 3,2)
print(rook.get_check_new_move_rook(3,8))

knight = Knight("white", 3, 3)
print(knight.get_check_new_move_knight(2,1))

bishop = Bishop("white", 6, 2)
print(bishop.get_check_new_move_bishop(5, 1))

queen = Queen("white", 3, 5)
print(queen.get_check_new_move_queen(3,1))

king = King("white", 7, 3)
print(king.get_check_new_move_king(6, 4))