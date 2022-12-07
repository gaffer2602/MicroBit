def on_button_pressed_a():
    music.play_melody("D4:2 - B4:2 - A4:2 - G4:2 - D4:6 - D4:1 - D4:1 - D4:2 - B4:2 - A4:2 - G4:2 - E4:6 - E4:2 - C5:2 - B4:2 - A4:2 - F#4:10 - D5:2 - D5:2 - C5:2 - A4:2 - B4:6 - D5:8", 180)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play_melody("B4:2 - B4:2 - B4:4 - B4:2 - B4:2 - B4:4 - B4:2 - D5:2 - G4:3 - A4:1 - B4:8 - C5:2 - C5:2 - C5:3 - C5:1 - C5:2 - B4:2 - B4:2 - B4:1 - B4:1 - B4:2 - A4:2 - A4:2 - B4:2 - A4:4 - D5:4 - B4:2 - B4:2 - B4:4 - B4:2 - B4:2 - B4:4 - B4:2 - D5:2 - G4:3 - A4:1 - B4:8 - C5:2 - C5:2 - C5:3 - C5:1 - C5:2 - B4:2 - B4:2 - B4:1 - B4:1 - D5:2 - D5:2 - C5:2 - A4:2 - G4:8", 240)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_string("Merry Christmas")
basic.forever(on_forever)
