import random
from cs1lib import *

WIN_H = 400  # Game will work perfectly fine for whatever height and width you choose for the window
WIN_W = 400
X_RIGHT_LIMIT = WIN_W
Y_DOWN_LIMIT = WIN_H
PAD_W = 20
PAD_H = 80
Y_UP_LIMIT = 0
X_LEFT_LIMIT = 0
move = 10
v_increase = 0.3
move_increase = 1
vx = 3
vy = 3
CR = 10
back_r = random.uniform(0, 1)
back_g = random.uniform(0, 1)
back_b = random.uniform(0, 1)
ball_r = random.uniform(0, 1)
ball_g = random.uniform(0, 1)
ball_b = random.uniform(0, 1)
cx = X_RIGHT_LIMIT // 2
cy = Y_DOWN_LIMIT // 2
x_right = X_RIGHT_LIMIT - PAD_W
y_right = Y_DOWN_LIMIT // 2 - PAD_H // 2
x_left = X_LEFT_LIMIT
y_left = Y_DOWN_LIMIT // 2 - PAD_H // 2
start = False
restart = False
qpress = False
apress = False
zpress = False
kpress = False
mpress = False


def pong_game():  # Calling helper functions into the main game function
    paddle_motion()
    game_features()
    ball_motion()
    restart_()


def game_features():
    # Set background colour
    set_clear_color(back_r, back_g, back_b)
    clear()
    set_stroke_color(0, 0, 0)
    draw_line(200, 0, 200, 400)
    disable_fill()
    draw_circle(200, 200, 50)
    # Draw paddles
    disable_fill()
    set_fill_color(ball_b, back_r, ball_g)
    draw_rectangle(x_left, y_left, PAD_W, PAD_H)  # Left paddle
    draw_rectangle(x_right, y_right, PAD_W, PAD_H)  # Right paddle
    # Draw ball
    disable_fill()
    set_stroke_color(0, 0, 0)
    set_fill_color(ball_r, ball_g, ball_b)

    draw_circle(cx, cy, CR)


def keypress(value):
    global cx, cy, y_left, y_right
    global apress, zpress, mpress, kpress, qpress, start, restart
    if value == "z":
        zpress = True
    if value == "m":
        mpress = True
    if value == "a":
        apress = True
    if value == "k":
        kpress = True
    if value == "q":
        qpress = True
    if value == " ":
        start = True
    if value == " ":
        restart = True
    if qpress:
        cs1_quit()


def keyrelease(value):
    global cx, cy, y_left, y_right
    global zpress, apress, mpress, kpress, qpress, start, restart
    if value == "z":
        zpress = False
    if value == "m":
        mpress = False
    if value == "a":
        apress = False
    if value == "k":
        kpress = False
    if value == "q":
        qpress = False
    if value == " ":
        restart = False


def paddle_motion():
    global y_left, y_right
    if zpress:
        if y_left < Y_DOWN_LIMIT - PAD_H:
            y_left += move
    if mpress:
        if y_right < Y_DOWN_LIMIT - PAD_H:
            y_right += move
    if apress:
        if y_left > Y_UP_LIMIT:
            y_left -= move
    if kpress:
        if y_right > Y_UP_LIMIT:
            y_right -= move
    if qpress:
        cs1_quit()


def ball_motion():
    global cx, cy, vx, vy, y_left, start, y_left, y_right, x_left, x_right, restart
    global move, v_increase, ball_r, ball_g, ball_b, back_r, back_g, back_b

    if start:  # Ball bounces back after it hits the paddles
        if x_right <= (cx + CR) and y_right <= cy <= (y_right + PAD_H):
            ball_r = random.uniform(0, 1)
            ball_g = random.uniform(0, 1)
            ball_b = random.uniform(0, 1)
            back_r = random.uniform(0, 1)
            back_g = random.uniform(0, 1)
            back_b = random.uniform(0, 1)
            cx -= (CR + 1)  # To stop ball from continuously bouncing on paddle
            vx += v_increase
            vx = -vx
            move += move_increase
        cx += vx
        if (x_left + PAD_W) >= (cx - CR) and y_left <= cy <= (y_left + PAD_H):
            ball_r = random.uniform(0, 1)
            ball_g = random.uniform(0, 1)
            ball_b = random.uniform(0, 1)
            back_r = random.uniform(0, 1)
            back_g = random.uniform(0, 1)
            back_b = random.uniform(0, 1)
            cx += (CR + 1)
            vx = abs(vx)
            vx += v_increase
            move += move_increase
        cx += vx

    if start:  # Ball bounces off horizontal walls
        if cy + CR >= Y_DOWN_LIMIT:
            ball_r = random.uniform(0, 1)
            ball_g = random.uniform(0, 1)
            ball_b = random.uniform(0, 1)
            vy += v_increase
            vy = -vy
        cy += vy
        if Y_UP_LIMIT <= cy <= CR:
            ball_r = random.uniform(0, 1)
            ball_g = random.uniform(0, 1)
            ball_b = random.uniform(0, 1)
            vy = abs(vy)
            vy += v_increase

        cy += vy


def restart_():
    global restart, CR, cx, cy, x_right, x_left, y_left, y_right
    global vx, vy, move

    if cx >= X_RIGHT_LIMIT or cx <= X_LEFT_LIMIT:  # if the ball hits vertical walls, game restarts
        restart = True

    if restart:  # If spacebar is pressed, the game restarts
        cx = X_RIGHT_LIMIT // 2
        cy = Y_DOWN_LIMIT // 2
        x_right = X_RIGHT_LIMIT - PAD_W
        y_right = Y_DOWN_LIMIT // 2 - PAD_H // 2
        x_left = X_LEFT_LIMIT
        y_left = Y_DOWN_LIMIT // 2 - PAD_H // 2
        vx = 3
        vy = 3
        move = 10


start_graphics(pong_game, key_press=keypress, height=WIN_H, width=WIN_W, key_release=keyrelease)
