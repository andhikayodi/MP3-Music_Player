#importing libraries 
import helpers
from pygame import mixer
import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image
from tkinter import filedialog

root=tk.Tk()
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

# #play button
play_button=tk.Button(root,text="Play",width =7, command=helpers.Play)
play_button['font']=defined_font
play_button.place(x=240,y=570)
# play_button.grid(row=1,column=0)

# #pause button 
# pause_button=tk.Button(history,text="Pause",width =7,command=helpers.Pause)
# pause_button['font']=defined_font
# pause_button.place(x=90,y=570)
# pause_button.grid(row=1,column=1)

# #stop button
# stop_button=tk.Button(root,text="Stop",width =7,command=mixer.Stop)
# stop_button['font']=defined_font
# stop_button.grid(row=1,column=2)

# #resume button
# Resume_button=tk.Button(root,text="Resume",width =7,command=mixer.Resume)
# Resume_button['font']=defined_font
# Resume_button.grid(row=1,column=3)

# #previous button
previous_button=tk.Button(root,text="Prev",width =7)
previous_button['font']=defined_font
previous_button.place(x=150,y=570)

# #nextbutton
next_button=tk.Button(root,text="Next",width =7)
next_button['font']=defined_font
next_button.place(x=330,y=570)

# #menu 
my_menu=tk.Menu(root)
root.config(menu=my_menu)
add_song_menu=tk.Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs")
add_song_menu.add_command(label="Delete song")
root.mainloop()