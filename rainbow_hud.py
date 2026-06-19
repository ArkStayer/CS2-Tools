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
import ctypes
from ctypes import wintypes
import pyautogui
import keyboard
import time
import threading
import mouse
import webbrowser
from tkinter import simpledialog
import subprocess
import pydirectinput
import time
import psutil
import string
# RESOURCE PATH FUNCTION MUST BE AT THE TOP (always)
def resource_path(relative_path):
    try:

        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)
# ^^^^ this whole thing above makes images and files port into the exe when run on other PC.
import os

def scan():
    common_paths = [
        r'Program Files\AutoHotkey'
    ]
    
    drives = [f'{d}:\\' for d in string.ascii_uppercase if os.path.exists(f'{d}:\\')]
    

    
    for drive in drives:
        for rel_path in common_paths:
            full_path = os.path.join(drive, rel_path)
            if os.path.isdir(full_path):
                return full_path
    
    return None


ahk_path = scan()
    
if ahk_path:
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
    def startscript5():
        btn6.config(state='disabled', text='Running...')
        thread = threading.Thread(target=crosshair, daemon=True)
        thread.start()
    def startscript6():
        btn7.config(state='disabled', text='Running...')
        thread = threading.Thread(target=macro, daemon=True)
        thread.start()
    def startscript7():
        btn8.config(state='disabled', text='Running...')
        thread = threading.Thread(target=lineup, daemon=True)
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
        # get path to the ahk script
        script_path = resource_path("bhop.ahk")
        
        # run AHK using recomended app.
        subprocess.run([script_path], shell=True)
    def macro():        # get path to the ahk script
        script_path = resource_path("rapid.ahk")
        
        # run AHK using recomended app.
        subprocess.run([script_path], shell=True)
    def lineup():        # get path to the ahk script
        def is_numlock_on():
            # check numlock
            VK_NUMLOCK = 0x90
            user32 = ctypes.windll.user32
            # GetKeyState
            # and then check the lowest bit (1 = toggled on).
            return (user32.GetKeyState(VK_NUMLOCK) & 0xFFFF) != 0
        

        if is_numlock_on():
            print("already numlock'd")
        else:
            keyboard.press_and_release('num lock')
        script_path = resource_path("lineup.ahk")
        
        # run AHK using recomended app.
        subprocess.run([script_path], shell=True)
        
    def crosshair():
        WS_EX_LAYERED = 0x80000
        WS_EX_TRANSPARENT = 0x20
        WS_EX_TOOLWINDOW = 0x80
        GWL_EXSTYLE = -20
        CROSSHAIR_COLOR = 'red'
        CROSSHAIR_SIZE = 10
        THICKNESS = 2
        temp_root = tk.Tk()
        temp_root.withdraw()
        poscolors = ['red','green','cyan','blue','purple','black','white','pink']
        color = simpledialog.askstring("Input", "Enter crosshair color, you may use these : red, green, cyan, blue, purple, black, white, pink",
            parent=temp_root
            )
        if color in poscolors:
            CROSSHAIR_COLOR = color
            size = simpledialog.askstring("Input","Enter crosshair size (default is 10):", parent=temp_root)
            if size.isdigit():
                size = int(size)
                CROSSHAIR_SIZE = size
                width = simpledialog.askstring("Input","Enter crosshair width (default is 2):", parent=temp_root)
                if width.isdigit():
                    width = int(width)
                    THICKNESS = width
                else:
                    CROSSHAIR_COLOR = 'red'
                    CROSSHAIR_SIZE = 10
                    THICKNESS = 2
                    messagebox.showwarning("Warning","Invalid crosshair width, proceeding with default...")
            else:
                CROSSHAIR_COLOR = 'red'
                CROSSHAIR_SIZE = 10
                THICKNESS = 2
                messagebox.showwarning("Warning","Invalid crosshair size, proceeding with default...")
        else:
            CROSSHAIR_COLOR = 'red'
            CROSSHAIR_SIZE = 10
            THICKNESS = 2
            messagebox.showwarning("Warning","Invalid crosshair color, proceeding with default...")
        ######################################### CHANGE THESE NOW!!!!

        #########################################
        def make_clickthrough(hwnd):
            style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            style = style | WS_EX_LAYERED | WS_EX_TRANSPARENT | WS_EX_TOOLWINDOW
            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
            ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, 255, 0x01)
        window = tk.Tk()
        window.overrideredirect(True)
        window.attributes('-topmost', True)
        window.attributes('-transparentcolor', 'black')
        w = window.winfo_screenwidth()
        h = window.winfo_screenheight()
        window.geometry(f"{w}x{h}+0+0")
        window.config(bg='black')
        canvas = tk.Canvas(window, bg='black', highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)
        cx, cy = w//2, h//2
        horizontal_line = canvas.create_line(
            cx - CROSSHAIR_SIZE, cy,
            cx + CROSSHAIR_SIZE, cy,
            fill=CROSSHAIR_COLOR, width=THICKNESS
        )
        vertical_line = canvas.create_line(
            cx, cy - CROSSHAIR_SIZE,
            cx, cy + CROSSHAIR_SIZE,
            fill=CROSSHAIR_COLOR, width=THICKNESS
        )
        make_clickthrough(canvas.winfo_id())
        visible = True
        def toggle_crosshair():
            nonlocal visible
            if visible:
                canvas.itemconfig(horizontal_line, state='hidden')
                canvas.itemconfig(vertical_line, state='hidden')
                visible = False
                print("Crosshair hidden")
            else:
                canvas.itemconfig(horizontal_line, state='normal')
                canvas.itemconfig(vertical_line, state='normal')
                visible = True
                print("Crosshair showing")
        keyboard.add_hotkey('n', toggle_crosshair)
        window.mainloop()

    def run_sma():
        def type_with_special_chars(text): #below info
            i = 0
            while i < len(text):
                char = text[i]
                
                if char == '_':

                    pydirectinput.keyDown('shift')
                    pydirectinput.press('-')
                    pydirectinput.keyUp('shift')
                elif char == '+':

                    pydirectinput.keyDown('shift')
                    pydirectinput.press('=')
                    pydirectinput.keyUp('shift')
                elif char == '"':

                    pydirectinput.keyDown('shift')
                    pydirectinput.press("'")  
                    pydirectinput.keyUp('shift')
                else:

                    pydirectinput.write(char)
                

                time.sleep(0.01)
                i += 1

        def run():
            commands = [
                'alias colors "colors0"',
                'alias colors0 "cl_hud_color 0; alias colors colors1"', 
                'alias colors1 "cl_hud_color 1; alias colors colors2"', 
                'alias colors2 "cl_hud_color 2; alias colors colors3"', 
                'alias colors3 "cl_hud_color 3; alias colors colors4"', 
                'alias colors4 "cl_hud_color 4; alias colors colors5"', 
                'alias colors5 "cl_hud_color 5; alias colors colors6"', 
                'alias colors6 "cl_hud_color 6; alias colors colors7"', 
                'alias colors7 "cl_hud_color 7; alias colors colors8"', 
                'alias colors8 "cl_hud_color 8; alias colors colors9"', 
                'alias colors9 "cl_hud_color 9; alias colors colors10"', 
                'alias colors10 "cl_hud_color 10; alias colors colors11"', 
                'alias colors11 "cl_hud_color 11; alias colors colors12"', 
                'alias colors12 "cl_hud_color 12; alias colors colors13"', 
                'alias colors13 "cl_hud_color 13; alias colors colors0"', 
                'bind mouse1 "+attack; colors;"',
            ]
            
            time.sleep(3)
            
            for i, line in enumerate(commands):
                type_with_special_chars(line)
                pydirectinput.press('enter')
                time.sleep(0.2)
            
            messagebox.showinfo("Done!")

        run()

    def run_script():
        def type_with_special_chars(text): # this is a temp fix for _ , ' and + for command pasting. if it aint broke, dont fix it.
            i = 0
            while i < len(text):
                char = text[i]
                
                if char == '_':

                    pydirectinput.keyDown('shift')
                    pydirectinput.press('-')
                    pydirectinput.keyUp('shift')
                elif char == '+':

                    pydirectinput.keyDown('shift')
                    pydirectinput.press('=')
                    pydirectinput.keyUp('shift')
                elif char == '"':

                    pydirectinput.keyDown('shift')
                    pydirectinput.press("'")  
                    pydirectinput.keyUp('shift')
                else:

                    pydirectinput.write(char)
                

                time.sleep(0.01)
                i += 1

        def run():
            commands = [
                'alias colors "colors0"',
                'alias colors0 "cl_hud_color 0; alias colors colors1"', 
                'alias colors1 "cl_hud_color 1; alias colors colors2"', 
                'alias colors2 "cl_hud_color 2; alias colors colors3"', 
                'alias colors3 "cl_hud_color 3; alias colors colors4"', 
                'alias colors4 "cl_hud_color 4; alias colors colors5"', 
                'alias colors5 "cl_hud_color 5; alias colors colors6"', 
                'alias colors6 "cl_hud_color 6; alias colors colors7"', 
                'alias colors7 "cl_hud_color 7; alias colors colors8"', 
                'alias colors8 "cl_hud_color 8; alias colors colors9"', 
                'alias colors9 "cl_hud_color 9; alias colors colors10"', 
                'alias colors10 "cl_hud_color 10; alias colors colors11"', 
                'alias colors11 "cl_hud_color 11; alias colors colors12"', 
                'alias colors12 "cl_hud_color 12; alias colors colors13"', 
                'alias colors13 "cl_hud_color 13; alias colors colors0"', 
                'bind d "+right; colors;"', 
                'bind a "+left; colors;"', 
                'bind w "+forward; colors;"', 
                'bind s "+back; colors;"', 
                'bind mouse1 "+attack; colors;"',
                'bind space "+jump; colors;"',
                'bind c "+duck; colors;"',
            ]
            
            time.sleep(3)
            
            for i, line in enumerate(commands):
                type_with_special_chars(line)
                pydirectinput.press('enter')
                time.sleep(0.2)
            
            messagebox.showinfo("Done!")

        run()
    win = Tk()
    win.configure(bg='#04000d')
    win.title("ArkStayer's CS2 Tools")
    # bg and title window ^^^^
 #   prebackground = Image.open(resource_path("bg.png"))
  #  background = ImageTk.PhotoImage(prebackground)
  #  bg_label = tk.Label(win, image=background)
  #  bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    try:
        logo_path = resource_path("logo.png")
        logo_image = Image.open(logo_path)
        icon = ImageTk.PhotoImage(logo_image)
        win.iconphoto(False, icon)
    except Exception as e:
        print(f"Could not load icon: {e}")
    # logo image to replace default tk one (put the file name into the brackets after resource path.)

    win.geometry("440x490")

    btn = tk.Button(
        win,
        text='Start Rainbow Hud',
        font=('Helvetica', 14, 'bold'),
        border= 0,
        bg='#06001f',
        fg='cyan',
        command=startscript
    )
    #Normal button ^^^
    btn2 = tk.Button(
        win,
        font=('Helvetica', 14, 'bold'),
        border= 0,
        bg='#06001f',
        fg='cyan',
        text='Start Rainbow Hud (CMA version)',
        command=startscript2
    )
    btn4 = tk.Button(
        win,
        font=('Helvetica', 14, 'bold'),
        border= 0,
        bg='#06001f',
        fg='cyan',
        text='Start AutoBHOP',
        command=startscript3
    )
    btn5 = tk.Button(
        win,
        font=('Helvetica', 14, 'bold'),
        border= 0,
        bg='#06001f',
        fg='cyan',
        text='Start spinbot [L]',
        command=startscript4
    )
    btn6 = tk.Button(
        win,
        font=('Helvetica', 14, 'bold'),
        border= 0,
        bg='#06001f',
        fg='cyan',
        text='Display Crosshair Overlay [N]',
        command=startscript5
    )
    btn7 = tk.Button(
        win,
        font=('Helvetica', 14, 'bold'),
        border= 0,
        bg='#06001f',
        fg='cyan',
        text='Rapid Fire',
        command=startscript6
    )
    btn8 = tk.Button(
        win,
        font=('Helvetica', 14, 'bold'),
        border= 0,
        bg='#06001f',
        fg='cyan',
        text='Auto JumpThrow(Numpad 1 , 3)',
        command=startscript7
    )
    button_frame = tk.Frame(win)
    button_frame.pack(pady=10)
    # lower button vertically ^^^ ALSO ASSIGN TO FRAME OF WINDOW, MORE THAN 1 PACKED BUTTON  DOES NOT WORK ON WIN LAYER.
    exitbtn = tk.Button(
        button_frame,
        font=('Helvetica', 14, 'bold'),
        border= 0,
        bg='#06001f',
        fg='#ff123d',
        text='Exit',
        command=win.destroy
    )
    # EXIT BUTTON ^^^^
    exitbtn.pack()
    btn.pack()
    btn2.pack(pady=10)
    btn4.pack(pady=10)
    btn5.pack(pady=10)
    btn6.pack(pady=10)
    btn7.pack(pady=10)
    btn8.pack(pady=10)
    def on_closing():
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] and 'autohotkey' in proc.info['name'].lower():
                    proc.terminate()  # or proc.kill() for force kill
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        win.destroy()

    #always to .pack(option)
    win.protocol("WM_DELETE_WINDOW", on_closing)
    win.mainloop()
else:
    print("no hotkey")
    messagebox.showinfo("Info","Click OK to run AHK installer (Install V 1.1.37.2), then relaunch the program.")
    script_path = resource_path("install_autohotkey.exe")
    subprocess.run([script_path], shell=True)

