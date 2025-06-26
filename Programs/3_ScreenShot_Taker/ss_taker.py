from tkinter import*
import pyautogui
import time
import datetime

root = Tk()
root.geometry("400x200")


def Start():
    global i
    global running
    
    running = True
    my_date = datetime.datetime.now().strftime("%d %m %Y, %H %M %S")
    
    if running:
        ss = pyautogui.screenshot()
        ss.save(f"D:\\Python Intership Programs\\Programs\\3_ScreenShot_Taker\\image-{i} at {my_date}.jpg")
        i = i + 1
        
        root.after("5000", Start)


def Stop():
    global running
    running = False
    
    root.quit()
    
i = 0
running = False

start_button = Button(root, text="Start ScreenShot", command=Start)
start_button.pack()

stop_button = Button(root, text="Stop ScreenShot", command=Stop)
stop_button.pack()

root.mainloop()