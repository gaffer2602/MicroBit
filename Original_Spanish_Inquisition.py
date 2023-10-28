def on_button_pressed_a():
    basic.show_leds("""
        . # # . #
        # # # . #
        # . # . .
        # . # # #
        . . # # .
        """)
    radio.send_string("Nobody expects the Spanish Inquisition!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_string("Nobody expects the Spanish Inquisition!")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
    radio.send_string("Hola")
    radio.send_string("42")
    radio.send_string("Nobody expects the Spanish Inquisition!")
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    if input.light_level() == 0:
        music.play_melody("F B F B F B F B ", 120)
    radio.send_string("Nobody expects the Spanish Inquisition!")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global shake
    if shake % 2 == 0:
        music.set_volume(120)
        shake += 1
    radio.send_string("Nobody expects the Spanish Inquisition!")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    radio.send_number(76)
    radio.send_string("Nobody expects the Spanish Inquisition!")
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

shake = 0
radio_group = 255
for index in range(255):
    radio.set_group(radio_group)
    radio.send_string("" + str((radio.received_packet(RadioPacketProperty.SERIAL_NUMBER))))
    radio.set_transmit_serial_number(True)
    radio.raise_event(EventBusSource.MICROBIT_ID_ACCELEROMETER,
        EventBusValue.MICROBIT_ACCELEROMETER_EVT_DATA_UPDATE)
    radio.send_string("Nobody expects the Spanish Inquisition!")
    radio_group += -1
