def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 1)
    servos.P0.set_angle(90)
    music.play(music.tone_playable(262, music.beat(BeatFraction.BREVE)),
        music.PlaybackMode.UNTIL_DONE)
    pins.digital_write_pin(DigitalPin.P2, 0)
    pins.digital_write_pin(DigitalPin.P1, 1)
    servos.P0.set_angle(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

pins.digital_write_pin(DigitalPin.P1, 1)