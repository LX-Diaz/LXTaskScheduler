import tkinter as tk
from tkinter import ttk
import sv_ttk
from time import *
import configparser


class DesktopClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.date_String = strftime('%m/%d/%Y')
        self.time_string = strftime('%I:%M:%S %p')

        w = 100  # width for the Tk root
        h = 50  # height for the Tk root

        # get screen width and height
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws) - (w)
        y = (hs) - (h)

        #set the dimensions and position of the screen
        self.geometry(f'{w}x{h}')
        self.geometry(f'+{int(x)}+{int(y)}')
        self.overrideredirect(True)
        self.attributes('-topmost', True, '-alpha', 0.5)
        self.dclock_label = ttk.Label(self)
        self.ddate_label = ttk.Label(self)
        # Grid widgets to deskClock
        self.dclock_label.grid(column=0, row=0, padx=1, pady=1, sticky='EW' + 'NS')
        self.ddate_label.grid(column=0, row=1, padx=1, pady=1, sticky='EW' + 'NS')
        self.UpdateDeskClock()
        # Set the Style of the app
        sv_ttk.set_theme('dark')

    def time(self):
        self.date_String = strftime('%m/%d/%Y')
        self.time_string = strftime('%I:%M:%S %p')
        return self.date_String, self.time_string

    def UpdateDeskClock(self):
        self.time()
        self.ddate_label.config(text=self.date_String)
        self.dclock_label.config(text=self.time_string)
        self.dclock_label.grid(column=0, row=0, padx=1, pady=1, sticky='NE')
        self.ddate_label.grid(column=0, row=1, padx=1, pady=1, sticky='NE')
        self.dclock_label.after(1000, self.UpdateDeskClock)


if __name__ == '__main__':
    dc = DesktopClock()
    dc.mainloop()