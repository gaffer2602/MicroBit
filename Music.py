def on_button_pressed_a():
    music.play_melody("B4:2 - B4:2 - B4:2 - B4:8 G4:8 A4:8 B4:6 A4:2 B4:16", 240)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play_melody("B4:1 - B4:1 - B4:1 - B4:1 - B4:1 - A4:1 - B4:1 - - - B4:1 - B4:1 - B4:1 - B4:1 - B4:1 - A4:1 - B4:1 - - - B4:1 - B4:1 - B4:1 - B4:1 - B4:1 - A4:1 - A4:1 - - - A4:1 - A4:1 - G4:1 - G4:1 - D5:2 - B4:1 - - - B4:1 - B4:1 - B4:1 - B4:1 - B4:1 - A4:1 - B4:1 - - - B4:1 - B4:1 - B4:1 - B4:1 - B4:1 - A4:1 - B4:1 - - - B4:1 - B4:1 - B4:1 - B4:1 - B4:1 - A4:1 - A4:1 - - - A4:1 - A4:1 - G4:1 - G4:1 - D5:2 - B4:1 - - - - - D5:2 - D5:2 B4:1 A4:1 - G4:1 - D5:2 - D5:2 - D5:2 B4:1 A4:1 - G4:1 - D5:2 - D5:2 - D5:2 B4:1 A4:1 - G4:1 - E5:2 - E5:1 - E5:1 - E5:2 - ", 120)
input.on_button_pressed(Button.B, on_button_pressed_b)
