"""
Sudoku solver
Josué Clément (2021)
"""
import arcade
from sudokulib import Sudoku

BIG_BORDER = 4
SMALL_BORDER = 2
CELL_SIZE = 50
ROWS, COLS = 9, 9

SCREEN_WIDTH = (4 * BIG_BORDER) + (6 * SMALL_BORDER) + (9 * CELL_SIZE)
SCREEN_HEIGHT = (4 * BIG_BORDER) + (6 * SMALL_BORDER) + (9 * CELL_SIZE)
SCREEN_TITLE = "Sudoku solver"

BIG_LINES_POSITIONS = \
[
    BIG_BORDER // 2,
    (1 * BIG_BORDER) + (2 * SMALL_BORDER) + (3 * CELL_SIZE) + (BIG_BORDER // 2),
    (2 * BIG_BORDER) + (4 * SMALL_BORDER) + (6 * CELL_SIZE) + (BIG_BORDER // 2),
    (3 * BIG_BORDER) + (6 * SMALL_BORDER) + (9 * CELL_SIZE) + (BIG_BORDER // 2)
]

SMALL_LINES_POSITIONS = \
[
    (1 * BIG_BORDER) + (1 * CELL_SIZE) + (SMALL_BORDER // 2),
    (1 * BIG_BORDER) + (1 * SMALL_BORDER) + (2 * CELL_SIZE) + (SMALL_BORDER // 2),
    (2 * BIG_BORDER) + (2 * SMALL_BORDER) + (4 * CELL_SIZE) + (SMALL_BORDER // 2),
    (2 * BIG_BORDER) + (3 * SMALL_BORDER) + (5 * CELL_SIZE) + (SMALL_BORDER // 2),
    (3 * BIG_BORDER) + (4 * SMALL_BORDER) + (7 * CELL_SIZE) + (SMALL_BORDER // 2),
    (3 * BIG_BORDER) + (5 * SMALL_BORDER) + (8 * CELL_SIZE) + (SMALL_BORDER // 2)
]

CELLS_START_POSITIONS = \
[
    (1 * BIG_BORDER),
    (1 * BIG_BORDER) + (1 * SMALL_BORDER) + (1 * CELL_SIZE),
    (1 * BIG_BORDER) + (2 * SMALL_BORDER) + (2 * CELL_SIZE),
    (2 * BIG_BORDER) + (2 * SMALL_BORDER) + (3 * CELL_SIZE),
    (2 * BIG_BORDER) + (3 * SMALL_BORDER) + (4 * CELL_SIZE),
    (2 * BIG_BORDER) + (4 * SMALL_BORDER) + (5 * CELL_SIZE),
    (3 * BIG_BORDER) + (4 * SMALL_BORDER) + (6 * CELL_SIZE),
    (3 * BIG_BORDER) + (5 * SMALL_BORDER) + (7 * CELL_SIZE),
    (3 * BIG_BORDER) + (6 * SMALL_BORDER) + (8 * CELL_SIZE)
]

def change_coords(x, y):
    """
    Change the coords to move the origin point
    from bottom-left to top-left
    """
    return (x, SCREEN_HEIGHT - y)

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.sudo = None
        self.mouse_x = 0
        self.mouse_y = 0
        self.cell_row = 0
        self.cell_col = 0

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.sudo = Sudoku()
        self.mouse_x = 0
        self.mouse_y = 0
        self.cell_row = 0
        self.cell_col = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self.draw_gameboard()
        
    #def on_update(self, delta_time):
    #    """
    #    All the logic to move, and the game logic goes here.
    #    Normally, you'll call update() on the sprite lists that
    #    need it.
    #    """
    #    pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        """
        val = 0
        if key in (arcade.key.KEY_1, arcade.key.NUM_1):
            val = 1
        elif key in (arcade.key.KEY_2, arcade.key.NUM_2):
            val = 2
        elif key in (arcade.key.KEY_3, arcade.key.NUM_3):
            val = 3
        elif key in (arcade.key.KEY_4, arcade.key.NUM_4):
            val = 4
        elif key in (arcade.key.KEY_5, arcade.key.NUM_5):
            val = 5
        elif key in (arcade.key.KEY_6, arcade.key.NUM_6):
            val = 6
        elif key in (arcade.key.KEY_7, arcade.key.NUM_7):
            val = 7
        elif key in (arcade.key.KEY_8, arcade.key.NUM_8):
            val = 8
        elif key in (arcade.key.KEY_9, arcade.key.NUM_9):
            val = 9
        elif key in (arcade.key.X, arcade.key.DELETE):
            self.sudo.gb[self.cell_row][self.cell_col] = None
        elif key in (arcade.key.SPACE, arcade.key.ENTER):
            self.try_to_solve()

        if val:
            self.sudo.gb[self.cell_row][self.cell_col] = val

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.mouse_x, self.mouse_y = change_coords(x, y)
        self.cell_row = self.get_cell(self.mouse_y)
        self.cell_col = self.get_cell(self.mouse_x)

    def _draw_big_lines(self):
        for i in range(4):
            sx, sy = change_coords(BIG_LINES_POSITIONS[i], 0)
            ex, ey = change_coords(BIG_LINES_POSITIONS[i], SCREEN_HEIGHT)
            arcade.draw_line(sx, sy, ex, ey, arcade.color.BLACK, BIG_BORDER)
            sx, sy = change_coords(0, BIG_LINES_POSITIONS[i])
            ex, ey = change_coords(SCREEN_WIDTH, BIG_LINES_POSITIONS[i])
            arcade.draw_line(sx, sy, ex, ey, arcade.color.BLACK, BIG_BORDER)

    def _draw_small_lines(self):
        for i in range(6):
            sx, sy = change_coords(SMALL_LINES_POSITIONS[i], 0)
            ex, ey = change_coords(SMALL_LINES_POSITIONS[i], SCREEN_HEIGHT)
            arcade.draw_line(sx, sy, ex, ey, arcade.color.BLACK, SMALL_BORDER)
            sx, sy = change_coords(0, SMALL_LINES_POSITIONS[i])
            ex, ey = change_coords(SCREEN_WIDTH, SMALL_LINES_POSITIONS[i])
            arcade.draw_line(sx, sy, ex, ey, arcade.color.BLACK, SMALL_BORDER)

    def draw_gameboard(self):
        """
        Draw the game board
        """
        self._draw_big_lines()
        self._draw_small_lines()

        for row_i in range(9):
            for col_i in range(9):
                tx, ty = change_coords(CELLS_START_POSITIONS[col_i] + (CELL_SIZE // 2), 
                                       CELLS_START_POSITIONS[row_i] + (CELL_SIZE // 2))
                arcade.draw_text(self.get_cell_str(row_i, col_i), tx, ty, arcade.color.BLACK, 32,
                                 width=40, align='center', anchor_x='center', anchor_y='center')

    def get_cell_str(self, row_i, col_i):
        """
        Get the cell number, or space if empty
        """
        if self.sudo.gb[row_i][col_i] is None:
            return ' '
        return str(self.sudo.gb[row_i][col_i])

    def get_cell(self, pos):
        """
        Get the current cell from mouse position
        """
        for i in range(1, 9):
            if pos < CELLS_START_POSITIONS[i]:
                return i - 1
        return 8

    def try_to_solve(self):
        pass_i = 1
        while(True):
            print(f"-------------- round {pass_i} -------------")
            self.sudo.build_possibilities()
            nb_winners = self.sudo.search_for_winners()
            if nb_winners == 0:
                break
            pass_i += 1

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
