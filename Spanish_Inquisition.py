#Press button a
def on_button_pressed_a():
    #Define our x variable, which is what will loop radio group down from 256 to 0
    global x
    x = 255
    #Send that message to anyone on the radio channel
    radio.send_string("Nobody Expects The Spanish Inquisition")
    #Loop over 256 times (there's 256 radio groups)
    for i in range(256):
        radio.set_group(x)
        #Iterate down by 1
        x -= 1
        #If x reaches the last radio group, bring it back to the start
        if x == 0:
            x = 255
input.on_button_pressed(Button.A, on_button_pressed_a)