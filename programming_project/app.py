"""
#importujemy biblioteke tkinter
from tkinter import *
import tkinter.ttk as TTK
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import Menu
#definiujemy funkcje
def klikniety():
    rozwiniecie.configure(text="KLINELES!")

def klick():
    res = "Welcome to " + pole.get()
    rozwiniecie.configure(text=res)
    print(selected.get())

def numer():
    print(selected.get())
    #wyskakujace okkienko
    #messagebox.showinfo('Message title', 'Message content')
    #messagebox.showwarning('Message title', 'Message content')  # shows warning message
    messagebox.showerror('Message title', 'Message content') #shows error
    res = messagebox.askquestion('Message title', 'Message content')
    res = messagebox.askyesno('Message title', 'Message content')
    res = messagebox.askyesnocancel('Message title', 'Message content')
    res = messagebox.askokcancel('Message title', 'Message content')
    res = messagebox.askretrycancel('Message title', 'Message content')

def edit():
    res = messagebox.askretrycancel('Edycja', 'Probujemy edycji?')
#deklarujemy nasze okienko
window = Tk()

#ustawiamy wielkosc okna (w px)
window.geometry('1000x750')

#jaka bedzie wyswietlana nazwa okna
window.title("Easy to use database")

menu = Menu(window)
#menu.add_command(label='File') #albo dajemy jedno i jego funkcje albo menu kaskadowe

new_item = Menu(menu, tearoff=0) #tearoff - usuwamy brzydki dodatek
new_item.add_command(label="New")
new_item.add_separator()
new_item.add_command(label='Edit', command=edit)

#new_item = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)

#deklarujemy kolejne elementy ktore beda wyswietlane ne ekranie ==============
#napis
wstep = Label(window, text="Witaj")
rozwiniecie = Label(window, text="to bedzie bardzo latwe du uzycia")
#guzik
start = Button(window, text="START", bg="white", fg="red", font=("Arial Italic", 20), command=klick)
#pole do wpisania
pole = Entry(window, width=20)#, state='disabled')

#checkbutton
chk_state = BooleanVar()
chk_state.set(True)  # set check state
#mozna tez tak
chk_state = IntVar()
chk_state.set(0)  # uncheck

chk = Checkbutton(window, text='Choose', var=chk_state)

#radiobutton
selected = IntVar()
rad1 = Radiobutton(window, text='First', value=1, variable=selected)
rad2 = Radiobutton(window, text='Second', value=2, variable=selected, command=numer)

#przewijane okno tekstowe
txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.insert(INSERT, 'You text goes here')

#combo menu
combo = TTK.Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Text")
combo.current(1)  # set the selected item

#wybieranie cyferek
spin = Spinbox(window, from_=0, to=100, width=5)
spin2 = Spinbox(window, values=(10, 20, 50, 100, 200, 500, 1000), width=5)

#pasek postepu
style = TTK.Style() #definiujemy styl
style.theme_use('default')
style.configure("pink.Horizontal.TProgressbar", background='black')

bar = Progressbar(window, length=200, style="pink.Horizontal.TProgressbar")
bar['value'] = 25

#filedialog
#file = filedialog.askopenfilename()
#files = filedialog.askopenfilenames()
#file = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
dir = filedialog.askdirectory()

#ustawiamy pozycjonowanie w "kratce" =========================================
wstep.grid(column=0, row=0)
rozwiniecie.grid(column=0, row=1)
start.grid(column=0, row=2)
pole.grid(column=0, row=3)
combo.grid(column=0, row=4)
chk.grid(column=0, row=5)
rad1.grid(column=0, row=6)
rad2.grid(column=1, row=6)
txt.grid(column=0, row=7)
spin.grid(column=4, row=4)
spin2.grid(column=5, row=4)
bar.grid(column=4, row=0)
#wyswietlanie okna=============================================================
window.mainloop()
"""

'''
IMPORT
'''

from tkinter import *
import random
import tkinter.ttk as TTK
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import Menu
import math
import time
from datetime import datetime
from threading import Thread

'''
MAIN WINDOW
'''

#   WINDOW DECLARATION

game = Tk()

#   WINDOW CONFIGURATION

game.geometry('1000x800')
game.resizable(0, 0)

game.title("The Game")

game.configure(background="gray10", cursor="circle")

window_icon = PhotoImage(file="images/logo.png")
game.iconphoto(True, window_icon)

#   READY
def loading_screen():
    loading_screen_frame.place(x=0, y=0)

    raise_frame(loading_screen_frame)

    bar = Progressbar(loading_screen_frame, length=200, style="green.Horizontal.TProgressbar")
    bar['value'] = 0
    bar.place(relx=0.5, rely=0.7, anchor=CENTER)

    loading_screen_frame.update()

    waving_flag = Label(loading_screen_frame, image=flag1, bg=main_color)
    waving_flag.place(relx=0.5, rely=0.3, anchor=CENTER)

    time.sleep(0.5)

    for i in range(1, 101):
        bar['value'] = i
        if i % 9 == 2:
            waving_flag.config(image=flag1)
        if i % 9 == 5:
            waving_flag.config(image=flag2)
        if i % 9 == 8:
            waving_flag.config(image=flag3)
        time.sleep(0.07)
        loading_screen_frame.update()

    time.sleep(0.5)
    loading_screen_frame.place_forget()
    raise_frame(main_menu)

#   READY
def timer():
    raise_frame(countdown_frame)
    countdown_timer_text.update()
    time.sleep(1)
    '''
    x = 5
    for i in range(x, 0, -1):
        cache = str(i)
        countdown_timer.set(cache)
        countdown_timer_text.update()
        time.sleep(0.25)
        for j in range(3, 0, -1):
            cache += "."
            countdown_timer.set(cache)
            countdown_timer_text.update()
            time.sleep(0.25)

    countdown_timer.set("")
    countdown_timer_text.update()
    time.sleep(0.5)'''
    countdown_timer.set("Let's start THE GAME")
    countdown_timer_text.update()
    time.sleep(2)
    countdown_timer.set("")
    countdown_timer_text.update()

#   READY
def raise_frame(frame):
    frame.tkraise()


def display_all_the_info():
    intro.place(x=33, y=30)
    raise_frame(intro)

def start_game():
    user_input_function()
    timer()
    raise_frame(gameplay)

    display_all_the_info()

    get_starting_time(0)

def calculate_points():
    global time_start_tab
    global time_end_tab
    global current_score

    #   MINUTES
    cache_start = ""
    cache_end = ""

    for i in range(0, 2, 1):
        cache_start += str(time_start_tab[i])
        cache_end += str(time_end_tab[i])

    minutes = int(cache_end) - int(cache_start)

    #   SECONDS
    cache_start = ""
    cache_end = ""

    for i in range(3, 5, 1):
        cache_start += str(time_start_tab[i])
        cache_end += str(time_end_tab[i])

    seconds = int(cache_end) - int(cache_start)
    if seconds < 0:
        seconds = 60 - seconds*(-1)
        minutes -= 1
    else:
        pass

    #   MILISECONDS
    cache_start = ""
    cache_end = ""

    for i in range(6, 8, 1):
        cache_start += str(time_start_tab[i])
        cache_end += str(time_end_tab[i])

    miliseconds = int(cache_end) - int(cache_start)
    if miliseconds < 0:
        miliseconds = 60 - miliseconds * (-1)
        seconds -= 1
    else:
        pass

    euler = 2.718281828459
    pi = 3.141592653589
    golden_ratio = 1.618033988749

    if clues_amount == 0:
        current_score = abs(int(minutes * euler + seconds * 2 * pi + miliseconds * golden_ratio))
    else:
        current_score = abs(int(minutes * euler + seconds * 2 * pi + miliseconds * golden_ratio * clues_amount * 10))


def get_starting_time(start_0_or_end_1):
    if start_0_or_end_1 == 0:
        global time_start_tab
        time_start = str(datetime.now())
        print(time_start)
        for i in range(len(time_start)):
            if i >= 14:
                time_start_tab.append(time_start[i])

        print(time_start_tab)

    elif start_0_or_end_1 == 1:
        global time_end_tab
        time_end = str(datetime.now())
        print(time_end)
        for i in range(len(time_end)):
            if i >= 14:
                time_end_tab.append(time_end[i])

        print(time_end_tab)




#   READY
def add_new_score():
    global current_score
    global user_name
    all_scores_file = open("data_files/all_scores.txt", "a")
    all_scores_file.write("\n" + user_name + " " + str(current_score))
    all_scores_file.close()

#   READY
def extract_all_trails_from_file():
    trails_file = open("data_files/trails.txt")
    global trails_list
    trails_list.clear()
    for line in trails_file:
        trails_list.append(line.strip())
    print(trails_list)
    trails_file.close()

def random_murder():
    murder_file = open("data_files/suspects.txt")
    murder_list = []
    for line in murder_file:
        murder_list.append(line.strip())
    print(murder_list)
    x = random.randint(0, len(murder_list)-1)
    murder_pick.set(murder_list[x])
    print(murder_pick.get())

#   READY
def extract_all_highscores():
    all_scores_file = open("data_files/all_scores.txt")
    high_scores_list = []

    all_scores_list = []
    for line in all_scores_file:
        all_scores_list.append(line.strip().split())
    all_scores_file.close()
    print(all_scores_list)

    only_scores_list = []
    for l in range(0, len(all_scores_list)):
        only_scores_list.append(int(all_scores_list[l][1]))
    only_scores_list.sort()
    # only_scores_list.reverse() # u want to reverse that list if the more points u have is the better

    for m in range(0, 5, 1):
        for k in range(0, len(all_scores_list)):
            if int(all_scores_list[k][1]) == int(only_scores_list[m]):
                high_scores_list.append(all_scores_list[k])

    cache = ""
    for i in range(0, len(high_scores_list)):
        cache += str(i+1) + ". " + str(high_scores_list[i][0] + " " + str(high_scores_list[i][1]) + "\n")
    high_scores.set(cache)

def input_var_change():
    save_input_var.set(1)

def user_input_function():
    global user_name
    raise_frame(user_input_frame)
    user_input_button.wait_variable(save_input_var)
    user.set(user_input_entry.get())
    user_name = user.get()
    if user.get() == "":
        messagebox.showerror('Error', 'You have to enter your name!')
        user_input_function()
    else:
        pass

#   =================================================================
def actuall_game_program():
    print("ekd")

def pokaz():
    time.sleep(2)
    main_tiles.place(x=33, y=30)

def goto_highscores():
    extract_all_highscores()
    raise_frame(high_scores_frame)

def give_a_clue(place):
    if place == "Exhibition":
        print("costam")
        add_item_to_inv()
        # add_item_to_inv()
    elif place == "BigBen":
        add_item_to_inv()
    elif place == "Soldiers":
        add_item_to_inv()
    elif place == "Musicians":
        add_item_to_inv()
    elif place == "Party":
        add_item_to_inv()
    elif place == "Photoshoot":
        add_item_to_inv()
    elif place == "Street":
        add_item_to_inv()
    elif place == "Street #2":
        add_item_to_inv()
    elif place == "Tramway":
        add_item_to_inv()
    elif place == "Poor district":
        add_item_to_inv()

def remove_place(place):
    if place == "Exhibition":
        tile_1.place_forget()
    elif place == "BigBen":
        tile_2.place_forget()
    elif place == "Soldiers":
        tile_3.place_forget()
    elif place == "Musicians":
        tile_4.place_forget()
    elif place == "Party":
        tile_5.place_forget()
    elif place == "Photoshoot":
        tile_6.place_forget()
    elif place == "Street":
        tile_7.place_forget()
    elif place == "Street #2":
        tile_8.place_forget()
    elif place == "Tramway":
        tile_9.place_forget()
    elif place == "Poor district":
        tile_10.place_forget()

def place_details(place):
    print(place)

    place_description_frame = Frame(game, bg="gray20", width=700, height=600, padx=20, pady=20)
    place_description_frame.place(x=33, y=30)

    raise_frame(place_description_frame)

    place_description_image = Label(place_description_frame, width=640, height=560, image=london_map)
    place_description_image.place(relx=0.5, rely=0.5, anchor=CENTER)

    # place_description_text = Label(game_info, bg="gray23", fg="white", textvariable=place_description, font=("Arial Black", 14))
    # place_description_text.place(relx=0.3, rely=0.5, anchor=CENTER)

    place_description_look_for = Button(place_description_frame, bg="gray10", fg="white", text="Look for clues", font=("Arial Black", 14), command=lambda: [give_a_clue(place), place_description_look_for.place_forget(), remove_place(place)])
    place_description_look_for.place(relx=0.5, rely=0.9, anchor=CENTER)

    place_description_close = Button(place_description_frame, bg="gray10", fg="white", text="Close", font=("Arial Black", 14), command=lambda: [place_description_frame.place_forget(), place_description_text.place_forget()])
    place_description_close.place(relx=0.85, rely=0.9, anchor=CENTER)

    if place == "Exhibition":
        place_description_image.config(image=london_exhibition)
        place_description.set("O")
    elif place == "BigBen":
        place_description_image.config(image=london_main)
    elif place == "Soldiers":
        place_description_image.config(image=london_military)
    elif place == "Musicians":
        place_description_image.config(image=london_musicians)
    elif place == "Party":
        place_description_image.config(image=london_party)
    elif place == "Photoshoot":
        place_description_image.config(image=london_photographer)
    elif place == "Street":
        place_description_image.config(image=london_talk)
    elif place == "Street #2":
        place_description_image.config(image=london_talk2)
    elif place == "Tramway":
        place_description_image.config(image=london_tramway)
    elif place == "Poor district":
        place_description_image.config(image=london_poor)


def description(trail_name):
    print(trail_name)

    description_frame = Frame(game, bg="gray20", width=700, height=600, padx=20, pady=20)
    description_frame.place(x=33, y=30)

    raise_frame(description_frame)

    description_text = Label(description_frame, bg="gray20", fg="white", textvariable=item_description, font=("Arial Black", 14))
    description_text.place(relx=0.5, rely=0.5, anchor=CENTER)

    description_button = Button(description_frame, bg="gray10", fg="white", text="Close", font=("Arial Black", 14), command=lambda: description_frame.place_forget())
    description_button.place(relx=0.5, rely=0.9, anchor=CENTER)

    if murder_pick.get() == "Soldier":
        if trail_name == "Hammer":
            print(trail_name)
            item_description.set("Hmmm... \nI'd say that it belongs to a man but i could be stolen.")
        elif trail_name == "Knife":
            print(trail_name)
            item_description.set("This kind of a knife could be used be almost everyone.")
        elif trail_name == "Money":
            print(trail_name)
            item_description.set("Hmm... That seems not to be a british currency.")
        elif trail_name == "Cigarette":
            print(trail_name)
            item_description.set("Womens smoke rather rarely. I'm not sure if it's an important thing to jot down.")
        elif trail_name == "Notebook":
            print(trail_name)
            item_description.set("It has been signed by \"Mc Dickhead\"\nIt's to vulgar for a british gentelman...\nUnless he's deviant.")
        elif trail_name == "Watch":
            print(trail_name)
            item_description.set("That's an expensive watch.\nThere is no way that owner is poor...\nUnless the \"owner\" has stolen this item.\nWhat are the other possibilities? I have no idea")
        elif trail_name == "Hat":
            print(trail_name)
            item_description.set("That hat could be worn be almost everyone.\nI don't think it will help.")
        elif trail_name == "Syringe":
            print(trail_name)
            item_description.set("Who tf uses those? Probably a nurse or a junkie.\nIt's soo dirty I think that it's been used by a junkie.")
        elif trail_name == "ArmyKnife":
            print(trail_name)
            item_description.set("This kind of a knife could be used most probably be a soldier\n or by a person that travels a lot.\n"
                                 "Wait a minute! Is it blood on the blade?")
        elif trail_name == "Newspaper":
            print(trail_name)
            item_description.set("This is a normal London's newspaper... Nothing interesting here.")

    elif murder_pick.get() == "Nurse":
        if trail_name == "Hammer":
            print(trail_name)
            item_description.set("Hmmm... \nI'd say that it belongs to a man but i could be stolen.")
        elif trail_name == "Knife":
            print(trail_name)
            item_description.set("This kind of a knife could be used be almost everyone.")
        elif trail_name == "Money":
            print(trail_name)
            item_description.set("Hmm... That seems not to be a british currency.")
        elif trail_name == "Cigarette":
            print(trail_name)
            item_description.set("Womens smoke rather rarely. I'm not sure if it's an important thing to jot down.")
        elif trail_name == "Notebook":
            print(trail_name)
            item_description.set("It has been signed by \"Mc Dickhead\"\nIt's to vulgar for a british gentelman...\nUnless he's deviant.")
        elif trail_name == "Watch":
            print(trail_name)
            item_description.set("That's an expensive watch.\nThere is no way that owner is poor...\nUnless the \"owner\" has stolen this item.\nWhat are the other possibilities? I have no idea")
        elif trail_name == "Hat":
            print(trail_name)
            item_description.set("That hat could be worn be almost everyone.\nI don't think it will help.")
        elif trail_name == "Syringe":
            print(trail_name)
            item_description.set("Who tf uses those? Probably a nurse or a junkie.\nIt's soo dirty I think that it's been used by a junkie.")
        elif trail_name == "ArmyKnife":
            print(trail_name)
            item_description.set("This kind of a knife could be used most probably be a soldier\n or by a person that travels a lot.\n"
                                 "Wait a minute! Is it blood on the blade?")
        elif trail_name == "Newspaper":
            print(trail_name)
            item_description.set("This is a normal London's newspaper... Nothing interesting here.")

def add_item_to_inv():
    global free_slot
    global selected_trail
    global clues_amount

    if len(trails_list) > 0:
        clues_amount += 1

        x = random.randint(0, len(trails_list) - 1)
        # x = random.randint(0, 0)
        trail_name = (str(trails_list[x]))

        if trail_name == "Hammer":
            selected_trail = hammer
        elif trail_name == "Knife":
            selected_trail = knife
        elif trail_name == "Money":
            selected_trail = dollar
        elif trail_name == "Cigarette":
            selected_trail = cigarette
        elif trail_name == "Notebook":
            selected_trail = notebook
        elif trail_name == "Watch":
            selected_trail = watch
        elif trail_name == "Hat":
            selected_trail = hat
        elif trail_name == "Syringe":
            selected_trail = syringe
        elif trail_name == "ArmyKnife":
            selected_trail = army_knife
        elif trail_name == "Newspaper":
            selected_trail = newspaper

        trails_list.remove(trail_name)
        print(trails_list)

        if free_slot <= 10:
            if free_slot == 1:
                inv_slot_1.config(image=selected_trail, command=lambda: description(trail_name))
            elif free_slot == 2:
                inv_slot_2.config(image=selected_trail, command=lambda: description(trail_name))
            elif free_slot == 3:
                inv_slot_3.config(image=selected_trail, command=lambda: description(trail_name))
            elif free_slot == 4:
                inv_slot_4.config(image=selected_trail, command=lambda: description(trail_name))
            elif free_slot == 5:
                inv_slot_5.config(image=selected_trail, command=lambda: description(trail_name))
            elif free_slot == 6:
                inv_slot_6.config(image=selected_trail, command=lambda: description(trail_name))
            elif free_slot == 7:
                inv_slot_7.config(image=selected_trail, command=lambda: description(trail_name))
            elif free_slot == 8:
                inv_slot_8.config(image=selected_trail, command=lambda: description(trail_name))
            elif free_slot == 9:
                inv_slot_9.config(image=selected_trail, command=lambda: description(trail_name))
            elif free_slot == 10:
                inv_slot_10.config(image=selected_trail, command=lambda: description(trail_name))
            free_slot += 1

        elif free_slot > 10:
            print("Not enough space in inventory")

def x_is_negative():
    global x
    x = -1
    intro_function()

def intro_function():
    global x
    if x >= 0:
        text_1 = "You're in XIX'th century London. Your task is to find the murder.\nYou can find items that will help you to identify the murder.\nYour score is based on:\n" \
                 "- How long it takes you to identify the murder\n- How many items you will need.\nThe less the better your score is.\n\nAll items will be stored in the inventory next to the main display\n" \
                 "You can find the items (circumstantial evidence)\nat different places. \nYou have to know that once you take the item from that place\nyou will no longer have access to it"
        text_2 = "If you ever need help you can find it in the right bottom corner."
        text_3 = "Good Luck!"
        intro_ok_button.config(text="OK")
        intro_ok_button.place_forget()
        intro_nah_button.place_forget()
        intro_text2.place_forget()
        intro_ok_button.place(relx=0.5, rely=0.8, anchor=CENTER)
        if x == 0:
            text_intro.set(text_1)
        elif x == 1:
            text_intro.set(text_2)
        elif x == 2:
            text_intro.set(text_3)
            intro_ok_button.config(text="Thanks!")
        elif x > 2:
            intro.place_forget()
            main_tiles.place(x=33, y=30)
            place_description.set("What we know for now is that the murder is a man.\nHe killed in one of the places that we will visit today.")
        x += 1
    else:
        intro.place_forget()
        main_tiles.place(x=33, y=30)
        place_description.set("What we know for now is that the murder is a man.\nHe killed in one of the places that we will visit today.")

def placement_on_the_map():
    possible_x = []
    possible_y = []

    #   third argument controls distance between buttons of locations
    for m in range(10, 91, 6):
        possible_x.append(m/100)
    for n in range(30, 91, 6):
        possible_y.append(n/100)

    print(len(possible_x), len(possible_y))

    for i in range(1, 11):
        temp_x_id = random.randint(0, len(possible_x)-1)
        temp_y_id = random.randint(0, len(possible_y)-1)

        temp_x = possible_x[temp_x_id]
        temp_y = possible_y[temp_y_id]
        while True:
            if temp_x in possible_x:
                possible_x.remove(temp_x)
                break
            else:
                temp_x_id = random.randint(0, len(possible_x)-1)
                temp_x = possible_x[temp_x_id]

        while True:
            if temp_y in possible_y:
                possible_y.remove(temp_y)
                break
            else:
                temp_y_id = random.randint(0, len(possible_y)-1)
                temp_y = possible_y[temp_y_id]

        if i == 1:
            tile_1.place(relx=temp_x, rely=temp_y, anchor=CENTER)
        elif i == 2:
            tile_2.place(relx=temp_x, rely=temp_y, anchor=CENTER)
        elif i == 3:
            tile_3.place(relx=temp_x, rely=temp_y, anchor=CENTER)
        elif i == 4:
            tile_4.place(relx=temp_x, rely=temp_y, anchor=CENTER)
        elif i == 5:
            tile_5.place(relx=temp_x, rely=temp_y, anchor=CENTER)
        elif i == 6:
            tile_6.place(relx=temp_x, rely=temp_y, anchor=CENTER)
        elif i == 7:
            tile_7.place(relx=temp_x, rely=temp_y, anchor=CENTER)
        elif i == 8:
            tile_8.place(relx=temp_x, rely=temp_y, anchor=CENTER)
        elif i == 9:
            tile_9.place(relx=temp_x, rely=temp_y, anchor=CENTER)
        elif i == 10:
            tile_10.place(relx=temp_x, rely=temp_y, anchor=CENTER)
        else:
            pass


def ending():
    # final screen

    final_screen = Frame(game, bg="gray2", width=main_width, height=main_height)
    final_screen.place(x=0, y=0)

    close_app = Button(final_screen, bg="gray5", fg="red4", text="Close Game", font=("Arial Black", 20), command=lambda: game.destroy())
    close_app.place(relx=0.5, rely=0.8, anchor=CENTER)

    last_msg = StringVar()
    last_msg.set("")

    last_info = Label(final_screen, bg="gray2", fg="white", textvariable=last_msg, font=("Arial Black", 30))
    last_info.place(relx=0.5, rely=0.3, anchor=CENTER)



    final_screen.tkraise()
    get_starting_time(1)
    if answer.get() == murder_pick.get():
        print("You win")
        calculate_points()
        add_new_score()
        print(current_score)

        final_score = IntVar()
        final_score.set(current_score)

        last_msg.set("YOU WON!\nCongratulations!\n\nYour score is:")
        last_info_score = Label(final_screen, bg="gray2", fg="gray50", textvariable=final_score, font=("Arial Black", 30))
        last_info_score.place(relx=0.5, rely=0.6, anchor=CENTER)
    else:
        print("You lose")
        last_msg.set("YOU LOST\n\n:c")


'''
VARIABLE DECLARATION
'''

free_slot = 1
trails_list = []
main_height = 800
main_width = 1006
main_color = "gray2"
current_score = 0
user_name = "Player"
selected_trail = None
clues_amount = 0

user = StringVar()

save_input_var = IntVar()
save_input_var.set(0)

text_intro = StringVar()
item_description = StringVar()
place_description = StringVar()

answer = StringVar()
answer.set("None")

murder_pick = StringVar()


time_start_tab = []
time_end_tab = []

x = 0

'''
OTHER STUFF
'''


#   countdown

countdown_frame = Frame(game, bg=main_color, width=main_width, height=main_height)
countdown_frame.place(x=0, y=0)

countdown_timer = StringVar()

countdown_timer_text = Label(countdown_frame, bg=main_color, fg="white", textvariable=countdown_timer, font=("Arial Black", 50))
countdown_timer_text.place(relx=0.5, rely=0.5, anchor=CENTER)


#   user input

user_input_frame = Frame(game, bg=main_color, width=main_width, height=main_height)
user_input_frame.place(x=0, y=0)

user_input_text = Label(user_input_frame, bg=main_color, fg="white", text="Please enter your name", font=("Arial Black", 20))
user_input_text.place(relx=0.5, rely=0.4, anchor=CENTER)

user_input_entry = Entry(user_input_frame, bg="gray20", fg="white", bd=5, font=("Arial Black", 20))
user_input_entry.place(relx=0.5, rely=0.6, anchor=CENTER)

user_input_button = Button(user_input_frame, bg=main_color, fg="white", text="OK", font=("Arial Black", 20), command=input_var_change)
user_input_button.place(relx=0.5, rely=0.7, anchor=CENTER)

# guess

guessing = Frame(game, bg="gray2", width=main_width, height=main_height)
guessing.place(x=0, y=0)

guess_later = Button(guessing, bg="gray10", fg="white", text="Give me more time", font=("Arial Black", 15), command=lambda: guessing.place_forget())
guess_later.place(relx=0.5, rely=0.9, anchor=CENTER)

guess = Button(guessing, bg="gray10", fg="white", text="That's my answer", font=("Arial Black", 15), command=lambda: ending())
guess.place(relx=0.5, rely=0.8, anchor=CENTER)

suspects_title = Label(guessing, bg="gray2", fg="white", text="Suspects", font=("Arial Black", 30))
suspects_title.place(relx=0.5, rely=0.1, anchor=CENTER)

suspects_actual_pick = Label(guessing, bg="gray2", fg="white", text="Actual pick:", font=("Arial Black", 15))
suspects_actual_pick.place(relx=0.5, rely=0.55, anchor=CENTER)

suspects_actual_pick = Label(guessing, bg="gray2", fg="gray60", textvariable=answer, font=("Arial Black", 20))
suspects_actual_pick.place(relx=0.5, rely=0.6, anchor=CENTER)

suspect_1 = Button(guessing, bg="gray10", fg="white", text="Soldier", font=("Arial Black", 15), command=lambda: answer.set("Soldier"))
suspect_1.place(relx=0.2, rely=0.3, anchor=CENTER)

suspect_2 = Button(guessing, bg="gray10", fg="white", text="Nurse", font=("Arial Black", 15), command=lambda: answer.set("Nurse"))
suspect_2.place(relx=0.4, rely=0.3, anchor=CENTER)

suspect_3 = Button(guessing, bg="gray10", fg="white", text="American\nbusinessman", font=("Arial Black", 15), command=lambda: answer.set("American_businessman"))
suspect_3.place(relx=0.6, rely=0.3, anchor=CENTER)

suspect_4 = Button(guessing, bg="gray10", fg="white", text="Wealthy\nInvestor", font=("Arial Black", 15), command=lambda: answer.set("Wealthy_Investor"))
suspect_4.place(relx=0.8, rely=0.3, anchor=CENTER)

suspect_5 = Button(guessing, bg="gray10", fg="white", text="Photographer", font=("Arial Black", 15), command=lambda: answer.set("Photographer"))
suspect_5.place(relx=0.2, rely=0.4, anchor=CENTER)

suspect_6 = Button(guessing, bg="gray10", fg="white", text="Seller from\nthe street", font=("Arial Black", 15), command=lambda: answer.set("Seller_from_the_street"))
suspect_6.place(relx=0.4, rely=0.4, anchor=CENTER)

suspect_7 = Button(guessing, bg="gray10", fg="white", text="Motorman", font=("Arial Black", 15), command=lambda: answer.set("Motorman"))
suspect_7.place(relx=0.6, rely=0.4, anchor=CENTER)

suspect_8 = Button(guessing, bg="gray10", fg="white", text="Trumpeter", font=("Arial Black", 15), command=lambda: answer.set("Trumpeter"))
suspect_8.place(relx=0.8, rely=0.4, anchor=CENTER)

# help

help_frame = Frame(game, bg="gray2", width=main_width, height=main_height)
help_frame.place(x=0, y=0)

help_close = Button(help_frame, bg="gray10", fg="white", text="Close", font=("Arial Black", 15), command=lambda: help_frame.place_forget())
help_close.place(relx=0.5, rely=0.8, anchor=CENTER)

help_text = Label(help_frame, bg="gray2", fg="white", text="Sorry\nI can't help you :c", font=("Arial Black", 15))
help_text.place(relx=0.5, rely=0.4, anchor=CENTER)

'''
ALL THE ICONS
'''

#   TRAILS

empty_slot_icon = PhotoImage(file="images/empty_slot.png")

hammer = PhotoImage(file="images/hammer.png")
flag1 = PhotoImage(file="images/flag1.png")
flag2 = PhotoImage(file="images/flag2.png")
flag3 = PhotoImage(file="images/flag3.png")
dollar = PhotoImage(file="images/dollar.png")
cigarette = PhotoImage(file="images/cigarette.png")
notebook = PhotoImage(file="images/notebook.png")
watch = PhotoImage(file="images/watch.png")
hat = PhotoImage(file="images/hat.png")
syringe = PhotoImage(file="images/syringe.png")
knife = PhotoImage(file="images/knife.png")
army_knife = PhotoImage(file="images/army_knife.png")
newspaper = PhotoImage(file="images/news.png")

london_party = PhotoImage(file="images/london_party.png")
london_exhibition = PhotoImage(file="images/london_exhibition.png")
london_military = PhotoImage(file="images/london_military.png")
london_musicians = PhotoImage(file="images/london_musicians.png")
london_photographer = PhotoImage(file="images/london_photographer.png")
london_talk = PhotoImage(file="images/london_talk.png")
london_talk2 = PhotoImage(file="images/london_talk2.png")
london_main = PhotoImage(file="images/london_main.png")
london_map = PhotoImage(file="images/london_map.png")
london_tramway = PhotoImage(file="images/london_tramway.png")
london_poor = PhotoImage(file="images/london_poor.png")



'''
HIGH SCORES
'''

#   HIGH SCORES FRAME DECLARATION

high_scores_frame = Frame(game, bg=main_color, width=main_width, height=main_height)

#   HIGH SCORES FRAME PLACEMENT

high_scores_frame.place(x=0, y=0)

high_scores = StringVar()

back_flag_2 = Label(high_scores_frame, image=flag1, bg=main_color)
back_flag_2.place(relx=0.5, rely=0.2, anchor=CENTER)

high_scores_text2 = Label(high_scores_frame, bg=main_color, fg="white", text="The less points you have the better", font=("Arial Black", 15))
high_scores_text2.place(relx=0.5, rely=0.35, anchor=CENTER)

high_scores_text = Label(high_scores_frame, bg=main_color, fg="white", textvariable=high_scores, font=("Arial Black", 15))
high_scores_text.place(relx=0.5, rely=0.55, anchor=CENTER)


back_to_main_menu_button_3 = Button(high_scores_frame, text="BACK TO\nMAIN MENU", bg="gray5", fg="red4", font=("Arial Black", 10), command=lambda: raise_frame(main_menu))
back_to_main_menu_button_3.place(relx=0.5, rely=0.8, anchor=CENTER)


'''
ABOUT GAME FRAME
'''

#   ABOUT GAME DECLARATION

about_game = Frame(game, bg=main_color, width=main_width, height=main_height)

#   ABOUT GAME PLACEMENT

about_game.place(x=0, y=0)

back_flag_1 = Label(about_game, image=flag1, bg=main_color)
back_flag_1.place(relx=0.5, rely=0.2, anchor=CENTER)

author_description = StringVar()
author_description.set("Wykonał Paweł Sieńkowski\nGrupa 2\nGame is all about finding the person who has murdered...\nYou will find few items and footprints.\nGood Luck!")

about_game_text = Label(about_game, bg=main_color, fg="white", textvariable=author_description, font=("Arial Black", 15))
about_game_text.place(relx=0.5, rely=0.5, anchor=CENTER)

back_to_main_menu_button_1 = Button(about_game, text="BACK TO\nMAIN MENU", bg="gray5", fg="red4", font=("Arial Black", 10), command=lambda: raise_frame(main_menu))
back_to_main_menu_button_1.place(relx=0.5, rely=0.8, anchor=CENTER)


'''
GAMEPLAY FRAME
'''

gameplay = Frame(game, bg="gray2", width=main_width, height=main_height)

gameplay.place(x=0, y=0)


'''
INTRO
'''

intro = Frame(game, bg="gray10", width=700, height=584, padx=20, pady=20)

# intro.place(x=33, y=30)


intro_text = Label(intro, bg="gray10", fg="white", textvariable=text_intro, font=("Arial Black", 14))
intro_text.place(relx=0.5, rely=0.4, anchor=CENTER)

intro_text2 = Label(intro, bg="gray10", fg="white", text="Are you familiar with this game?\nNeed help?", font=("Arial Black", 14))
intro_text2.place(relx=0.5, rely=0.4, anchor=CENTER)

intro_ok_button = Button(intro, bg="gray20", fg="white", text="Show me around", font=("Arial Black", 14), command=intro_function)
intro_ok_button.place(relx=0.3, rely=0.8, anchor=CENTER)

intro_nah_button = Button(intro, bg="gray20", fg="white", text="No thanks", font=("Arial Black", 14), command=x_is_negative)
intro_nah_button.place(relx=0.7, rely=0.8, anchor=CENTER)


'''
GAME INFO
pasek na dole ekranu czyli game info // dostep do opcji // dopstep do podpowiedzi
'''

#   GAME INFO DECLARATION

game_info = Frame(gameplay, bg="gray23", width=main_width-66, height=120)

#   GAME INFO PLACEMENT

game_info.place(x=33, y=655)

back_to_main_menu_button_2 = Button(game_info, text="Quit", fg="red4", bg="gray70", font=("Arial Black", 11), command=lambda: game.destroy())
back_to_main_menu_button_2.place(relx=0.94, rely=0.5, anchor=CENTER)

take_a_guess = Button(game_info, text="Take a guess", fg="white", bg="gray20", font=("Arial Black", 12), command=lambda: [guessing.place(x=0, y=0), guessing.tkraise()])
take_a_guess.place(relx=0.8, rely=0.7, anchor=CENTER)

need_help = Button(game_info, text="Need help", fg="white", bg="gray20", font=("Arial Black", 11), command=lambda: [help_frame.place(x=0, y=0), help_frame.tkraise()])
need_help.place(relx=0.8, rely=0.3, anchor=CENTER)


place_description_text = Label(game_info, bg="gray23", fg="white", textvariable=place_description, font=("Arial Black", 14))
place_description_text.place(relx=0.3, rely=0.5, anchor=CENTER)

'''
TILES
'''

#   TILES FRAME DECLARATION

main_tiles = Frame(gameplay, bg="gray10", width=700, height=600, padx=10, pady=10)
main_tiles.place(x=33, y=30)

main_tiles_background = Label(main_tiles, width=640, height=560, image=london_map)
main_tiles_background.place(relx=0.5, rely=0.5, anchor=CENTER)


#   TILES

tile_1 = Button(main_tiles, bg="gray15", fg="white", text="Exhibition", font=("Arial Black", 10), command=lambda: place_details("Exhibition"))
tile_2 = Button(main_tiles, bg="gray15", fg="white", text="BigBen", font=("Arial Black", 10), command=lambda: place_details("BigBen"))
tile_3 = Button(main_tiles, bg="gray15", fg="white", text="Soldiers", font=("Arial Black", 10), command=lambda: place_details("Soldiers"))
tile_4 = Button(main_tiles, bg="gray15", fg="white", text="Musicians", font=("Arial Black", 10), command=lambda: place_details("Musicians"))
tile_5 = Button(main_tiles, bg="gray15", fg="white", text="Party", font=("Arial Black", 10), command=lambda: place_details("Party"))
tile_6 = Button(main_tiles, bg="gray15", fg="white", text="Photoshoot", font=("Arial Black", 10), command=lambda: place_details("Photoshoot"))
tile_7 = Button(main_tiles, bg="gray15", fg="white", text="Street", font=("Arial Black", 10), command=lambda: place_details("Street"))
tile_8 = Button(main_tiles, bg="gray15", fg="white", text="Street #2", font=("Arial Black", 10), command=lambda: place_details("Street #2"))
tile_9 = Button(main_tiles, bg="gray15", fg="white", text="Tramway", font=("Arial Black", 10), command=lambda: place_details("Tramway"))
tile_10 = Button(main_tiles, bg="gray15", fg="white", text="Poor district", font=("Arial Black", 10), command=lambda: place_details("Poor district"))


#   TILES PLACEMENT


'''
INVENTORY
'''

#   INVENTORY NAME

inv_name = Label(gameplay, bg="white", fg="gray30", text="Inventory", font=("Arial Black", 17))
inv_name.place(x=760, y=30, width=210)


#   INVENTORY FRAME

inventory = Frame(gameplay, bg="gray25", width=200, height=550)
# inventory.place(x=766, y=100)
inventory.place(x=760, y=100)


#   INVENTORY SLOTS CONFIGURATION

inv_slot_width = 100
inv_slot_height = 100

inv_slot_color = "white"


#   INVENTORY SLOTS

inv_slot_1 = Button(inventory, bg=inv_slot_color, image=empty_slot_icon, width=inv_slot_width, height=inv_slot_height)
inv_slot_2 = Button(inventory, bg=inv_slot_color, image=empty_slot_icon, width=inv_slot_width, height=inv_slot_height)


inv_slot_3 = Button(inventory, bg=inv_slot_color, image=empty_slot_icon, width=inv_slot_width, height=inv_slot_height)
inv_slot_4 = Button(inventory, bg=inv_slot_color, image=empty_slot_icon, width=inv_slot_width, height=inv_slot_height)


inv_slot_5 = Button(inventory, bg=inv_slot_color, image=empty_slot_icon, width=inv_slot_width, height=inv_slot_height)
inv_slot_6 = Button(inventory, bg=inv_slot_color, image=empty_slot_icon, width=inv_slot_width, height=inv_slot_height)


inv_slot_7 = Button(inventory, bg=inv_slot_color, image=empty_slot_icon, width=inv_slot_width, height=inv_slot_height)
inv_slot_8 = Button(inventory, bg=inv_slot_color, image=empty_slot_icon, width=inv_slot_width, height=inv_slot_height)


inv_slot_9 = Button(inventory, bg=inv_slot_color, image=empty_slot_icon, width=inv_slot_width, height=inv_slot_height)
inv_slot_10 = Button(inventory, bg=inv_slot_color, image=empty_slot_icon, width=inv_slot_width, height=inv_slot_height)


#   INVENTORY SLOTS PLACEMENT

inv_slot_1.grid(column=1, row=1, sticky="nsew")
inv_slot_2.grid(column=2, row=1, sticky="news")

inv_slot_3.grid(column=1, row=2)
inv_slot_4.grid(column=2, row=2)

inv_slot_5.grid(column=1, row=3)
inv_slot_6.grid(column=2, row=3)

inv_slot_7.grid(column=1, row=4)
inv_slot_8.grid(column=2, row=4)

inv_slot_9.grid(column=1, row=5)
inv_slot_10.grid(column=2, row=5)


'''
MAIN MENU FRAME
'''

#   MAIN MENU FRAME DECLARATION

main_menu = Frame(game, bg=main_color, width=main_width, height=main_height)

main_menu.place(x=0, y=0)

#   MAIN MENU NAME

title = Label(main_menu, bg=main_color, fg="white", text="Murder in London", font=("Helvetica BOLD", 60, "bold italic"))
"""IMPORTANT NOTE - adding width and height to label slows it down and causes stutters"""
title.place(relx=0.5, rely=0.2, anchor=CENTER)

#   MENU BUTTONS FRAME

main_menu_buttons = Frame(main_menu, bg="gray10", width=main_width, height=main_height)

main_menu_buttons.place(relx=0.5, rely=0.6, anchor=CENTER)

#   FRAME BUTTONS

start_game_button = Button(main_menu_buttons, text="Start The Game", bg="gray5", fg="white", font=("Arial Black", 20), command=lambda: start_game())

start_game_button.grid(column=1, row=1, sticky="news")


about_game_button = Button(main_menu_buttons, text="About The Game", bg="gray5", fg="white", font=("Arial Black", 15), command=lambda: raise_frame(about_game))

about_game_button.grid(column=1, row=2, sticky="news")


high_scores_button = Button(main_menu_buttons, text="High Scores", bg="gray5", fg="white", font=("Arial Black", 15), command=lambda: goto_highscores())

high_scores_button.grid(column=1, row=3, sticky="news")


quit_game = Button(main_menu_buttons, text="Quit The Game", bg="gray5", fg="red4", font=("Arial Black", 20), command=game.destroy)

quit_game.grid(column=1, row=5, sticky="news")


'''
LOADING SCREEN
'''

loading_screen_frame = Frame(game, bg=main_color, width=main_width, height=main_height, cursor="watch")

# loading_screen_frame.place(x=0, y=0)


'''
MAIN CODE
'''

extract_all_trails_from_file()
extract_all_highscores()
placement_on_the_map()
random_murder()
loading_screen()
# raise_frame(main_menu)


game.mainloop()