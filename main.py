printing = 0
def print_direction(position: str):
    if printing:
        basic.show_string(position)
def print_comand(command: number):
    if printing:
        basic.show_number(command)