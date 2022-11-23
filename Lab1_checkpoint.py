# Author : Chikwanda Chisha
# Date: 10/11/2022
from cs1lib import *

W = 20
H = 80
x_right = 400 - W
y_right = 240 - H
x_left = 0
y_left = 160
move = 10
vx = 4
vy = 4
cx = 200
cy = 200
CR = 10
qpress = False
start = False
restart = False
apress = False
zpress = False
kpress = False
mpress = False


def game_features():
    # Set background colour
    set_clear_color(0.8, 0.8, 0.9)
    clear()
    # Draw paddles
    disable_fill()
    disable_stroke()
    set_fill_color(0.5, 0.5, 0.8)
    draw_rectangle(x_left, y_left, W, H)  # Left paddle
    draw_rectangle(x_right, y_right, W, H)  # Right paddle
    # Draw ball
    disable_fill()
    set_fill_color(0, 0, 0)
    draw_circle(cx, cy, CR)


def start_game():
    paddle_motion()
    game_features()
    ball_motion()


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


def paddle_motion():
    global y_left, y_right
    if zpress:
        if y_left < 400 - H:
            y_left += move
    if mpress:
        if y_right < 400 - H:
            y_right += move
    if apress:
        if y_left > 0:
            y_left -= move
    if kpress:
        if y_right > 0:
            y_right -= move
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


def ball_motion():
    global cx, cy, vx, vy, y_left, start, y_left, y_right, x_left, x_right
    if start:
        if x_right <= (cx + CR) and y_right <= cy <= (y_right + H):
            vx = -vx
        cx += vx
        if (x_left + W) >= (cx - CR) and y_left <= cy <= (y_left + H):
            vx = abs(vx)
        cx += vx
 
    if start:
        if cy >= 400:
            vy = -vy
        cy += vy
        if cy <= 0:
            cy += vy

    if cx >= 400 or cx <= 0:
        quit()

    if restart:
        cx = 200
        cy = 200
        x_right = 400 - W
        y_right = 240 - H
        x_left = 0
        y_left = 160


start_graphics(start_game, key_press=keypress, height=400, width=400, key_release=keyrelease)
