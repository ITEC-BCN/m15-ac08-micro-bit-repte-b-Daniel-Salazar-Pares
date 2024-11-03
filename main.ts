//  Melodía predefinida
//  Melodía personalizada
//  Cambia la velocidad según la inclinación de Y
input.onButtonPressed(Button.A, function on_button_a_pressed() {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Birthday), music.PlaybackMode.InBackground)
})
input.onButtonPressed(Button.B, function on_button_b_pressed() {
    music.play(music.tonePlayable(Note.C, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(Note.E, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(Note.G, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(Note.F, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(Note.E, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(Note.D, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(Note.C, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
})
basic.forever(function on_forever() {
    let acc_y = input.acceleration(Dimension.Y)
    let tempo = 120 + Math.trunc(acc_y / 10)
    music.setTempo(tempo)
})
