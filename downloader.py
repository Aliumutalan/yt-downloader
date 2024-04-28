from tkinter import *
from pytube import YouTube
from os import system
system("pip install pytube")
system("pip install tkinter")
system("exit")

FONT = ("matrix", 20, "bold")
def download720():
    yt=YouTube(urlc.get())
    yt.streams.get_highest_resolution().download("download")
    writer1.config(text=f"<{yt.title}> video downloaded", bg="Blue", pady=20, padx=30, font=("matrix,10,normal"))
    writer1.pack(padx=20 , pady=20)

def download360():
    yt=YouTube(urlc.get())
    yt.streams.get_lowest_resolution().download("download")
    writer1.config(text=f"<{yt.title}> video downloaded",bg="Blue", pady=20, padx=30, font=("matrix,10,normal"))
    writer1.pack(padx=20 , pady=20)

def downloadVoice():
    yt=YouTube(urlc.get())
    yt.streams.get_audio_only().download("download")
    writer1.config(text=f"<{yt.title}> mp3 downloaded",bg="Blue", pady=20, padx=30, font=("matrix,10,normal"))
    writer1.pack(padx=20 , pady=20)

window = Tk()
window.title("Youtube Downloader")
window.minsize(width=300,height=600)

writer1 = Label()

whatdoyou=Label(text="WHAT DO YOU WANT?", padx=20, pady=20, font=FONT)
whatdoyou.pack()

p720download = Button(text="720p video Download", width=20, height=3, command=download720)
p720download.pack(pady=20,padx=20)

p360download = Button(text="360p video Download", width=20, height=3, command=download360)
p360download.pack(pady=20,padx=20)

mp3download = Button(text="mp3 voice Download", width=20, height=3, command=downloadVoice)
mp3download.pack(pady=20,padx=20)

wurl = Label(text="Enter your url : ", font=FONT)
wurl.pack(padx=20, pady=20)

urlc = Entry(width=30)
urlc.pack()
mainloop()
