# Melodía predefinida
def on_button_a_pressed():
    music._play_default_background(music.built_in_playable_melody(Melodies.BIRTHDAY), music.PlaybackMode.IN_BACKGROUND)

# Melodía personalizada
def on_button_b_pressed():
    music.play(music.tone_playable(Note.C, music.beat(BeatFraction.HALF)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(Note.E, music.beat(BeatFraction.HALF)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(Note.G, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(Note.F, music.beat(BeatFraction.HALF)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(Note.E, music.beat(BeatFraction.QUARTER)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(Note.D, music.beat(BeatFraction.HALF)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(Note.C, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)

# Cambia la velocidad según la inclinación de Y
def on_forever():
    acc_y = input.acceleration(Dimension.Y)
    tempo = 120 + int(acc_y / 10)
    music.set_tempo(tempo)

input.on_button_pressed(Button.A, on_button_a_pressed)
input.on_button_pressed(Button.B, on_button_b_pressed)
basic.forever(on_forever)