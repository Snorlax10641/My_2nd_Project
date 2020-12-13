def on_button_pressed_a():
    if input.button_is_pressed(Button.B):
        basic.show_icon(IconNames.HEART)
    elif input.button_is_pressed(Button.A):
        basic.show_icon(IconNames.SQUARE)
    elif input.is_gesture(Gesture.SHAKE):
        basic.show_icon(IconNames.DIAMOND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if input.is_gesture(Gesture.SHAKE):
        basic.show_icon(IconNames.SMALL_DIAMOND)
    elif input.button_is_pressed(Button.B):
        basic.show_icon(IconNames.SMALL_SQUARE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    if input.button_is_pressed(Button.AB):
        basic.show_icon(IconNames.HAPPY)
    elif input.is_gesture(Gesture.SHAKE):
        basic.show_icon(IconNames.CHESSBOARD)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_string("Try Me!")