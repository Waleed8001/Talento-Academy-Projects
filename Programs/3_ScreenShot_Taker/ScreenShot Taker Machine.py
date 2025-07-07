from tkinter import*
import pyautogui
from tkinter.filedialog import askdirectory
import tkinter.messagebox as tmsg
import datetime

try:
    root = Tk()
    root.geometry("1060x370")
    root.title("ScreenShot Taker Machine")
    root.iconbitmap("ss_icon.ico")
    root.minsize(1060, 370)
    root.maxsize(1060, 370)
    root.resizable(False, False)
    root.config(bg="grey14", pady=20)

    Label(root, text="Welcome to our ScreenShot Taker App", bg="grey14", fg="white",  font=("Arial", 20, "bold")).pack(pady=20)

    # Start Taking ScreenShot
    def Start():
        global i
        global running
        
        my_date = datetime.datetime.now().strftime("Date %d %m %Y Time %H %M %S")
        
        secto_msec = str(int(t.get() * 1000))
        # print(secto_msec)
        if running:
            my_label.config(text="ScreenShot Taking Process has been Started", font=("Arial", 13))
            ss = pyautogui.screenshot()
            ss.save(f"{direct.cget('text')}\\image-{i} at {my_date}.jpg")
            i = i + 1
            
            root.after(secto_msec, Start)

    # Ready for Start
    def takess():
        try:
            if my_label.cget('text') == "ScreenShot Stop":
                my_label.config(text="")
                
            if direct.cget("text") == "" or not t.get().is_integer():
                tmsg.showerror(title="Error", message="Please choose a Directory or Choose Valid Number")
            
            else:
                dir_button.config(state=DISABLED)
                t_e.config(state=DISABLED)
                global running
                running = True
                Start()
        
        except Exception as e:
            tmsg.showerror(title="Error", message="Enter Valid Number")
        
            
    # Stop ScreenShot Process
    def Stop():
        if my_label.cget('text') == "ScreenShot Stop" or my_label.cget('text') == "ScreenShot already Stopped":
            my_label.config(text="ScreenShot already Stopped", font=("Arial", 13))
        
        else:   
            dir_button.config(state=NORMAL)
            t_e.config(state=NORMAL)
            global running
            running = False
            dir_button['background'] = "PaleTurquoise1"
        
            my_label.config(text="ScreenShot Stop", font=("Arial", 13))

    # Hover system in Start Button    
    def on_enter(e):
        start_button['background'] = 'honeydew3'

    def on_leave(e):
        start_button['background'] = "PaleTurquoise1"

    # Hover system in Stop Button    
    def on_enter_2(e):
        stop_button['background'] = "honeydew3"

    def on_leave_2(e):
        stop_button['background'] = "PaleTurquoise1"
        
    # Hover system in Choose Path Button   
    def on_enter_3(e):
        dir_button['background'] = "honeydew3"

    def on_leave_3(e):
        dir_button['background'] = "PaleTurquoise1"
        
    # Select Directory for Storing ScreenShots
    def find_Directory():
        directory = askdirectory()
        direct.config(text=directory)
        # print(direct.cget("text"))
        
        
    # Initialize
    i = 0
    running = False

    # Frame for Directory
    f1 = Frame(root, bg="grey14")
    dir_label = Label(f1, text="Where to store your Screenshots?", bg="grey14", fg="white", font=("Arial", 13)).pack(side=LEFT)

    # direct_str = StringVar()
    # direct_str.set("")
    direct = Label(f1, bg="black", width=30, fg="white", height=1, font=(("Calibri", 12)))
    direct.pack(side=LEFT, padx=(15, 20))

    dir_button = Button(f1, text="Choose Directory", command=find_Directory, borderwidth=1, bg="PaleTurquoise1", activebackground="grey36", font=("Segoe UI", 9, "bold"))
    dir_button.pack(side=RIGHT, pady=15)
    dir_button.bind("<Enter>", on_enter_3)
    dir_button.bind("<Leave>", on_leave_3)

    f1.pack(pady=(0, 7))

    # Frame for Choosing Time
    f2 = Frame(root, bg="grey14")

    Label(f2, text="Enter Time Interval (In Seconds):", bg="grey14", fg="white", font=("Arial", 13)).pack(side=LEFT, padx=(0, 28))
    t = IntVar()
    t.set(5)
    Label(f2, text="sec", bg="grey14", fg="white", font=("Arial", 13)).pack(side=RIGHT)

    t_e = Entry(f2, textvariable=t, font=("Calibri", 12))
    t_e.pack()

    f2.pack(padx=(51, 0), pady=(0, 7), anchor="nw")

    # Frame for Buttons
    btn_frame = Frame(root, bg="grey14")

    start_button = Button(btn_frame, text="Start ScreenShot", command=takess, borderwidth=1, bg="PaleTurquoise1", activebackground="grey36", font=("Segoe UI", 9, "bold"))
    start_button.pack(side=LEFT, padx=(0, 20))
    start_button.bind("<Enter>", on_enter)
    start_button.bind("<Leave>", on_leave)

    stop_button = Button(btn_frame, text="Stop ScreenShot", command=Stop, borderwidth=1, bg="PaleTurquoise1", activebackground="grey36", font=("Segoe UI", 9, "bold"))
    stop_button.pack(side=LEFT, padx=(0, 15))
    stop_button.bind("<Enter>", on_enter_2)
    stop_button.bind("<Leave>", on_leave_2)

    my_label = Label(btn_frame, text="", font=("Arial", 15), bg="grey14", fg="white")
    my_label.pack(side=LEFT)

    btn_frame.pack(padx = (56, 0), pady=(20, 0), anchor="w")

    root.mainloop()

except Exception as e:
    tmsg.showerror(title="Error", message="Please retry!!")