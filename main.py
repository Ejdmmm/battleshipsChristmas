"""
random and main code
"""
import random
import localization
import class_date
import pickle
import os

SELECTED_LANG = "en"

def get_lang_setting_from_user():
    """
    get settings of languages from user
    """
    while True:
        localization.print_localization(SELECTED_LANG, "welcome.text")
        localization.print_localization(SELECTED_LANG, "language_sel")
        selected_lang = input("en or cs: ")
        if selected_lang in localization.SUPPORTED_LANG:
            localization.print_localization(SELECTED_LANG, "selected")
            return selected_lang
        localization.print_localization(SELECTED_LANG, "bad_lang")
def user_choosing():
    """
    choosing size of board to play
    """
    while True:
        localization.print_localization(SELECTED_LANG,"board_size")
        user_choose = input()
        if user_choose.isdigit():
            return int(user_choose)

        localization.print_localization(SELECTED_LANG,"bad_type_choose")
def start_game():
    """
    starting game
    """
    board = []
    board_size = user_choosing()
    for game in range(board_size):
        board.append(["O"]* board_size)
    enemies = gen_boats(5, board_size)
    print_board(board)
    print(enemies)
    play(board, enemies, board_size)

def print_board(board):
    """
    printing board to console
    """
    for row in board:
        print(" ".join(row))

def gen_boats(enemies_count, board_size):
    enemies = []
    for x in range (enemies_count):
        boat_x = random.randint(0, board_size - 1)
        boat_y = random.randint(0, board_size - 1)
        enemies.append((boat_x, boat_y))
    return enemies

def play(board, enemies, board_size):
    while True:
        print_board(board)
        localization.print_localization(SELECTED_LANG, "enter_x")
        x = int(input())
        localization.print_localization(SELECTED_LANG, "enter_y")
        y = int(input())

        point = (x, y)
        if point not in enemies:
            localization.print_localization(SELECTED_LANG, "miss")
        else:
            index = x
            print(board[index][:y])
            board[index] = board[index][:y] + list("X") + board[index][y + 1:]
            localization.print_localization(SELECTED_LANG, "hit")
        # zvolit pokusy na základě boardu, kolik měl pokusu, kdy vyhral

def print_last_played_time():
    file_path = 'serialized_obj.bin'
    if os.path.exists(file_path):
        print('The file exists!')
    else:
        print('The file does not exist.')

    deserialized_obj = pickle.loads(file_path)
    with open(file_path, "rb") as file:
        serialized_obj = file.read()
    deserialized_obj.print_date()

def write_last_played_time():
    file_path = 'serialized_obj.bin'
    if os.path.exists(file_path):
        print('The file exists!')
    else:
        print('The file does not exist.')

    new_play = class_date.PlayedTime()
    serialized_obj = pickle.dumps(new_play)
    with open(file_path, "wb") as file:
        file.write(serialized_obj)

if __name__ == "__main__": ## volat metody sem
    print_last_played_time()
    SELECTED_LANG = get_lang_setting_from_user()
    start_game()
    write_last_played_time()
    