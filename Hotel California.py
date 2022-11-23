def on_button_pressed_a():
    music.play_melody("B3:2 F#4:1 D5:2 F#5:2 D5:1 B5:4 D5:2 E5:2 A#4:2 E5:1 F#5:2 C#6:2 E5:1 F#5:8 A4:2 E5:1 A5:2 B5:2 E5:1 A5:4 E5:4", 72)
input.on_button_pressed(Button.A, on_button_pressed_a)
