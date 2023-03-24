def on_button_pressed_a():
    if paddleA.get(LedSpriteProperty.X) > 0:
        paddleA.change(LedSpriteProperty.X, -1)
        paddleB.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    game.resume()
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_ab():
    game.pause()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if paddleA.get(LedSpriteProperty.X) < 3:
        paddleA.change(LedSpriteProperty.X, 1)
        paddleB.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    game.game_over()
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

paddleB: game.LedSprite = None
paddleA: game.LedSprite = None
game.set_life(5)
paddleA = game.create_sprite(2, 4)
paddleB = game.create_sprite(3, 4)
ball = game.create_sprite(randint(0, 4), 0)
directionY = 1
directionX = randint(-1, 1)
basic.pause(500)
game.set_score(0)
sound = 1

def on_forever():
    global directionY, sound, directionX
    ball.change(LedSpriteProperty.X, directionX)
    ball.change(LedSpriteProperty.Y, directionY)
    if ball.is_touching(paddleA) or ball.is_touching(paddleB):
        game.add_score(1)
        ball.change(LedSpriteProperty.X, directionX * -1)
        ball.change(LedSpriteProperty.Y, -1)
        directionY = -1
        if sound == 0:
            music.play_tone(294, music.beat(BeatFraction.HALF))
            basic.pause(100)
            sound = 1
        elif sound == 1:
            music.play_tone(147, music.beat(BeatFraction.HALF))
            basic.pause(100)
            sound = 0
    else:
        if ball.get(LedSpriteProperty.Y) <= 0:
            directionY = 1
            directionX = randint(-1, 1)
        elif ball.get(LedSpriteProperty.Y) >= 4:
            music.play_tone(131, music.beat(BeatFraction.HALF))
            directionY = -1
            game.remove_life(1)
            ball.set(LedSpriteProperty.BLINK, 1)
            basic.pause(2000)
            ball.set(LedSpriteProperty.BLINK, 0)
            if game.score() == 0:
                music.play_melody("B4:1 - B4:1 - B4:1 - B4:5 G4:5 A4:5 B4:4 A4:1 B4:8", 180)
        if ball.get(LedSpriteProperty.X) <= 0:
            directionX = 1
        elif ball.get(LedSpriteProperty.X) >= 4:
            directionX = -1
        basic.pause(500)
basic.forever(on_forever)
