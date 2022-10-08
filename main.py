# +--------------------------------------------------------------------+
# |                           Introduction                             |
# |                          ==============                            |
# | A Python Gui Script to Shutdown ,Restart and Logout using Tkinter. |
# +--------------------------------------------------------------------+
# |                   Author : Prashant Bhandari                       |
# |                  ============================                      |
# +--------------------------------------------------------------------+

import os
import platform
import tkinter as tk
from tkinter import messagebox
import tkinter.font as TkFont


def whichos():
    global ops
    ops = platform.system()


def shutdown():
    if ops == "Windows":
        tk.messagebox.showinfo("Info", "Shutting down...")
        os.system("shutdown /s /t 1")
    elif ops == "Linux":
        tk.messagebox.showinfo("Info", "Shutting down...")
        os.system("sudo halt")
    elif ops == "Darwin":
        tk.messagebox.showinfo("Info", "Shutting down...")
        print("Mac")
    else:
        tk.messagebox.showinfo("Info", "Operating System not supported...")


def restart():
    if ops == "Windows":
        tk.messagebox.showinfo("Info", "Restarting...")
        # os.system("shutdown /r /t 1")
    elif ops == "Linux":
        tk.messagebox.showinfo("Info", "Restarting...")
        # os.system("sudo reboot")
    elif ops == "Darwin":
        tk.messagebox.showinfo("Info", "Restarting...")
        # os.system("")
    else:
        tk.messagebox.showinfo("Info", "Operating System not supported...")


def logout():
    if ops == "Windows":
        tk.messagebox.showinfo("Info", "Logging out...")
        # os.system("shutdown -l")
    elif ops == "Linux":
        tk.messagebox.showinfo("Info", "Logging out...")
        # os.system("sudo log out")
    elif ops == "Darwin":
        tk.messagebox.showinfo("Info", "Logging out...")
        # os.system("")
    else:
        tk.messagebox.showinfo("Info", "Operating System not supported...")


def main():
    whichos()
    m = tk.Tk()
    m.title("Panel")
    m.configure(bg="Gray")
    m.geometry("235x224")
    m.minsize(235, 224)
    m.maxsize(235, 224)
    ft = TkFont.Font(family='Times', size=18)
    btn1 = tk.Button(m, font=ft, text="Shutdown", fg="Red", bg="Black", borderwidth="2px", command=shutdown)
    btn1.place(x=30, y=30, width=170, height=40)
    btn2 = tk.Button(m, font=ft, text="Restart", fg="Red", bg="Black", borderwidth="2px", command=restart)
    btn2.place(x=30, y=90, width=170, height=40)
    btn3 = tk.Button(m, font=ft, text="Log out", fg="Red", bg="Black", borderwidth="2px", command=logout)
    btn3.place(x=30, y=150, width=170, height=40)
    m.mainloop()


if __name__ == '__main__':
    main()
