from tkinter import *
import pytube
import tkinter
from tkinter import messagebox
root = Tk()
root.title("Youtube video downloader")
root.geometry('800x150')
lbl = Label(root, text = "Enter youtube url: ") #label lbl.grid(column=0,row=0)
Youtube_url = Entry(root, width=60) # getting input from user
Youtube_url.grid(column =0, row =1) 
def download_video():
    try:
        url =Youtube_url.get() #get url from Youtube_url variable
        yt = pytube.YouTube(url)
        stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
        lb2 = Label(root, text = f"Downloading\n{yt.title}") #label
        lb2.grid(column=0, row=3)
        messagebox.askyesno("Do you want to download",f"Do you want to download{stream}")
        root.title("-------Downloading Video------")
        stream.download(output_path="C:/youtube_video")
        root.title("-------Downloaded Successfully------")
        messagebox.showinfo("--------Downloaded Successfully-------",f"--------Downloaded Successfully-------\n{yt.title}")
        root.title("Youtube video download")
        lb2 = Label(root, text = f"--------Downloaded Successfully-------\n{yt.title}\n\nPlease open=====>>> C:/youtube_video") #label
        lb2.grid(column=0, row=3)
    except:
        messagebox.showinfo("Error", "Incorrect URL OR Youtube not allow to download video")
btn = Button(root, text = "Download" ,fg = "red", command=download_video)#this button to callownload_video() function
btn.grid(column=0, row=2) #button location on window 
root.mainloop()


