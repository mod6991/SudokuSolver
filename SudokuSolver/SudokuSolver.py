"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade

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

gb = []
for row_i in range(9):
    gb.append([])
    for col_i in range(9):
        gb[row_i].append(None)

def get_cell_str(row_i, col_i):
    if gb[row_i][col_i] is None:
        return ' '
    return str(gb[row_i][col_i])

def draw_gb():
    for row_i in range(9):
        for col_i in range(9):
            tx, ty = change_coords(CELLS_START_POSITIONS[col_i] + (CELL_SIZE // 2), CELLS_START_POSITIONS[row_i] + (CELL_SIZE // 2))
            arcade.draw_text(get_cell_str(row_i, col_i), tx, ty, arcade.color.BLACK, 20,
                             width=40, align='center', anchor_x='center', anchor_y='center')

def get_cell(pos):
    for i in range(1, 9):
        if pos < CELLS_START_POSITIONS[i]:
            return i - 1
    return 8

def change_coords(x, y):
    return (x, SCREEN_HEIGHT - y)

def draw_big_lines():
    for i in range(4):
        sx, sy = change_coords(BIG_LINES_POSITIONS[i], 0)
        ex, ey = change_coords(BIG_LINES_POSITIONS[i], SCREEN_HEIGHT)
        arcade.draw_line(sx, sy, ex, ey, arcade.color.BLACK, BIG_BORDER)
        sx, sy = change_coords(0, BIG_LINES_POSITIONS[i])
        ex, ey = change_coords(SCREEN_WIDTH, BIG_LINES_POSITIONS[i])
        arcade.draw_line(sx, sy, ex, ey, arcade.color.BLACK, BIG_BORDER)

def draw_small_lines():
    for i in range(6):
        sx, sy = change_coords(SMALL_LINES_POSITIONS[i], 0)
        ex, ey = change_coords(SMALL_LINES_POSITIONS[i], SCREEN_HEIGHT)
        arcade.draw_line(sx, sy, ex, ey, arcade.color.BLACK, SMALL_BORDER)
        sx, sy = change_coords(0, SMALL_LINES_POSITIONS[i])
        ex, ey = change_coords(SCREEN_WIDTH, SMALL_LINES_POSITIONS[i])
        arcade.draw_line(sx, sy, ex, ey, arcade.color.BLACK, SMALL_BORDER)

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.mouse_x = 0
        self.mouse_y = 0
        self.cell_row = 0
        self.cell_col = 0

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        draw_big_lines()
        draw_small_lines()
        draw_gb()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

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

        if val:
            gb[self.cell_row][self.cell_col] = val

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.mouse_x, self.mouse_y = change_coords(x, y)
        self.cell_row = get_cell(self.mouse_y)
        self.cell_col = get_cell(self.mouse_x)
        
def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
