printing = False
S1_RIGHT = 0
S1_LEFT = 0
S2_BACK = 0
S2_FORWARD = 0
S3_BACK = 0
S3_FORWARD = 0
PINCH_OPEN = 0
PINCH_CLOSE = 0
CAR_FORWARD = 0
CAR_BACK = 0
CAR_RIGHT = 0
CAR_LEFT = 0
lower_limit = 0
higher_limit = 0
j1_y = 0
j1_x = 0
j2_y = 0
b1 = 0
b2 = 0
command = 0
def print_direction(position: str):
    if printing:
        basic.show_string(position)
def print_comand(command2: number):
    if printing:
        basic.show_number(command2)

def on_forever():
    global printing, S1_RIGHT, S1_LEFT, S2_BACK, S2_FORWARD, S3_BACK, S3_FORWARD, PINCH_OPEN, PINCH_CLOSE, CAR_FORWARD, CAR_BACK, CAR_RIGHT, CAR_LEFT, lower_limit, higher_limit, j1_y, j1_x, j2_y, b1, b2, command
    radio.set_group(1)
    printing = False
    S1_RIGHT = 1
    S1_LEFT = 2
    S2_BACK = 4
    S2_FORWARD = 8
    S3_BACK = 16
    S3_FORWARD = 32
    PINCH_OPEN = 64
    PINCH_CLOSE = 128
    CAR_FORWARD = 256
    CAR_BACK = 512
    CAR_RIGHT = 1024
    CAR_LEFT = 2048
    lower_limit = 311
    higher_limit = 711
    while True:
        j1_y = pins.analog_read_pin(AnalogPin.P0)
        j1_x = pins.analog_read_pin(AnalogPin.P1)
        j2_y = pins.analog_read_pin(AnalogPin.P2)
        b1 = pins.digital_read_pin(DigitalPin.P14)
        b2 = pins.digital_read_pin(DigitalPin.P15)
        command = 0
        if j1_y < lower_limit:
            command = bitwise.or(command, S2_FORWARD)
            print_direction("j1^")
        elif j1_y > higher_limit:
            command = bitwise.or(command, S2_BACK)
            print_direction("j1v")
        if j1_x < lower_limit:
            command = bitwise.or(command, S1_RIGHT)
            print_direction("j1>")
        elif j1_x > higher_limit:
            command = bitwise.or(command, S1_LEFT)
            print_direction("j1<")
        if j2_y < lower_limit:
            command = bitwise.or(command, S3_FORWARD)
            print_direction("j2v")
        elif j2_y > higher_limit:
            command = bitwise.or(command, S3_BACK)
            print_direction("j2^")
        if input.button_is_pressed(Button.A):
            command = bitwise.or(command, PINCH_CLOSE)
            print_direction("b1")
        elif input.button_is_pressed(Button.B):
            command = bitwise.or(command, PINCH_CLOSE)
            print_direction("b1")
        if input.is_gesture(Gesture.SCREEN_UP):
            command = bitwise.or(command, CAR_FORWARD)
            print_direction("^")
        elif input.is_gesture(Gesture.SCREEN_DOWN):
            command = bitwise.or(command, CAR_BACK)
            print_direction("v")
        if input.is_gesture(Gesture.TILT_LEFT):
            command = bitwise.or(command, CAR_RIGHT)
            print_direction("<")
        elif input.is_gesture(Gesture.TILT_RIGHT):
            command = bitwise.or(command, CAR_LEFT)
            print_direction(">")
        radio.send_string("" + str((command)))
        basic.pause(200)
basic.forever(on_forever)
