
# all imports
import time
from tkinter import *
from pygame import mixer
import threading as thre



# background music
mixer.init()
mixer.music.load("Minecraft.mp3")
mixer.music.play()

# function music
def main_music():
  mixer.init()
  mixer.music.load("Minecraft.mp3")
  mixer.music.play()

# function on click
def click():
    mixer.init()
    mixer.music.load("click.mp3")
    mixer.music.play()
    print("creating world.../joining server...")
    time.sleep(0.1)
    main_music()

# on click exit
def exit_window():
    
    exit()


# window definition
play_calm_music = thre.Thread(target=main_music)
play_calm_music.start()
window = Tk()
window.geometry("420x420")
window.title('MINECRAFT("scuffed edition")')
icon = PhotoImage(file="minecraft_dirt.png")
dirt_image = PhotoImage(file="minecraft_dirt_smaller.png")
window.iconphoto(True,icon)
window.config(background="#277bd6")







# main top mainecraft label
minecraft_lable = Label(


    window,
    text="MINECRAFT",
    background="#277bd6",
    foreground="#a3ada3",
    font=("Arial",50,"bold"),
    bd=10,    
    padx=10,
    pady=10,
    bg="#277bd6",
    compound="top"


)
minecraft_lable.pack()






   

# create_new_world_button
create_new_world_button = Button(
    
    window,
    text="create new world",
    padx=100,
    bg="#a9b0ba",
    command=click,
    font=("Arial",10,"bold",),
    overrelief=RAISED,
    activebackground="#a9b0ba"

               )
create_new_world_button.pack()






# join_server_button
join_server_button = Button(
    window,
    text="    join a server    ",
    padx=100,
    bg="#a9b0ba",
    command=click,
    font=("Arial",10,"bold",),
    relief=RAISED,
    activebackground="#a9b0ba"
)
join_server_button.pack()





# exit_button
exit_button = Button(
    
    
    window,
    text="           EXIT          ",
    bg="#a9b0ba",
    command=exit_window,
    font=("Arial",10,"bold"),
    padx=100,
    relief=RAISED,
    

)
exit_button.pack()






window.mainloop()