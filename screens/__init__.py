from tkinter import *

import requests
from apscheduler.schedulers.background import BackgroundScheduler


class MainScreen:

    def __init__(self):
        scheduler = BackgroundScheduler()

        window = Tk()

        window.title("League Game Analyser")
        window.geometry('350x200')

        lbl = Label(window, text="Status")
        lbl.grid(column=0, row=0)

        listenerStatus = Label(window, text="Ready")
        listenerStatus.grid(column=1, row=0)

        def runApiCall():
            try:
                api_url = "https://127.0.0.1:2999/liveclientdata/allgamedata"
                response = requests.get(api_url, timeout=0.01)
                print(response.json())
            except:
                print("failed")

        def startListener():
            scheduler.add_job(runApiCall, 'interval', seconds=5)
            scheduler.start()
            listenerStatus.config(text="waiting for game...")


        def stopListener():
            scheduler.shutdown()
            listenerStatus.config(text="Ready")

        startListenerBtn = Button(window, text="Start Listener", command=startListener)
        startListenerBtn.grid(column=0, row=1)

        window.mainloop()
