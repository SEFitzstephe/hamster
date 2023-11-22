def on_gesture_shake():
    basic.show_icon(IconNames.SAD)
    music.play(music.builtin_playable_sound_effectsoundExpression.sad),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    basic.show_icon(IconNames.HAPPY)
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.UNTIL_DONE)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

basic.show_icon(IconNames.HEART)