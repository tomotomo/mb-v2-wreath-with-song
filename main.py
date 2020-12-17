def on_logo_pressed():
    global tone
    tone = 233
    for index in range(32):
        tone += 12
        music.play_tone(tone, music.beat(BeatFraction.SIXTEENTH))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

level = 0
tone = 0
spell = 0
input.set_sound_threshold(SoundThreshold.LOUD, 180)
basic.clear_screen()

def on_forever():
    global level
    level = Math.map(input.sound_level(), 0, 225, 0, 7)
    pins.analog_write_pin(AnalogPin.P0, Math.map(input.sound_level(), 0, 225, 0, 1023))
    if level > 5:
        basic.show_leds("""
            # . # . #
            . # # # .
            # . # . #
            # # . # #
            . . # . .
            """)
    elif level > 4:
        basic.show_leds("""
            . . # . .
            # # . . #
            # . . # #
            . . # . .
            . # . # .
            """)
    elif level > 3:
        basic.show_leds("""
            . . . # .
            . # . . #
            # . # . .
            . # . # .
            . . # . .
            """)
    elif level > 2:
        basic.show_leds("""
            . . . . #
            # . . . .
            . . . # .
            . . # . .
            . # . . #
            """)
    elif level > 1:
        basic.show_leds("""
            . . . . #
            . # . . .
            . . . . .
            . . . . .
            # . . . #
            """)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            """)
basic.forever(on_forever)
