# encoding utf-8
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import sv_ttk
import configparser
import time
import sched
import timer
import pygame
import threading
import sqlite3



class ReminderManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.threads = []
        self.clock = None
        self.timerdisp = None
        self.message = None
        self.reminders_dict = {}
        self.config = configparser.ConfigParser()
        self.config.read('timeconfig.ini')
        sv_ttk.set_theme(self.config['OPTIONS']['theme'])
        #DBCursor = sqlite3.connect("reminders.db")
        style = ttk.Style()
        self.clock = time.strftime('%I:%M:%S %p')
        print(f'[***] Program started at {self.clock}')
        self.schd = sched.scheduler(time.time, time.sleep)
        self.start_threads()


    def reminder_loop(self, message, minutes):
        seconds = minutes * 60
        while True:
            self.schd.enter(seconds, 1, self.print_message, argument=(message,))
            self.schd.run()
            time.sleep(1)
        print(f'[***] Program ended at {self.clock}')

    def print_message(self, message):
        print(message)

    def start_threads(self):
        #self.import_reminders()
        for key in self.config['REMINDERS']:
            message = key
            minutes = self.config['REMINDERS'][key]

            self.threads.append(threading.Thread(target=self.reminder_loop, args=(message, int(minutes))))
        for thread in self.threads:
            print(thread)
            thread.start()

RM = ReminderManager()
# RM.start_reminders()
