#!/usr/bin/env python
from tkinter import ttk
from tkinter import *
from random import randint


class CustomDefaultWindow:

    def __init__(self, parent):
        root.withdraw()
        top = self.top = Toplevel(parent)
        top.wm_attributes("-topmost", 1)
        top.minsize(width=780, height=521)
        top.maxsize(width=780, height=521)
        self.top.grid_columnconfigure(0, weight=1)
        self.top.grid_rowconfigure(0, weight=1)
        background_image = PhotoImage(file="Battleship_title.gif")
        background_label = Label(top, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.OneButton = Button(top, height=3, width=13, text='One Player', command=self.one).place(x=210, y=400)
        self.TwoButton = Button(top, height=3, width=13, text='Two Player', command=self.two).place(x=520, y=400)
        self.board_size = StringVar()
        self.turns = StringVar()
        self.icon_size = IntVar()
        self.ship_size = []
        self.sets = []
        self.game_mode = IntVar()


    def one(self):
        self.game_mode = 1
        self.DefaultButton = Button(self.top, height=3, width=13, text='Default Settings', command=self.defaults).place(x=210, y=400)
        self.CustomButton = Button(self.top, height=3, width=13, text='Custom Settings', command=self.custom).place(x=520, y=400)

    def two(self):
        self.game_mode = 2
        self.DefaultButton = Button(self.top, height=3, width=13, text='Default Settings', command=self.defaults).place(x=210, y=400)
        self.CustomButton = Button(self.top, height=3, width=13, text='Custom Settings', command=self.custom).place(x=520, y=400)

    def custom(self):
        self.custom_bool = True
        self.sets = [1, 1, [1, 1], 1, self.game_mode]
        self.top.destroy()

    def defaults(self):
        self.custom_bool = False
        self.board_size = 10
        self.turns = 0
        self.icon_size = 1
        self.ship_size = [5, 4, 3, 3, 2]
        self.sets = [int(self.board_size), int(self.turns), self.ship_size, self.icon_size, self.game_mode]
        self.top.destroy()
        root.deiconify()


class TwoPlayerBoatInput:
    def __init__(self, parent):
        root.withdraw()
        user_boat_input_class = self.top = Toplevel(parent)
        user_boat_input_class.wm_attributes("-topmost", 1)
        upper_frame_twoplay = ttk.Frame(user_boat_input_class, padding="10 10 10 10")
        upper_frame_twoplay.pack(side=BOTTOM)
        upper_frame_twoplay.columnconfigure(0, weight=1)
        upper_frame_twoplay.rowconfigure(0, weight=1)
        main_frame_twoplay = ttk.Frame(user_boat_input_class, padding="10 10 10 10")
        main_frame_twoplay.pack()
        main_frame_twoplay.columnconfigure(0, weight=1)
        main_frame_twoplay.rowconfigure(0, weight=1)
        lower_frame_twoplay = ttk.Frame(user_boat_input_class, padding="10 10 10 10")
        lower_frame_twoplay.pack(side=BOTTOM)
        lower_frame_twoplay.columnconfigure(0, weight=1)
        lower_frame_twoplay.rowconfigure(0, weight=1)
        self.clear_ship_button = Button(lower_frame_twoplay, text="Clear Current Ship", command=self.clear_ship).pack(side=LEFT, padx=50)
        self.clear_all_button = Button(lower_frame_twoplay, text="Clear Ships", command=self.clear_all).pack(side=LEFT, padx=50)
        self.submit_button = Button(lower_frame_twoplay, text="Done", command=self.submit).pack(side=LEFT, padx=50)

        self.final_user_ships = [1, 2, 3, 4, 5]

        self.ocean_pic = PhotoImage(file='Ocean_small.gif')
        self.boat_pic = PhotoImage(file='Boat_mid_small.gif')
        self.boat_pic_left = PhotoImage(file='Boat_left_small.gif')
        self.boat_pic_right = PhotoImage(file='Boat_right_small.gif')
        board_size_func = 10
        self.btn_dict_func = {}
        c = 1
        r = 1

        self.i_func = 0
        self.cur_ship_dir = ""

        self.ships = [5, 4, 3, 3, 2]
        self.user_ship_positions = []
        self.new_all_user_ships = []
        self.final_user_ships = []
        self.user_list = []
        positions_func = []
        i = 0
        self.let_to_words = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
                        11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T'}
        while i < board_size_func:
            j = 0
            while j < board_size_func:
                button_value = self.let_to_words[i] + str(j + 1)
                positions_func.append(button_value)
                j += 1
            i += 1

        i = 0
        j = 0
        self.alpha_to_list_func = {}
        for pos in positions_func:
            self.alpha_to_list_func[pos] = [i, j]
            j += 1
            if j == board_size_func:
                j = 0
                i += 1

        for pos in positions_func:
            # pass each button's text to a function
            action = lambda x=pos: self.user_ship_pos_choice(x)
            # create the buttons and assign to pos:button-object dict pair
            self.btn_dict_func[pos] = Button(main_frame_twoplay, image=self.ocean_pic, command=action)
            self.btn_dict_func[pos].grid(row=r, column=c, pady=0, padx=0)
            c += 1
            if c == board_size_func + 1:
                c = 1
                r += 1

    def clear_all(self):
        for z in self.positions_func:
            self.btn_dict_func[z].configure(image=ocean_pic)
        # global user_list
        self.user_list = []
        # global ships
        self.ships = [5, 4, 3, 3, 2]
        # global user_ship_positions
        self.user_ship_positions = []
        print("Clear All")

    def clear_ship(self):
        # global self.user_list
        for i in self.user_list:
            for letter, number in self.alpha_to_list_func.items():
                if i == number:
                    self.btn_dict_func[letter].configure(image=ocean_pic)

        self.user_list = []
        print("Clear Ship")

    def submit(self):
        print("Submit")
        if not self.ships:
            self.final_user_ships = self.user_ship_positions
            print(self.final_user_ships)
        else:
            print("Invalid Ship Co-ordinates")
        """
        self.final_user_ships = [1, 2, 3, 4, 5]
        print("Submit")"""
        self.top.destroy()
        root.deiconify()

    def user_ship_pos_choice(self, y):
        if self.ships:
            # global self.user_ship_positions
            # global self.user_list
            but = self.alpha_to_list_func[y]
            len_user = len(self.user_list)

            ship_len = self.ships[0]
            add_pos = False
            att_dir = ""
            ship_dir = ""

            if not self.user_list:
                add_pos = True
                print("empty user list")
            elif len_user > 1:
                if self.user_list[0][0] == self.user_list[1][0]:
                    ship_dir = "h"
                elif self.user_list[0][1] == self.user_list[1][1]:
                    ship_dir = "v"
                if abs(but[0] - self.user_list[int(len_user - 1)][0]) == 1 and abs(
                                but[1] - self.user_list[int(len_user - 1)][1]) == 0:
                    att_dir = "v"
                elif abs(but[1] - self.user_list[int(len_user - 1)][1]) == 1 and abs(
                                but[0] - self.user_list[int(len_user - 1)][0]) == 0:
                    att_dir = "h"
                if att_dir == "h" and ship_dir == "h":
                    add_pos = True
                elif att_dir == "v" and ship_dir == "v":
                    add_pos = True
            elif len_user > 0:
                if abs(but[0] - self.user_list[int(len_user - 1)][0]) == 1 and abs(
                                but[1] - self.user_list[int(len_user - 1)][1]) == 0:
                    add_pos = True
                elif abs(but[1] - self.user_list[int(len_user - 1)][1]) == 1 and abs(
                                but[0] - self.user_list[int(len_user - 1)][0]) == 0:
                    add_pos = True

            for pos in self.user_list:
                if but == pos:
                    add_pos = False

            if add_pos:
                for counter_1 in range(len(self.user_ship_positions)):
                    for counter_2 in self.user_ship_positions[counter_1]:
                        if but == counter_2:
                            add_pos = False
                            print("Invalid Position: Overlapping Ships")

            if add_pos:
                self.user_list.append(but)
                self.btn_dict_func[y].configure(image=self.boat_pic)
                if ship_len == len(self.user_list):
                    del (self.ships[0])
                    self.user_ship_positions.append(self.user_list)
                    self.user_list = []
                    if not self.ships:
                        print("All ships complete")


class ShipsWindow:

    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.wm_attributes("-topmost", 1)
        self.Size_Label = Label(top, text='Enter Board Size:')
        self.Size_Label.pack()
        self.Ship_Entry = Entry(top)
        self.Ship_Entry.pack()
        self.myAddButton = Button(top, text='Another', command=self.add)
        self.myAddButton.pack()
        self.mySubmitButton = Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()
        self.ship = []

    def send(self):
        self.ship.append(int(self.Ship_Entry.get()))
        self.top.destroy()

    def add(self):
        self.ship.append(int(self.Ship_Entry.get()))
        self.Ship_Entry.delete(0, 'end')


class SettingsWindow:

    def __init__(self, parent):
        root.withdraw()
        top = self.top = Toplevel(parent)
        top.wm_attributes("-topmost", 1)
        self.Size_Label = Label(top, text='Enter Board Size:')
        self.Size_Label.pack()
        self.Size_Entry = Entry(top)
        self.Size_Entry.pack()
        self.Turns_Label = Label(top, text='Enter Number of Turns:')
        self.Turns_Label.pack()
        self.Turns_Entry = Entry(top)
        self.Turns_Entry.pack()
        self.Ships_Label = Label(top, text='Number of Ships:')
        self.Ships_Label.pack()
        self.Ships_Radio = IntVar()
        Radiobutton(top, text="Default", variable=self.Ships_Radio, value=0).pack()
        Radiobutton(top, text="Custom", variable=self.Ships_Radio, value=1).pack()
        self.Icon_Label = Label(top, text='Icon Size:')
        self.Icon_Label.pack()
        self.Icon_Radio = IntVar()
        Radiobutton(top, text="small", variable=self.Icon_Radio, value=1).pack()
        Radiobutton(top, text="large", variable=self.Icon_Radio, value=2).pack()
        self.mySubmitButton = Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()
        self.board_size = StringVar()
        self.turns = StringVar()
        self.ships = IntVar()
        self.icon_size = IntVar()
        self.ship_size = []

    def send(self):
        self.board_size = self.Size_Entry.get()
        self.turns = self.Turns_Entry.get()
        self.ships = self.Ships_Radio.get()
        self.icon_size = self.Icon_Radio.get()
        if self.ships == 1:
            ship_dialog = ShipsWindow(root)
            root.wait_window(ship_dialog.top)
            self.ship_size = ship_dialog.ship
        else:
            self.ship_size = [5, 4, 3, 3, 2]
        self.top.destroy()
        root.deiconify()


def on_open():
    main_page = CustomDefaultWindow(root)
    root.wait_window(main_page.top)
    user_settings = main_page.sets
    global user_ship_list
    if user_settings[4] == 2:
        user_boat_position_input = TwoPlayerBoatInput(root)
        root.wait_window(user_boat_position_input.top)
        user_ship_list = user_boat_position_input.final_user_ships
        print(user_ship_list)
        print("result from submit^")
    if main_page.custom_bool:
        settings = SettingsWindow(root)
        root.wait_window(settings.top)
        user_settings = [int(settings.board_size), int(settings.turns), settings.ship_size, settings.icon_size]

    return user_settings


def user_guess(pos):
    guess = alpha_to_list[pos]
    hit = 0
    hit_ship = 0
    guess_row = guess[0]
    guess_col = guess[1]
    if board_cpu_visual[guess_row][guess_col] == "X":
        hit_bool = True
        print("You hit my battleships!")
        for c in range(len(cpu_ship_list)):
            for d in range(len(cpu_ship_list[c])):
                ship = cpu_ship_list[c]
                current_ship_pos = ship[d]
                if guess == current_ship_pos:
                    hit = 1
                    hit_ship = c
                    break
        if hit == 1:
            cpu_ship_list[hit_ship].remove(guess)

    else:
        hit_bool = False
        if board_cpu[guess_row][guess_col] == "M" or board_cpu[guess_row][guess_col] == "H":
            print("You guessed that one already.")
        else:
            print("You missed my battleships!")
            board_cpu[guess_row][guess_col] = "M"

    if hit_bool:
        btn_dict[pos].configure(image=hit_pic)
    else:
        btn_dict[pos].configure(image=miss_pic)


def print_ship(ship):
    for l in ship:
        board_cpu_visual[l[0]][l[1]] = "X"


def print_board(board_to_print):
    s = ' '
    for row in board_to_print:
        print(s.join(row))


def user_sizes(how_many_ships):
    user_ship_sizes_func = []
    while how_many_ships > 0:
        user_ship_sizes_func.append(int(input("Size of Each Ship(Largest First):")))
        how_many_ships -= 1
    return user_ship_sizes_func


def direction(initial_position, size):
    row = initial_position[0]
    col = initial_position[1]
    add_spaces = size - 1
    directs = []

    if row >= add_spaces:
        directs.append(0)
    if row < board_size - add_spaces:
        directs.append(2)
    if col >= add_spaces:
        directs.append(3)
    if col < board_size - add_spaces:
        directs.append(1)
    random_length = len(directs) - 1
    rand = randint(0, random_length)
    dir_func = directs[rand]
    return dir_func


def random_pos():
    ship_row = randint(0, board_size_zero)
    ship_col = randint(0, board_size_zero)
    return [ship_row, ship_col]


def get_ship_positions(size):
    ship_positions = []
    initial_position = []
    a = True
    while a:
        initial_position = random_pos()
        center_min = board_size - size + 1
        center_max = size - 2
        a = False
        if center_min <= initial_position[0] <= center_max and center_min <= initial_position[1] <= center_max:
            a = True

    avail_direction = direction(initial_position, size)
    i = 1
    ship_positions.append(initial_position)

    if avail_direction == 0:
        while size > 1:
            ship_positions.append([initial_position[0] - i, initial_position[1]])
            size -= 1
            i += 1
    elif avail_direction == 1:
        while size > 1:
            ship_positions.append([initial_position[0], initial_position[1] + i])
            size -= 1
            i += 1
    elif avail_direction == 2:
        while size > 1:
            ship_positions.append([initial_position[0] + i, initial_position[1]])
            size -= 1
            i += 1
    else:
        while size > 1:
            ship_positions.append([initial_position[0], initial_position[1] - i])
            size -= 1
            i += 1
    return ship_positions


def place_all_ships(ship_sizes):
    b = 0
    ships = []
    ship_next = []
    while ship_sizes:
        while True:
            ship_next = get_ship_positions(ship_sizes[0])
            redo = 0
            for j in range(len(ship_next)):
                if ship_next[j] in taken_positions:
                    redo = 1
            if redo == 0:
                break
        ships.append(ship_next)
        for i in ship_next:
            taken_positions.append(i)
        del(ship_sizes[0])
        print_ship(ships[b])
        b += 1
    return ships


def get_board_positions():
    positions_func = []
    i = 0
    let_to_words = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
                    11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T'}
    while i < board_size:
        j = 0
        while j < board_size:
            button_value = let_to_words[i] + str(j+1)
            positions_func.append(button_value)
            j += 1
        i += 1
    return positions_func


def get_btn_dict(positions_func, board_size_func, command_function):
    btn_dict_func = {}
    c = 1
    r = 1
    for pos in positions_func:
        # pass each button's text to a function
        action = lambda x = pos: command_function(x)
        # create the buttons and assign to pos:button-object dict pair
        btn_dict_func[pos] = Button(mainframe, image=ocean_pic, command=action)
        btn_dict_func[pos].grid(row=r, column=c, pady=0, padx=0)
        c += 1
        if c == board_size_func + 1:
            c = 1
            r += 1
    return btn_dict_func


def get_alpha_to_list(positions_func, board_size_func):
    i = 0
    j = 0
    alpha_to_list_func = {}
    for pos in positions_func:
        alpha_to_list_func[pos] = [i, j]
        j += 1
        if j == board_size_func:
            j = 0
            i += 1
    return alpha_to_list_func


def icon(icon_decision):
    if icon_decision == 2:
        ocean_picture = PhotoImage(file="Ocean_large.gif")
        hit_picture = PhotoImage(file="Hit_large.gif")
        miss_picture = PhotoImage(file="Miss_large.gif")
    else:
        ocean_picture = PhotoImage(file="Ocean_small.gif")
        hit_picture = PhotoImage(file="Hit_small.gif")
        miss_picture = PhotoImage(file="Miss_small.gif")
    return [ocean_picture, hit_picture, miss_picture]


root = Tk()
root.title("Battleship")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Game Info #
user_ship_list = []
info = on_open()
board_size = info[0]
turns = info[1]
user_ship_sizes = info[2]
icon_setting = info[3]
game_mode = info[4]
board_size_zero = board_size - 1
ocean_pic, hit_pic, miss_pic = icon(icon_setting)

# SetUp Board
board_cpu = []
board_cpu_visual = []
taken_positions = []
for x in range(board_size):
    board_cpu.append(["O"] * board_size)
    board_cpu_visual.append(["O"] * board_size)

# Develop Dictionaries based on board size
positions = get_board_positions()
btn_dict = get_btn_dict(positions, board_size, user_guess)
alpha_to_list = get_alpha_to_list(positions, board_size)

cpu_ship_list = place_all_ships(user_ship_sizes)

# user_ship_list = []  # Must link to
print("CPU SHIPS: ", cpu_ship_list)
print("Player SHIPS: ", user_ship_list)
num_ships_sunk = 0

# run the GUI event loop
root.mainloop()
