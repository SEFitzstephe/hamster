input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showIcon(IconNames.Sad)
    music.play(music.builtinPlayableSoundEffect(soundExpression.sad), music.PlaybackMode.UntilDone)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    basic.showIcon(IconNames.Happy)
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
})
basic.showIcon(IconNames.Heart)
