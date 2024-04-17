# encoding utf-8
import configparser
import time
import sched
import threading


class ReminderManager():
    def __init__(self):
        super().__init__()
        self.threads = []
        self.clock = None
        self.timerdisp = None
        self.message = None
        self.reminders_dict = {}
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.clock = time.strftime('%I:%M:%S %p')
        print(f'[***] Program started at {self.clock}')
        self.schd = sched.scheduler(time.time, time.sleep)
        self.start_threads()


    def reminder_loop(self, message, minutes):
        seconds = minutes * 60
        while True:
            self.schd.enter(seconds, 1, print, argument=(message,))
            self.schd.run()
            time.sleep(1)


    def start_threads(self):
        #self.import_reminders()
        for key in self.config['REMINDERS']:
            message = key
            minutes = self.config['REMINDERS'][key]

            self.threads.append(threading.Thread(target=self.reminder_loop, args=(message, int(minutes))))
        for thread in self.threads:
            print(thread)
            thread.start()
