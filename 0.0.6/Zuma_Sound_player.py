from tkinter import *
#from PIL import ImageTk,Image
from tkinter import filedialog
import pygame
from tkinter import messagebox
pygame.mixer.init()
version = '0.0.6'

root = Tk()
root.title('Zuma Sound player v' + version)
root.iconbitmap('icon.ico')
root.geometry("730x450")
root.filename = ""


bg = PhotoImage(file="Original/Images/mainbg.png")

#my_canvas = Canvas(root, width=730, height=500)
#my_canvas.pack(fill="both", expand=True)

#my_canvas.create_image(0,0, image=bg, anchor="nw")

bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def change():
    stop()
    root.filename = filedialog.askopenfilename(initialdir ="Original/Music", title="Select an audio", filetypes=(("mp3 files", "*.mp3"),("OGG Vorbis file", "*.ogg"),("Microsoft WAV File", "*.wav"),("FLAC", "*.flac")))

def popup():
    response = messagebox.askyesno("Warning!", "You need to select an audio file to play. Do you want to select an audio?")
    if response == 1:
        root.filename = filedialog.askopenfilename(initialdir ="Original/Music", title="Select an audio", filetypes=(("mp3 files", "*.mp3"),("OGG Vorbis file", "*.ogg"),("Microsoft WAV File", "*.wav"),("FLAC", "*.flac")))
        if not root.filename == "":
            play()

def popup1():
    messagebox.showinfo("Warning!", "No audio is currently playing.")


def play():
    if not root.filename == "":
        pygame.mixer.music.load(root.filename)
        pygame.mixer.music.play(loops=0)
    else:
        popup()
        


def stop():
    pygame.mixer.music.stop()


    

play_button = Button(root, text="Play Audio", font=("Comic Sans MS", 32), command=play)
play_button.pack(pady=20)

stop_button = Button(root, text="Stop Audio", font=("Comic Sans MS", 32), command=stop)
stop_button.pack(pady=20)

change_button = Button(root, text="Change Audio", font=("Comic Sans MS", 32), command=change)
change_button.pack(pady=20)



root.mainloop()
