import os
import time
from enum import Enum

TEXT = "test"
MAX_LINE_LENGTH = 20
DELAYS_BETWEEN_ANIMATIONS = 0.05

COUNTER = 0

# each animation should return the initial position of text on the left side of the screen
class MovementType(Enum):
    NO_ANIMATION = 0
    BOUNCE = 1
    LETTER_BY_LETTER_BOUNCE = 2

def clear_screen():
    global COUNTER
    os.system('cls' if os.name == 'nt' else 'clear')
    COUNTER = COUNTER + 1

def animate_text(movement_type = MovementType.NO_ANIMATION):
    if movement_type == MovementType.BOUNCE:
        animate_bounce()
    if movement_type == MovementType.LETTER_BY_LETTER_BOUNCE:
        animate_letter_by_letter()
    elif movement_type == MovementType.NO_ANIMATION:
        do_nothing()

def animate_letter_by_letter():
    letter_on_left = len(TEXT)
    letter_on_right = 0
    # 1 == right, -1 == left
    direction = 1

    while True:
        # move one letter to the direction
       
        # print(letter_on_left, letter_on_right)
        letter_to_move = TEXT[letter_on_right] if direction == 1 else TEXT[letter_on_left]

        # update the number of letters on each side
        if direction == 1:
            letter_on_left -= 1
        else:
            letter_on_right -= 1
        
        if letter_to_move != ' ':
            # animate the movement of the letter
            pos = 0 if direction == 1 else MAX_LINE_LENGTH - len(TEXT)
            while True:
                clear_screen()
                space = ' ' * (MAX_LINE_LENGTH - len(TEXT) + 1)
                space = space[:pos] + letter_to_move.upper() + space[pos+1:]
                print(TEXT[0:letter_on_left] + space + TEXT[len(TEXT) - letter_on_right:])
                pos = pos + direction
                if pos == 0 or pos == (MAX_LINE_LENGTH - len(TEXT)):
                    break
                time.sleep(DELAYS_BETWEEN_ANIMATIONS)

        # update the number of letters on each side
        if direction == 1:
            letter_on_right += 1
        else:
            letter_on_left += 1

        # swap direction if we reach the end of the text
        if letter_on_left == 0:
            direction = -1
        if letter_on_right == 0:
            direction = 1
        # stop the animation after the first cycle
        if letter_on_right == 0:
            return


def do_nothing():
    count = 0 
    while True:
        clear_screen()
        print(TEXT)
        count += 1
        if(count == 10):
            return
        time.sleep(DELAYS_BETWEEN_ANIMATIONS)

def animate_bounce():
    direction = 1
    position = 0
    while True:
        clear_screen()
        padding = ' ' * position
        print(padding + TEXT)
        time.sleep(DELAYS_BETWEEN_ANIMATIONS)

        if position == MAX_LINE_LENGTH - len(TEXT) - 1:
            direction = -1
        elif position == 0:
            direction = 1
        position += direction
        if position == 0:
            return

if __name__ == "__main__":
    input_text = input("Enter the text: ")
    input_max_line_length = int(input("Enter the max line length: "))
    
    if input_max_line_length < len(input_text):
        print("Error: Max line length must be greater than or equal to the length of the text.")
        exit(1)

    TEXT = input_text
    MAX_LINE_LENGTH = input_max_line_length

    while True:
        animate_text(MovementType.BOUNCE)
        animate_text(MovementType.LETTER_BY_LETTER_BOUNCE)
        
