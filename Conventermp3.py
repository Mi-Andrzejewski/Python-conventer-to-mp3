#!/usr/bin/env python3
import os
from moviepy import VideoFileClip
from tkinter import *
from tkinter import filedialog , messagebox

def choose_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Video files", "*.mp4 *.mkv *.avi *.webm"), ("All files", "*.*")]
    )
    if file_path:
        entry_var.set(file_path)


def choose_folder():
    folder_path = filedialog.askdirectory(title="Choose folder to save MP3")
    if folder_path:
        save_var.set(folder_path)


def convertmp3():
    input_p = entry_var.get()
    if not input_p:
        messagebox.showwarning("Lack of file","Lack of file, choose file first")
        return
    
    try:
        bitrate_value =str(int(bitrate_var.get()))+"k"
        
        output_p = os.path.join(save_var.get(), os.path.basename(os.path.splitext(input_p)[0] + ".mp3"))
        
        clip = VideoFileClip(input_p)
        clip.audio.write_audiofile(output_p, bitrate=bitrate_value)
        clip.close()
        messagebox.showinfo("Everything is fine",f"File saved as\n{output_p}")
    except Exception as error:
        messagebox.showerror("ERROR",f"\n{error}")

# TKINTER
root = Tk()
root.geometry("500x300")
root.title("Video -> mp.3")
root.resizable(False, False)
root.configure(background = "gray")

lable= Label(root,  text="Choose movie file: ",background = "gray",font=12).place(x=160,y=5)

entry_var = StringVar()
entry_p = Entry(root,textvariable= entry_var,width=50,state="readonly").place(x=40,y=40)

#choose your file
button= Button(root, text="Choose file",command=choose_file).place(x=350,y=38)
#button= Button(root, text="Choose file",width=9, command=choose_file).place(x=350,y=38) #for linux with KDE


#Saving lable
lable2= Label(root,  text="Choose path to save: ",background = "gray",font=12).place(x=160,y=80)

save_var = StringVar()
exit_p = Entry(root,textvariable = save_var,width=50,state="readonly").place(x=40,y=120)


button_folder = Button(root, text="Browse", command=choose_folder).place(x=350,y=118)
#button_folder = Button(root, text="Browse",width=9, command=choose_folder).place(x=350,y=118) #for linux with KDE


#Sound_quality

lable3= Label(root, text="kbps",background = "gray",font=12).place(x=350,y=180)

bitrate_var = IntVar(value=192)

Scale(root,variable=bitrate_var,from_=64,to=320,orient=HORIZONTAL,length=300,showvalue=True,tickinterval=64,resolution=64,background="gray").place(x=40,y=160)

#CONVERT
button_conv = Button(root,text="CONVERT",command=convertmp3).place(x=200,y=240)

root.mainloop()
