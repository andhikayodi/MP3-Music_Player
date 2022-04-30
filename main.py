#importing libraries 
import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image
from tkinter import filedialog
from pygame import mixer

def play():
    song=songs_list.get(tk.ACTIVE)
    song=song
    label = play_button["text"]
    if (label == "Play"):
        play_button.config(text="Pause")
        mixer.music.load(song)
        mixer.music.play()
    else: 
        play_button.config(text="Play")
        mixer.music.pause()

def add_song():
    temp_song= filedialog.askopenfilenames(title="Pilih lagu", filetypes=(("mp3 Files","*.mp3"),))
    for s in temp_song:
        songs_list.insert(tk.END,s)
    songs_list.selection_set( first = 0 )

def delete_song():
    curr_song=songs_list.curselection()
    print(curr_song)
    songs_list.delete(curr_song[0])

def previous():
    #to get the selected song index
    previous_one=songs_list.curselection()
    #to get the previous song index
    previous_one=previous_one[0]-1
    #to get the previous song
    temp2=songs_list.get(previous_one)
    temp2=temp2
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,tk.ACTIVE)
    #activate new song
    songs_list.activate(previous_one)
    #set the next song
    songs_list.selection_set(previous_one)


def next():
    #to get the selected song index
    next_one=songs_list.curselection()
    #to get the next song index
    next_one=next_one[0]+1
    #to get the next song 
    temp=songs_list.get(next_one)
    temp=temp
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0,tk.END)
    #activate newsong
    songs_list.activate(next_one)
     #set the next song
    songs_list.selection_set(next_one)


root=tk.Tk()
mixer.init()
# disable resize
root.resizable(0,0)
root.geometry("900x600")
root.title('MP3 Music player')

root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(0, weight = 1)

calc = tk.Frame(root, bg = "white")
calc.grid(row = 0, column = 0, sticky = "nesw")
history = tk.Frame(root, bg = "white")
history.grid(row = 0, column = 1, sticky = "nesw")


songs_list=tk.Listbox(history,selectmode=tk.SINGLE,bg="black",fg="white",font=('arial',15),height=31,width=50,selectbackground="green",selectforeground="black")
songs_list.place(x=0, y=1)

img = ImageTk.PhotoImage(Image.open("mp.png"))
label = tk.Label(calc, image = img, width=200,height=150)
label.pack()



defined_font = font.Font(family='Helvetica')

# play button
play_button=tk.Button(root,text="Play",width =7, command=play)
play_button['font']=defined_font
play_button.place(x=240,y=570)

# #previous button
previous_button=tk.Button(root,text="Prev",width =7, command=previous)
previous_button['font']=defined_font
previous_button.place(x=150,y=570)

# #nextbutton
next_button=tk.Button(root,text="Next",width =7, command=next)
next_button['font']=defined_font
next_button.place(x=330,y=570)

# #menu 
my_menu=tk.Menu(root)
root.config(menu=my_menu)
add_song_menu=tk.Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=add_song)
add_song_menu.add_command(label="Delete song", command=delete_song)
root.mainloop()