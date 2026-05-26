import keyboard
import time
import pyperclip
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import threading
from tkinter import messagebox
import os
import pydirectinput
import sys

# RESOURCE PATH FUNCTION MUST BE AT THE TOP (always)
def resource_path(relative_path):
    try:

        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)
# ^^^^ this whole thing above makes images and files port into the exe when run on other PC.

messagebox.showinfo("Info","How To Use:\n1. Open CS2 console.\n2. Bring this app's window on top of CS2's.\n3. Select the config you want to use (click on it).\n4. Normal config makes all user inputs change UI color, CMA version only changes when you shoot.\n5. Wait until the 'Done' window pops up.\n6. To apply another config or to retry applying the same one click Exit and restart it.\n7. TO PROCEED CLOSE THIS WINDOW OR PRESS OK.")

def startscript():
    btn.config(state='disabled', text='Running...')
    thread = threading.Thread(target=run_script, daemon=True)
    thread.start()
#threading to make apps run instantly( use threading.Thread and the put the target function, daemon should be True.)
def startscript2():
    btn2.config(state='disabled', text='Running...')
    thread = threading.Thread(target=run_sma, daemon=True)
    thread.start()
def startscript3():
    btn4.config(state='disabled', text='Running...')
    thread = threading.Thread(target=autohop, daemon=True)
    thread.start()
def startscript4():
    btn5.config(state='disabled', text='Running...')
    thread = threading.Thread(target=spinbot, daemon=True)
    thread.start()
last_space_time = 0
space_delay = 0.01  # 10ms delay between space presses
bhopping = False
p_pressed_last = False
def spinbot():
    global moving, stop_moving
    pydirectinput.PAUSE = 0 # the thing to allow gfn compatability

    moving = False # bools to spin
    stop_moving = False
    SPEED = 300  # speed

    def move_continuously():
        global moving, stop_moving
        while not stop_moving:
            if moving:
                pydirectinput.moveRel(SPEED, 0, relative=True) # while L is held, spin.
            time.sleep(0.001)

    def start_moving(): # move and stop move func
        global moving
        moving = True

    def stop_moving_func():
        global moving
        moving = False

    stop_moving = False
    movement_thread = threading.Thread(target=move_continuously, daemon=True) #threading to catch input
    movement_thread.start()

    keyboard.on_press_key('l', lambda _: start_moving()) #func on
    keyboard.on_release_key('l', lambda _: stop_moving_func()) #func off

    print(f"Hold 'l' to move right at speed: {SPEED}")
    keyboard.wait()
def autohop():
    global bhopping, current_time,p_pressed_last,p_pressed,last_space_time,space_delay
    while True:
        p_pressed = keyboard.is_pressed('p')
    
        # To    ggle when p is first pressed (not held)
        if p_pressed and not p_pressed_last:
            bhopping = not bhopping
            print(f"Auto-bhop: {'ON' if bhopping else 'OFF'}")
    
        p_pressed_last = p_pressed
    
        if bhopping:
            current_time = time.time()
            if current_time - last_space_time >= space_delay:
                keyboard.press_and_release("space")
                last_space_time = current_time
    
        time.sleep(0.001)

def run_sma():
    commands = ["alias colors \"colors0\"",
    "alias colors0 \"cl_hud_color 0; alias colors colors1\"", 
    "alias colors1 \"cl_hud_color 1; alias colors colors2\"", 
    "alias colors2 \"cl_hud_color 2; alias colors colors3\"", 
    "alias colors3 \"cl_hud_color 3; alias colors colors4\"", 
    "alias colors4 \"cl_hud_color 4; alias colors colors5\"", 
    "alias colors5 \"cl_hud_color 5; alias colors colors6\"", 
    "alias colors6 \"cl_hud_color 6; alias colors colors7\"", 
    "alias colors7 \"cl_hud_color 7; alias colors colors8\"", 
    "alias colors8 \"cl_hud_color 8; alias colors colors9\"", 
    "alias colors9 \"cl_hud_color 9; alias colors colors10\"", 
    "alias colors10 \"cl_hud_color 10; alias colors colors11\"", 
    "alias colors11 \"cl_hud_color 11; alias colors colors12\"", 
    "alias colors12 \"cl_hud_color 12; alias colors colors13\"", 
    "alias colors13 \"cl_hud_color 13; alias colors colors0\"", 
    "bind mouse1 \"+attack; colors;\""
    ]
    for line in commands:
        pyperclip.copy(line)
        time.sleep(10)
        keyboard.press_and_release('ctrl+v')
        time.sleep(0.2)
        keyboard.press_and_release('enter')
    messagebox.showinfo('Rainbow Hud','Done')
# CMA CONFIG ^^^
def run_script():
    commands = ["alias colors \"colors0\"",
    "alias colors0 \"cl_hud_color 0; alias colors colors1\"", 
    "alias colors1 \"cl_hud_color 1; alias colors colors2\"", 
    "alias colors2 \"cl_hud_color 2; alias colors colors3\"", 
    "alias colors3 \"cl_hud_color 3; alias colors colors4\"", 
    "alias colors4 \"cl_hud_color 4; alias colors colors5\"", 
    "alias colors5 \"cl_hud_color 5; alias colors colors6\"", 
    "alias colors6 \"cl_hud_color 6; alias colors colors7\"", 
    "alias colors7 \"cl_hud_color 7; alias colors colors8\"", 
    "alias colors8 \"cl_hud_color 8; alias colors colors9\"", 
    "alias colors9 \"cl_hud_color 9; alias colors colors10\"", 
    "alias colors10 \"cl_hud_color 10; alias colors colors11\"", 
    "alias colors11 \"cl_hud_color 11; alias colors colors12\"", 
    "alias colors12 \"cl_hud_color 12; alias colors colors13\"", 
    "alias colors13 \"cl_hud_color 13; alias colors colors0\"", 
    "bind d \"+right; colors;\"", 
    "bind a \"+left; colors;\"", 
    "bind w \"+forward; colors;\"", 
    "bind s \"+back; colors;\"", 
    "bind mouse1 \"+attack; colors;\"",
    "bind space \"+jump; colors;\"",
    "bind c \"+duck; colors;\"",
    ]
    for line in commands:
        pyperclip.copy(line)
        time.sleep(10)
        keyboard.press_and_release('ctrl+v')
        time.sleep(0.2)
        keyboard.press_and_release('enter')
    messagebox.showinfo('Rainbow HUD','Done')
# ^^^^^ normal one (rebind to ctrl if u dont use C)

win = Tk()
win.configure(bg='black')
win.title("ArkStayer's CS2 Tools")
# bg and title window ^^^^

try:
    logo_path = resource_path("logo.png")

    logo_image = Image.open(logo_path)
    icon = ImageTk.PhotoImage(logo_image)
    win.iconphoto(False, icon)
except Exception as e:
    print(f"Could not load icon: {e}")
# logo image to replace default tk one (put the file name into the brackets after resource path.)

win.geometry("325x220")

btn = tk.Button(
    win,
    bg='green',
    fg='black',
    text='Start Rainbow Hud',
    command=startscript
)
#Normal button ^^^
btn2 = tk.Button(
    win,
    bg='cyan',
    fg='black',
    text='Start Rainbow Hud (CMA version)',
    command=startscript2
)
btn4 = tk.Button(
    win,
    bg='purple',
    fg='black',
    text='Start AutoBHOP [P]',
    command=startscript3
)
btn5 = tk.Button(
    win,
    bg='orange',
    fg='black',
    text='Start spinbot [L]',
    command=startscript4
)
button_frame = tk.Frame(win)
button_frame.pack(pady=10)
# lower button vertically ^^^ ALSO ASSIGN TO FRAME OF WINDOW, MORE THAN 1 PACKED BUTTON  DOES NOT WORK ON WIN LAYER.
exitbtn = tk.Button(
    button_frame,
    bg='red',
    fg='black',
    text='Exit',
    command=win.destroy
)
# EXIT BUTTON ^^^^
exitbtn.pack()
btn.pack()
btn2.pack(pady=10)
btn4.pack(pady=10)
btn5.pack(pady=10)
#always to .pack(option)
win.mainloop()