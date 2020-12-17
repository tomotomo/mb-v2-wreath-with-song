input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    tone = 233
    for (let index = 0; index < 32; index++) {
        tone += 12
        music.playTone(tone, music.beat(BeatFraction.Sixteenth))
    }
})
let tone = 0
basic.clearScreen()
basic.forever(function () {
    pins.analogWritePin(AnalogPin.P0, Math.map(input.soundLevel(), 0, 225, 0, 1023))
    led.plotBarGraph(
    180 - input.soundLevel(),
    255
    )
})
