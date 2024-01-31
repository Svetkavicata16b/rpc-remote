let printing = false
let S1_RIGHT = 0
let S1_LEFT = 0
let S2_BACK = 0
let S2_FORWARD = 0
let S3_BACK = 0
let S3_FORWARD = 0
let PINCH_OPEN = 0
let PINCH_CLOSE = 0
let CAR_FORWARD = 0
let CAR_BACK = 0
let CAR_RIGHT = 0
let CAR_LEFT = 0
let lower_limit = 0
let higher_limit = 0
let j1_y = 0
let j1_x = 0
let j2_y = 0
let b1 = 0
let b2 = 0
let command = 0
function print_direction (position: string) {
    if (printing) {
        basic.showString(position)
    }
}
function print_comand (command: number) {
    if (printing) {
        basic.showNumber(command)
    }
}
basic.forever(function () {
    radio.setGroup(1)
    printing = false
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
    while (true) {
        j1_y = pins.analogReadPin(AnalogPin.P0)
        j1_x = pins.analogReadPin(AnalogPin.P1)
        j2_y = pins.analogReadPin(AnalogPin.P2)
        b1 = pins.digitalReadPin(DigitalPin.P14)
        b2 = pins.digitalReadPin(DigitalPin.P15)
        command = 0
        if (j1_y < lower_limit) {
            command = bitwise.or(command, S2_FORWARD)
            print_direction("j1^")
        } else if (j1_y > higher_limit) {
            command = bitwise.or(command, S2_BACK)
            print_direction("j1v")
        }
        if (j1_x < lower_limit) {
            command = bitwise.or(command, S1_RIGHT)
            print_direction("j1>")
        } else if (j1_x > higher_limit) {
            command = bitwise.or(command, S1_LEFT)
            print_direction("j1<")
        }
        if (j2_y < lower_limit) {
            command = bitwise.or(command, S3_FORWARD)
            print_direction("j2v")
        } else if (j2_y > higher_limit) {
            command = bitwise.or(command, S3_BACK)
            print_direction("j2^")
        }
        if (input.buttonIsPressed(Button.A)) {
            command = bitwise.or(command, PINCH_CLOSE)
            print_direction("b1")
        } else if (input.buttonIsPressed(Button.B)) {
            command = bitwise.or(command, PINCH_CLOSE)
            print_direction("b1")
        }
        if (input.isGesture(Gesture.ScreenUp)) {
            command = bitwise.or(command, CAR_FORWARD)
            print_direction("^")
        } else if (input.isGesture(Gesture.ScreenDown)) {
            command = bitwise.or(command, CAR_BACK)
            print_direction("v")
        }
        if (input.isGesture(Gesture.TiltLeft)) {
            command = bitwise.or(command, CAR_RIGHT)
            print_direction("<")
        } else if (input.isGesture(Gesture.TiltRight)) {
            command = bitwise.or(command, CAR_LEFT)
            print_direction(">")
        }
        radio.sendString("" + (command))
        basic.pause(200)
    }
})
