input.onButtonPressed(Button.A, function () {
    if (input.buttonIsPressed(Button.B)) {
        basic.showIcon(IconNames.Heart)
    } else if (input.isGesture(Gesture.Shake)) {
        basic.showIcon(IconNames.Diamond)
    } else {
        basic.showIcon(IconNames.Square)
    }
})
input.onButtonPressed(Button.B, function () {
    if (input.isGesture(Gesture.Shake)) {
        basic.showIcon(IconNames.SmallDiamond)
    } else {
        basic.showIcon(IconNames.SmallSquare)
    }
})
input.onGesture(Gesture.Shake, function () {
    if (input.buttonIsPressed(Button.AB)) {
        basic.showIcon(IconNames.Happy)
    } else if (input.isGesture(Gesture.Shake)) {
        basic.showIcon(IconNames.Chessboard)
    }
})
basic.showString("Try Me!")
