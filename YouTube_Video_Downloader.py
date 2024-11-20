from tkinter import *
from pytubefix import YouTube

def download_video():
    url = link.get()
    try:
        YouTube(url).streams.first().download()
        Label(root, text='Downloaded', font='arial 15').pack()
    except Exception as e:
        Label(root, text='Error: ' + str(e), font='arial 15').pack()

root = Tk()
root.title("YouTube Video Downloader")
link = StringVar()
Label(root, text='Paste Link Here:', font='arial 15 bold').pack()
Entry(root, textvariable=link, width=70).pack()
Button(root, text='Download', command=download_video).pack()
root.mainloop()