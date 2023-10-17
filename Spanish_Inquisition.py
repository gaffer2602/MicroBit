def on_button_pressed_a():
    global x
    for index in range(256):
        radio.send_string("Nobody Expects The Spanish Inquisition")
        if x > 0:
            x += -1
        elif x == 0:
            x = 255
input.on_button_pressed(Button.A, on_button_pressed_a)

x = 0
x = 255
radio.set_group(x)
