def on_button_pressed_a():
    global x
    x = 255
    basic.show_string("Sending")
    for index in range(256):
        basic.show_number(x)
        radio.set_group(x)
        radio.send_string("Nobody Expects The Spanish Inquisition")
        if x > 0:
            x += -1
        elif x == 0:
            x = 255
input.on_button_pressed(Button.A, on_button_pressed_a)

x = 0
basic.show_string("Hello!")
