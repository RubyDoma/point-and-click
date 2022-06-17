

from tkinter import *
from tkinter.tix import *
from turtle import back
import winsound

from pkg_resources import safe_extra

# sound = winsound.PlaySound("main.wav", winsound.SND_ASYNC + winsound.SND_LOOP)  


window = Tk()
window.geometry("900x800")
window.configure(bg='black') 
window.state('zoomed')
window.title('ESCAPE THE ROOM!')
tip= Balloon(window)


img = PhotoImage(file='images/mainroom.png')
Label(window,image=img).pack()



intro1 = Label(text = """You are locked
in this room!
Find the door key 
and escape!
Good luck!

BONUS:
FIND THE 
EASTER EGG!

""")
intro1.place(x =1300, y = 30)
intro1["bg"] = "black"
intro1["fg"] = "white"
intro1["font"] = "helvetica, 14"


objects = []


def OpenDrawer1():
    drawer1_text = Label(text = "This drawer is empty")
    window.after(1000, lambda: drawer1_text.destroy())
    drawer1_text.place(x =650, y = 650)
    drawer1_text["bg"] = "black"
    drawer1_text["fg"] = "white"
    drawer1_text["font"] = "helvetica, 14"
          
def OpenBigDrawer1():
    if "document" in objects: 
        already_done = Label(text = "This drawer is now empty")
        window.after(1000, lambda: already_done.destroy())
        already_done.place(x =610, y = 650)
        already_done["bg"] = "black"
        already_done["fg"] = "white"
        already_done["font"] = "helvetica, 14"
    else:
        if "key" in objects:
            winsound.PlaySound("sounds/pickobject.wav", winsound.SND_ASYNC) 
            doc_text = Label(text = "You found a piece of paper")
            window.after(2000, lambda: doc_text.destroy())
            objects.append("document")
            doc_img = PhotoImage(file='images/pieceofpaper.png')
            doc_btn = Button(image=doc_img, bd=0,cursor="circle",command=ViewPic)
            doc_btn.image = doc_img # keep a reference!
            doc_btn.pack()
            doc_btn.place(x=130, y=120,width=50,height=50)
            tip.bind_widget(doc_btn,balloonmsg="View piece of paper")
            doc_text.place(x =610, y = 650)
            doc_text["bg"] = "black"
            doc_text["fg"] = "white"
            doc_text["font"] = "helvetica, 14"
            
        else:
            winsound.PlaySound("sounds/door.wav", winsound.SND_ASYNC)
            big_drawer1_text = Label(text = "This drawer is locked")
            window.after(1000, lambda: big_drawer1_text.destroy())
            big_drawer1_text.place(x =610, y = 650)
            big_drawer1_text["bg"] = "black"
            big_drawer1_text["fg"] = "white"
            big_drawer1_text["font"] = "helvetica, 14"

def ViewPic():
    if "ink" in objects:
        winsound.PlaySound("sounds/paper2.wav", winsound.SND_ASYNC) 
        objects.append("doc_clue")
        pic_img = PhotoImage(file='images/raven.png')
        pic_btn = Button(image=pic_img, bd=0,cursor="circle")
        pic_btn.image = pic_img # keep a reference!
        pic_btn.pack()
        pic_btn.place(x =510, y = 610,width=300,height=300)
        open_img = PhotoImage(file='images/x.png')
        dismiss_btn_commands = lambda: [dismiss_btn.destroy(),pic_btn.destroy()]
        dismiss_btn = Button(image=open_img, bd=0,cursor="circle",command=dismiss_btn_commands)
        dismiss_btn.image = open_img # keep a reference!
        dismiss_btn.pack(pady=20)
        dismiss_btn.place(x =820, y = 620,width=50,height=50)
    else:
        winsound.PlaySound("sounds/paper2.wav", winsound.SND_ASYNC) 
        cannot_read_img = PhotoImage(file='images/paperpiece.png')
        cannot_read_btn = Button(image=cannot_read_img, bd=0,cursor="circle")
        cannot_read_btn.image = cannot_read_img # keep a reference!
        cannot_read_btn.pack()
        cannot_read_btn.place(x =600, y = 610,width=230,height=220)

        cannot_read_text = Label(text = "The paper is blank...")
        cannot_read_text.place(x =630, y = 830)
        cannot_read_text["bg"] = "black"
        cannot_read_text["fg"] = "white"
        cannot_read_text["font"] = "helvetica, 14"

        dismiss_img = PhotoImage(file='images/x.png')
        dismiss_btn_commands = lambda: [dismiss_btn.destroy(),cannot_read_btn.destroy(),cannot_read_text.destroy()]
        dismiss_btn = Button(image=dismiss_img, bd=0,cursor="circle",command=dismiss_btn_commands)
        dismiss_btn.image = dismiss_img # keep a reference!
        dismiss_btn.pack(pady=20)
        dismiss_btn.place(x =910, y = 620,width=50,height=50)
        
def OpenDrawer2():
    if "key" in objects: 
        already_done = Label(text = "This drawer is now empty")
        window.after(1000, lambda: already_done.destroy())
        already_done.place(x =610, y = 650)
        already_done["bg"] = "black"
        already_done["fg"] = "white"
        already_done["font"] = "helvetica, 14"
    else:
        winsound.PlaySound("sounds/pickobject.wav", winsound.SND_ASYNC) 
        drawer2_text = Label(text = "You found a key!")
        window.after(2000, lambda: drawer2_text.destroy())
        objects.append("key")
        key_img = PhotoImage(file='images/key.png')
        key_btn = Button(image=key_img, bd=0,cursor="circle")
        key_btn.image = key_img # keep a reference!
        key_btn.pack(side=LEFT)
        key_btn.place(x=50, y=50)
        tip.bind_widget(key_btn,balloonmsg="Key")
        drawer2_text.place(x =610, y = 650)
        drawer2_text["bg"] = "black"
        drawer2_text["fg"] = "white"
        drawer2_text["font"] = "helvetica, 14"
       
def OpenBigDrawer2():
    if "scissors" in objects:
        already_done = Label(text = "This drawer is now empty")
        window.after(1000, lambda: already_done.destroy())
        already_done.place(x =610, y = 650)
        already_done["bg"] = "black"
        already_done["fg"] = "white"
        already_done["font"] = "helvetica, 14"
    else:
        winsound.PlaySound("sounds/pickobject.wav", winsound.SND_ASYNC) 
        big_drawer2_text = Label(text = "You found scissors")
        window.after(1000, lambda: big_drawer2_text.destroy())
        big_drawer2_text.place(x =650, y = 650)
        big_drawer2_text["bg"] = "black"
        big_drawer2_text["fg"] = "white"
        big_drawer2_text["font"] = "helvetica, 14"
        window.after(2000, lambda: big_drawer2_text.destroy())
        objects.append("scissors")
        scissors_img = PhotoImage(file='images/scissors.png')
        scissors_btn = Button(image=scissors_img, bd=0,cursor="circle")
        scissors_btn.image = scissors_img # keep a reference!
        scissors_btn.pack(side=LEFT)
        scissors_btn.place(x=50, y=190,width=50,height=50)
        tip.bind_widget(scissors_btn,balloonmsg="Scissors")

def OpenBox():
    if "ink" in objects: 
        already_done = Label(text = "The box is now empty")
        window.after(1000, lambda: already_done.destroy())
        already_done.place(x =610, y = 650)
        already_done["bg"] = "black"
        already_done["fg"] = "white"
        already_done["font"] = "helvetica, 14"
    else:
        winsound.PlaySound("sounds/pickobject.wav", winsound.SND_ASYNC)
        drawer2_text = Label(text = "You found invisible ink")
        window.after(2000, lambda: drawer2_text.destroy())
        ink_img = PhotoImage(file='images/ink.png')
        ink_btn = Button(image=ink_img, bd=0,cursor="circle", width=50, height=50)
        ink_btn.image = ink_img # keep a reference!
        ink_btn.pack()
        ink_btn.place(x=130, y=50)
        tip.bind_widget(ink_btn,balloonmsg="Invisible ink")
        objects.append("ink")
        drawer2_text.place(x =610, y = 650)
        drawer2_text["bg"] = "black"
        drawer2_text["fg"] = "white"
        drawer2_text["font"] = "helvetica, 14"
    
def OpenSmallBox():
    if "lens" in objects: 
        already_done = Label(text = "The box is now empty")
        window.after(1000, lambda: already_done.destroy())
        already_done.place(x =610, y = 650)
        already_done["bg"] = "black"
        already_done["fg"] = "white"
        already_done["font"] = "helvetica, 14"
    else:
        if "scissors" in objects:
            winsound.PlaySound("sounds/pickobject.wav", winsound.SND_ASYNC)
            lens_text = Label(text = "You found a magnifying lens")
            window.after(2000, lambda: lens_text.destroy())
            lens_img = PhotoImage(file='images/lens.png')
            lens_btn = Button(image=lens_img, bd=0,cursor="circle", width=50, height=50)
            lens_btn.image = lens_img # keep a reference!
            lens_btn.pack()
            lens_btn.place(x=50, y=260,width=50,height=50)
            tip.bind_widget(lens_btn,balloonmsg="Magnifying lens")
            objects.append("lens")
            lens_text.place(x =610, y = 650)
            lens_text["bg"] = "black"
            lens_text["fg"] = "white"
            lens_text["font"] = "helvetica, 14"
        else:
            cannot_open = Label(text = "The box is sealed")
            window.after(1000, lambda: cannot_open.destroy())
            cannot_open.place(x =610, y = 650)
            cannot_open["bg"] = "black"
            cannot_open["fg"] = "white"
            cannot_open["font"] = "helvetica, 14"

def InspectPainting1():
    winsound.PlaySound("sounds/painting1.wav", winsound.SND_ASYNC) 
    objects.append("painting_clue")
    painting_img = PhotoImage(file='images/puppyreal.png')
    painting_btn = Button(image=painting_img, bd=0,cursor="circle")
    painting_btn.image = painting_img # keep a reference!
    painting_btn.pack()
    painting_btn.place(x =590, y = 600,width=300,height=200)
    open_img = PhotoImage(file='images/x.png')
    dismiss_btn_commands = lambda: [dismiss_btn.destroy(),painting_btn.destroy()]
    dismiss_btn = Button(image=open_img, bd=0,cursor="circle",command=dismiss_btn_commands)
    dismiss_btn.image = open_img # keep a reference!
    dismiss_btn.pack(pady=20)
    dismiss_btn.place(x =910, y = 620,width=50,height=50)
   
def InspectPainting2():
    winsound.PlaySound("sounds/painting1.wav", winsound.SND_ASYNC) 
    objects.append("painting2_clue")
    painting2_img = PhotoImage(file='images/liverpool.png')
    painting2_btn = Button(image=painting2_img, bd=0,cursor="circle")
    painting2_btn.image = painting2_img # keep a reference!
    painting2_btn.pack()
    painting2_btn.place(x=610, y=600,width=190,height=150)
    open_img = PhotoImage(file='images/x.png')
    dismiss_btn_commands = lambda: [dismiss_btn.destroy(),painting2_btn.destroy()]
    dismiss_btn = Button(image=open_img, bd=0,cursor="circle",command=dismiss_btn_commands)
    dismiss_btn.image = open_img # keep a reference!
    dismiss_btn.pack(pady=20)
    dismiss_btn.place(x =910, y = 620,width=50,height=50) 

def InspectPainting3():
    winsound.PlaySound("sounds/painting1.wav", winsound.SND_ASYNC) 
    objects.append("painting3_clue")
    painting3_img = PhotoImage(file='images/soldier.png')
    painting3_btn = Button(image=painting3_img, bd=0,cursor="circle")
    painting3_btn.image = painting3_img # keep a reference!
    painting3_btn.pack()
    painting3_btn.place(x =610, y = 600,width=150,height=340)
    open_img = PhotoImage(file='images/x.png')
    dismiss_btn_commands = lambda: [dismiss_btn.destroy(),painting3_btn.destroy()]
    dismiss_btn = Button(image=open_img, bd=0,cursor="circle",command=dismiss_btn_commands)
    dismiss_btn.image = open_img # keep a reference!
    dismiss_btn.pack(pady=20)
    dismiss_btn.place(x =910, y = 620,width=50,height=50)

def InspectPainting4():
    winsound.PlaySound("sounds/painting1.wav", winsound.SND_ASYNC) 
    objects.append("painting4_clue")
    painting4_img = PhotoImage(file='images/kpmg.png')
    painting4_btn = Button(image=painting4_img, bd=0,cursor="circle")
    painting4_btn.image = painting4_img # keep a reference!
    painting4_btn.pack()
    painting4_btn.place(x =610, y = 610,width=200,height=160)
    open_img = PhotoImage(file='images/x.png')
    dismiss_btn_commands = lambda: [dismiss_btn.destroy(),painting4_btn.destroy()]
    dismiss_btn = Button(image=open_img, bd=0,cursor="circle",command=dismiss_btn_commands)
    dismiss_btn.image = open_img # keep a reference!
    dismiss_btn.pack(pady=20)
    dismiss_btn.place(x =910, y = 620,width=50,height=50)

def InspectCalendar():
    winsound.PlaySound("sounds/paper.wav", winsound.SND_ASYNC) 
    objects.append("calendar_clue")
    calendar_img = PhotoImage(file='images/day.png')
    calendar_btn = Button(image=calendar_img, bd=0,cursor="circle")
    calendar_btn.image = calendar_img # keep a reference!
    calendar_btn.pack()
    calendar_btn.place(x=130, y=120,width=200,height=160)
    window.after(3000, lambda: calendar_btn.destroy())
    calendar_btn.place(x =610, y = 650)
    
def ViewPlant():
    winsound.PlaySound("sounds/paper.wav", winsound.SND_ASYNC) 
    objects.append("plant_clue")
    pant_img = PhotoImage(file='images/december.png')
    pant_btn = Button(image=pant_img, bd=0,cursor="circle")
    pant_btn.image = pant_img # keep a reference!
    pant_btn.pack()
    pant_btn.place(x =630, y = 620,width=200,height=80)
    window.after(3000, lambda: pant_btn.destroy())
   
def TurnLightOn():
    winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)  
    light = Label(text = "The light doesn't work")
    window.after(1000, lambda: light.destroy())
    light.place(x =610, y = 650)
    light["bg"] = "black"
    light["fg"] = "white"
    light["font"] = "helvetica, 14"

def ViewFan():
    winsound.PlaySound("sounds/fan.wav", winsound.SND_ASYNC)  
    light = Label(text = "Refreshing...")
    window.after(1000, lambda: light.destroy())
    light.place(x =620, y = 650)
    light["bg"] = "black"
    light["fg"] = "white"
    light["font"] = "helvetica, 14"

def ViewWindow():
    winsound.PlaySound("sounds/knock.wav", winsound.SND_ASYNC)  
    windowimg = Label(text = "I really want to go out :( ...")
    window.after(3000, lambda: windowimg.destroy())
    windowimg.place(x =610, y = 650)
    windowimg["bg"] = "black"
    windowimg["fg"] = "white"
    windowimg["font"] = "helvetica, 14"

def InspectBooks1():
    winsound.PlaySound("sounds/paper2.wav", winsound.SND_ASYNC) 
    objects.append("book_clue")
    book_img = PhotoImage(file='images/book.png')
    book_btn = Button(image=book_img, bd=0,cursor="circle")
    book_btn.image = book_img # keep a reference!
    book_btn.pack()
    book_btn.place(x =610, y = 590,width=260,height=350)
    open_img = PhotoImage(file='images/x.png')
    dismiss_btn_commands = lambda: [dismiss_btn.destroy(),book_btn.destroy()]
    dismiss_btn = Button(image=open_img, bd=0,cursor="circle",command=dismiss_btn_commands)
    dismiss_btn.image = open_img # keep a reference!
    dismiss_btn.pack(pady=20)
    dismiss_btn.place(x =910, y = 620,width=50,height=50)

def OpenBook():
    winsound.PlaySound("sounds/paper2.wav", winsound.SND_ASYNC) 
    objects.append("bigbook_clue")
    book_img = PhotoImage(file='images/javascript.png')
    book_btn = Button(image=book_img, bd=0,cursor="circle")
    book_btn.image = book_img # keep a reference!
    book_btn.pack()
    book_btn.place(x =610, y = 590,width=210,height=260)
    open_img = PhotoImage(file='images/x.png')
    dismiss_btn_commands = lambda: [dismiss_btn.destroy(),book_btn.destroy()]
    dismiss_btn = Button(image=open_img, bd=0,cursor="circle",command=dismiss_btn_commands)
    dismiss_btn.image = open_img # keep a reference!
    dismiss_btn.pack(pady=20)
    dismiss_btn.place(x =910, y = 620,width=50,height=50)

def ViewMessage():
    if "lens" in objects:
        winsound.PlaySound("sounds/paper2.wav", winsound.SND_ASYNC) 
        objects.append("message_clue")
        messagepic_img = PhotoImage(file='images/magnifiedmessage.png')
        messagepic_btn = Button(image=messagepic_img, bd=0,cursor="circle")
        messagepic_btn.image = messagepic_img # keep a reference!
        messagepic_btn.pack()
        messagepic_btn.place(x =540, y = 610,width=300,height=300)

        dismiss_img = PhotoImage(file='images/x.png')
        dismiss_btn_commands = lambda: [dismiss_btn.destroy(),messagepic_btn.destroy()]
        dismiss_btn = Button(image=dismiss_img, bd=0,cursor="circle",command=dismiss_btn_commands)
        dismiss_btn.image = dismiss_img # keep a reference!
        dismiss_btn.pack(pady=20)
        dismiss_btn.place(x =930, y = 620,width=50,height=50)
    
    else:
        winsound.PlaySound("sounds/paper2.wav", winsound.SND_ASYNC) 
        small_writing_img = PhotoImage(file='images/smallwriting.png')
        small_writing_btn = Button(image=small_writing_img, bd=0,cursor="circle")
        small_writing_btn.image = small_writing_img # keep a reference!
        small_writing_btn.pack()
        small_writing_btn.place(x =500, y = 610,width=400,height=260)

        small_writing_text = Label(text = "The writing is too small...")
        small_writing_text.place(x =610, y = 900)
        small_writing_text["bg"] = "black"
        small_writing_text["fg"] = "white"
        small_writing_text["font"] = "helvetica, 14"


        dismiss_img = PhotoImage(file='images/x.png')
        dismiss_btn_commands = lambda: [dismiss_btn.destroy(),small_writing_btn.destroy(),small_writing_text.destroy()]
        dismiss_btn = Button(image=dismiss_img, bd=0,cursor="circle",command=dismiss_btn_commands)
        dismiss_btn.image = dismiss_img # keep a reference!
        dismiss_btn.pack(pady=20)
        dismiss_btn.place(x =910, y = 620,width=50,height=50)

def InspectBooks2():
    winsound.PlaySound("sounds/paper2.wav", winsound.SND_ASYNC) 
    if "message" in objects: 
        already_done = Label(text = "There is nothing else to see here")
        window.after(1000, lambda: already_done.destroy())
        already_done.place(x =610, y = 650)
        already_done["bg"] = "black"
        already_done["fg"] = "white"
        already_done["font"] = "helvetica, 14"
    else:
        winsound.PlaySound("sounds/pickobject.wav", winsound.SND_ASYNC) 
        books2_text = Label(text = "You found a message...")
        window.after(1000, lambda: books2_text.destroy())
        objects.append("message")
        message_img = PhotoImage(file='images/message.png')
        message_btn = Button(image=message_img, bd=0,cursor="circle",command=ViewMessage)
        message_btn.image = message_img # keep a reference!
        message_btn.pack()
        message_btn.place(x=50, y=120,width=50,height=50)
        tip.bind_widget(message_btn,balloonmsg="Read message")
        books2_text.place(x =610, y = 650)
        books2_text["bg"] = "black"
        books2_text["fg"] = "white"
        books2_text["font"] = "helvetica, 14"
        objects.append("combination")

def ShowMagazine():
    winsound.PlaySound("sounds/paper.wav", winsound.SND_ASYNC) 
    objects.append("newspaper_clue")
    magazine_img = PhotoImage(file='images/tina.png')
    magazine_btn = Button(image=magazine_img, bd=0,cursor="circle")
    magazine_btn.image = magazine_img # keep a reference!
    magazine_btn.pack()
    magazine_btn.place(x =600, y = 600,width=230,height=250)
    open_img = PhotoImage(file='images/x.png')
    dismiss_btn_commands = lambda: [dismiss_btn.destroy(),magazine_btn.destroy()]
    dismiss_btn = Button(image=open_img, bd=0,cursor="circle",command=dismiss_btn_commands)
    dismiss_btn.image = open_img # keep a reference!
    dismiss_btn.pack(pady=20)
    dismiss_btn.place(x =910, y = 620,width=50,height=50)

def InspectBin():
    winsound.PlaySound("sounds/paper2.wav", winsound.SND_ASYNC) 
    if "newspaper" in objects: 
        already_done = Label(text = "There is nothing else to see here")
        window.after(1000, lambda: already_done.destroy())
        already_done.place(x =610, y = 650)
        already_done["bg"] = "black"
        already_done["fg"] = "white"
        already_done["font"] = "helvetica, 14"
    else:
        pass
        winsound.PlaySound("sounds/pickobject.wav", winsound.SND_ASYNC) 
        newspaper_text = Label(text = "There is a magazine in the bin")
        window.after(1000, lambda: newspaper_text.destroy())
        newspaper_img_small = PhotoImage(file='images/news-small.png')
        newspaper_btn = Button(image=newspaper_img_small, bd=0,cursor="circle", command=ShowMagazine)
        newspaper_btn.image = newspaper_img_small # keep a reference!
        newspaper_btn.pack()
        newspaper_btn.place(x=130, y=190,width=50,height=50)
        tip.bind_widget(newspaper_btn,balloonmsg="View newspaper")
        newspaper_text.place(x =610, y = 650)
        newspaper_text["bg"] = "black"
        newspaper_text["fg"] = "white"
        newspaper_text["font"] = "helvetica, 14"
        objects.append("newspaper")

def ShowEasterEgg():
    easter_egg_img = PhotoImage(file='images/easteregg.png')
    easter_egg_btn = Button(image=easter_egg_img, bd=0,cursor="circle")
    easter_egg_btn.image = easter_egg_img # keep a reference!
    easter_egg_btn.pack()
    easter_egg_btn.place(x =1322, y = 250,width=120,height=130)
  
def AskCupboardombination():
    
    global cupboard_correct_answer
    global insert_cupboard
    global check_cupboard_answer 
    
    cupboard_correct_answer = "christmas"

    if "easteregg" in objects: 
        already_done = Label(text = "There is nothing else here")
        window.after(1000, lambda: already_done.destroy())
        already_done.place(x =610, y = 650)
        already_done["bg"] = "black"
        already_done["fg"] = "white"
        already_done["font"] = "helvetica, 14"
    else:
        enter_cupboard_answer = Label(text = "Enter password")
        enter_cupboard_answer.place(x =645, y = 650)
        enter_cupboard_answer["bg"] = "black"
        enter_cupboard_answer["fg"] = "white"
        enter_cupboard_answer["font"] = "helvetica, 14"


        check_cupboard_answer = Label(text = "check")
        check_cupboard_answer.place(x =690, y = 800)
        check_cupboard_answer["bg"] = "black"
        check_cupboard_answer["fg"] = "white"
        check_cupboard_answer["font"] = "helvetica, 14"


        insert_cupboard = Entry(textvariable="")
        insert_cupboard.pack()
        insert_cupboard.place(x =620, y = 700, width = 200, height = 25)
        insert_cupboard["justify"] = "center"
        insert_cupboard.focus()
        cupboard_combination_inserted = insert_cupboard.get()
        str(cupboard_combination_inserted)
        
        open_cupboard_img = PhotoImage(file='images/cupboardlock.png')
        open_btn_commands = lambda: [open_cupboard_btn.destroy(), enter_cupboard_answer.destroy(), Check_if_Cupbopard_Combination_Is_Correct()]
        open_cupboard_btn = Button(image=open_cupboard_img, bd=0,cursor="circle",command=open_btn_commands)
        open_cupboard_btn.image = open_cupboard_img # keep a reference!
        open_cupboard_btn.pack(pady=20)
        open_cupboard_btn.place(x =690, y = 750,width=50,height=50)
        
def Check_if_Cupbopard_Combination_Is_Correct():
    global cupboard_correct_answer
    global insert_cupboard
    global check_cupboard_answer 
    cupboard_correct_answer = cupboard_correct_answer.lower()

    cupboard_combination_inserted = insert_cupboard.get()
    str(insert_cupboard)

    
    if cupboard_combination_inserted == cupboard_correct_answer:
        OpenCupbpard()
        insert_cupboard.destroy()
        check_cupboard_answer.destroy()
    else:
        winsound.PlaySound("sounds/door.wav", winsound.SND_ASYNC)
        wrong_combination = Label(text = "The combination is wrong")
        window.after(1000, lambda: wrong_combination.destroy())
        wrong_combination.place(x =610, y = 650)
        wrong_combination["bg"] = "black"
        wrong_combination["fg"] = "white"
        wrong_combination["font"] = "helvetica, 14"
        insert_cupboard.destroy()
        check_cupboard_answer.destroy()

def OpenCupbpard():
    winsound.PlaySound("sounds/bling.wav", winsound.SND_ASYNC)
    easter_egg_text = Label(text = "YOU FOUND THE EASTER EGG!")
    easter_egg_text.place(x =560, y = 810)
    easter_egg_text["bg"] = "black"
    easter_egg_text["fg"] = "white"
    easter_egg_text["font"] = "helvetica, 14"
    objects.append("easteregg")

    easter_egg_img = PhotoImage(file='images/easteregg.png')
    easter_egg_btn = Button(image=easter_egg_img, bd=0,cursor="circle")
    easter_egg_btn.image = easter_egg_img # keep a reference!
    easter_egg_btn.pack()
    easter_egg_btn.place(x =650, y = 600,width=120,height=130)

    dismiss_img = PhotoImage(file='images/x.png')
    dismiss_btn_commands = lambda: [dismiss_btn.destroy(),easter_egg_btn.destroy(),easter_egg_text.destroy(),ShowEasterEgg()]
    dismiss_btn = Button(image=dismiss_img, bd=0,cursor="circle",command=dismiss_btn_commands)
    dismiss_btn.image = dismiss_img # keep a reference!
    dismiss_btn.pack(pady=20)
    dismiss_btn.place(x =910, y = 620,width=50,height=50)
        
def OpenSafe():

    if "doorkey" in objects: 
        already_done = Label(text = "There is nothing else in the safe")
        window.after(1000, lambda: already_done.destroy())
        already_done.place(x =610, y = 650)
        already_done["bg"] = "black"
        already_done["fg"] = "white"
        already_done["font"] = "helvetica, 14"
    else:
        winsound.PlaySound("sounds/bling.wav", winsound.SND_ASYNC)
        safe_text = Label(text = """Correct! 

        You found the door key!""")
        window.after(2000, lambda: safe_text.destroy())
        objects.append("key")
        doorkey_img = PhotoImage(file='images/doorkey.png')
        doorkey_btn = Button(image=doorkey_img, bd=0, width=50, height=50,cursor="circle")
        doorkey_btn.image = doorkey_img # keep a reference!
        doorkey_btn.pack()
        doorkey_btn.place(x=130, y=260,width=50,height=50)
        tip.bind_widget(doorkey_btn,balloonmsg="Door key")
        safe_text.place(x=580, y = 650)
        safe_text["bg"] = "black"
        safe_text["fg"] = "white"
        safe_text["font"] = "helvetica, 14"
        objects.append("doorkey")

def AskCombination():
   
    if "doorkey" in objects:
        already_done = Label(text = "There is nothing else here")
        window.after(1000, lambda: already_done.destroy())
        already_done.place(x =610, y = 650)
        already_done["bg"] = "black"
        already_done["fg"] = "white"
        already_done["font"] = "helvetica, 14"
    else:
        global correct_answer
        global insert
        global check    
        
        correct_answer = ["Lindsey is the best", "Lindsey Raven is the best"]

        enter_combination = Label(text = "Enter combination")
        enter_combination.place(x =645, y = 650)
        enter_combination["bg"] = "black"
        enter_combination["fg"] = "white"
        enter_combination["font"] = "helvetica, 14"

        check = Label(text = "check")
        check.place(x =698, y = 800)
        check["bg"] = "black"
        check["fg"] = "white"
        check["font"] = "helvetica, 14"

        insert = Entry(textvariable="")
        insert.pack()
        insert.place(x =620, y = 700, width = 200, height = 25)
        insert["justify"] = "center"
        insert.focus()
        combination_inserted = insert.get()
        str(combination_inserted)
        
        open_img = PhotoImage(file='images/lock.png')
        open_btn_commands = lambda: [open_btn.destroy(), enter_combination.destroy(),Check_if_Combination_Is_Correct()]
        open_btn = Button(image=open_img, bd=0,cursor="circle",command=open_btn_commands)
        open_btn.image = open_img # keep a reference!
        open_btn.pack(pady=20)
        open_btn.place(x =700, y = 750,width=50,height=50)
        

def Check_if_Combination_Is_Correct():
    
    global correct_answer
    global insert
    global check

    combination_inserted = insert.get()
    str(insert)

    
    if combination_inserted in correct_answer:
        OpenSafe()
        insert.destroy()
        check.destroy()
    
    else:
        winsound.PlaySound("sounds/door.wav", winsound.SND_ASYNC)
        wrong_combination = Label(text = "The combination is wrong")
        window.after(1000, lambda: wrong_combination.destroy())
        wrong_combination.place(x =610, y = 650)
        wrong_combination["bg"] = "black"
        wrong_combination["fg"] = "white"
        wrong_combination["font"] = "helvetica, 14"
        insert.destroy()
        check.destroy()
    
    
def Out():
    winsound.PlaySound("sounds/out.wav", winsound.SND_ASYNC) 
    out_img = PhotoImage(file='images/out.png')
    out_btn = Button(image=out_img, bd=0,cursor="circle")
    out_btn.image = out_img # keep a reference!
    out_btn.pack()
    out_btn.place(x =235, y = 0)
    intro1.destroy()

    you_win_text = Label(text = "Congratulations, you managed to escape the room!")
    you_win_text.place(x =500, y = 650)
    you_win_text["bg"] = "black"
    you_win_text["fg"] = "white"
    you_win_text["font"] = "helvetica, 14"

    enjoy_text = Label(text = "We hope you enjoyed the game!")
    enjoy_text.place(x =570, y = 750)
    enjoy_text["bg"] = "black"
    enjoy_text["fg"] = "white"
    enjoy_text["font"] = "helvetica, 14"

    if "easteregg" in objects:
        outro1 = Label(text = """
        Well done
        on finding 
        the Easter Egg!
        """)
        outro1.place(x =1270, y = 30)
        outro1["bg"] = "black"
        outro1["fg"] = "white"
        outro1["font"] = "helvetica, 14"
    else:
        outro2 = Label(text = """
        You didn't find
        the Easter Egg :(
        """)
        outro2.place(x =1270, y = 30)
        outro2["bg"] = "black"
        outro2["fg"] = "white"
        outro2["font"] = "helvetica, 14"

def OpenDoor():
    global intro1
    if "doorkey" not in objects: 
        winsound.PlaySound("sounds/door.wav", winsound.SND_ASYNC)
        door_text = Label(text = "It's locked")
        window.after(1000, lambda: door_text.destroy())
        door_text.place(x =650, y = 650)
        door_text["bg"] = "black"
        door_text["fg"] = "white"
        door_text["font"] = "helvetica, 14"
    else:
        winsound.PlaySound("sounds/dooropen.wav", winsound.SND_ASYNC) 
        open_door_txt = Label(text = "Go out!")
        open_door_txt.place(x =630, y = 650)
        open_door_txt["bg"] = "black"
        open_door_txt["fg"] = "white"
        open_door_txt["font"] = "helvetica, 14"
        doorhandle_img = PhotoImage(file='images/doorhandle.png')
        doorhandle_btn_commands = lambda: [doorhandle_btn.destroy(), open_door_txt.destroy(), stay_txt.destroy(),stay_btn.destroy(),Out()]
        doorhandle_btn = Button(image=doorhandle_img, bd=0,cursor="circle", command=doorhandle_btn_commands)
        doorhandle_btn.image = doorhandle_img # keep a reference!
        doorhandle_btn.pack(pady=20)
        doorhandle_btn.place(x =640, y = 600,width=50,height=50)

        stay_txt = Label(text = "Stay in")
        stay_txt.place(x =710, y = 650)
        stay_txt["bg"] = "black"
        stay_txt["fg"] = "white"
        stay_txt["font"] = "helvetica, 14"

        stay_img = PhotoImage(file='images/stay.png')
        stay_btn_commands = lambda: [doorhandle_btn.destroy(), open_door_txt.destroy(),stay_txt.destroy(),stay_btn.destroy()]
        stay_btn = Button(image=stay_img, bd=0,cursor="circle", command=stay_btn_commands)
        stay_btn.image = stay_img # keep a reference!
        stay_btn.pack(pady=20)
        stay_btn.place(x =720, y = 600,width=50,height=50)
        

                                            ########## BUTTONS #########


drawer1_img = PhotoImage(file='images/drawer1.png')
drawer1 = Button(command = OpenDrawer1,image=drawer1_img, highlightthickness = 0, bd = 0,cursor="circle")
tip.bind_widget(drawer1,balloonmsg="Open drawer")
drawer1.place(x=690, y=290)

drawer2_img = PhotoImage(file='images/drawer2.png')
drawer2 = Button(command = OpenDrawer2,image=drawer2_img, highlightthickness = 0, bd = 0,cursor="circle")
tip.bind_widget(drawer2,balloonmsg="Open drawer")
drawer2.place(x=690, y=310)

big_drawer1_img = PhotoImage(file='images/bigdrawer1.png')
big_drawer1 = Button(command = OpenBigDrawer1,image=big_drawer1_img, highlightthickness = 0, bd = 0,cursor="circle")
tip.bind_widget(big_drawer1,balloonmsg="Open drawer")
big_drawer1.place(x=608, y=250)

big_drawer2_img = PhotoImage(file='images/bigdrawer2.png')
big_drawer2 = Button(command = OpenBigDrawer2,image=big_drawer2_img, highlightthickness = 0, bd = 0, cursor="circle")
tip.bind_widget(big_drawer2,balloonmsg="Open drawer")
big_drawer2.place(x=587, y=290)

painting_img = PhotoImage(file='images/painting_img.png')
painting = Button(command = InspectPainting1, image=painting_img,highlightthickness = 0, bd = 0, cursor="circle")
tip.bind_widget(painting,balloonmsg="View painting")
painting.place(x=440, y=80)

painting2_img = PhotoImage(file='images/painting2.png')
painting2 = Button(command = InspectPainting2, image=painting2_img,highlightthickness = 0, bd = 0, cursor="circle")
tip.bind_widget(painting2,balloonmsg="View painting")
painting2.place(x=412, y=183)

painting3_img = PhotoImage(file='images/painting3.png')
painting3 = Button(command = InspectPainting3, image=painting3_img,highlightthickness = 0, bd = 0, cursor="circle")
tip.bind_widget(painting3,balloonmsg="View painting")
painting3.place(x=488, y=169)

painting4_img = PhotoImage(file='images/painting4.png')
painting4 = Button(command = InspectPainting4, image=painting4_img,highlightthickness = 0, bd = 0, cursor="circle")
tip.bind_widget(painting4,balloonmsg="View painting")
painting4.place(x=453, y=232)

books1_img = PhotoImage(file='images/books1.png')
books1 = Button(command = InspectBooks1, image=books1_img,highlightthickness = 0, bd = 0, cursor="circle")
tip.bind_widget(books1,balloonmsg="Inspect books")
books1.place(x=622, y=162)

books2_img = PhotoImage(file='images/books2.png')
books2 = Button(command = InspectBooks2, image=books2_img,highlightthickness = 0, bd = 0, cursor="circle")
tip.bind_widget(books2,balloonmsg="Inspect books")
books2.place(x=622, y=206)

door_img = PhotoImage(file='images/doorlock.png')
door = Button(command = OpenDoor,image=door_img, highlightthickness = 0, bd = 0, cursor="circle")
tip.bind_widget(door,balloonmsg="Open door")
door.place(x=994, y=280)

safe_img = PhotoImage(file='images/safe.png')
safe = Button(command = AskCombination,image=safe_img, highlightthickness = 0, bd = 0,relief=RIDGE,cursor="circle")
tip.bind_widget(safe,balloonmsg="Open safe")
safe.place(x=861, y=330)

calendar_img = PhotoImage(file='images/calendar.png')
calendar = Button(command = InspectCalendar,image=calendar_img, highlightthickness = 0, bd = 0,relief=RIDGE,cursor="circle")
tip.bind_widget(calendar,balloonmsg="Inspect calendar")
calendar.place(x=793, y=176)

fan_img = PhotoImage(file='images/fan.png')
fan = Button(command = ViewFan,image=fan_img, highlightthickness = 0, bd = 0,relief=RIDGE,cursor="circle")
tip.bind_widget(fan,balloonmsg="View fan")
fan.place(x=850, y=116)

light_img = PhotoImage(file='images/light.png')
light = Button(command = TurnLightOn,image=light_img, highlightthickness = 0, bd = 0,relief=RIDGE,cursor="circle")
tip.bind_widget(light,balloonmsg="Turn light on")
light.place(x=725, y=208)

window_img = PhotoImage(file='images/window.png')
window = Button(command = ViewWindow,image=window_img, highlightthickness = 0, bd = 0,relief=RIDGE,cursor="circle")
tip.bind_widget(window,balloonmsg="View window")
window.place(x=308, y=140)

box_img = PhotoImage(file='images/box.png')
box = Button(command = OpenBox,image=box_img, highlightthickness = 0, bd = 0, cursor="circle")
tip.bind_widget(box,balloonmsg="Inspect box")
box.place(x=694, y=380)

small_box_img = PhotoImage(file='images/small-box.png')
small_box = Button(command = OpenSmallBox,image=small_box_img, highlightthickness = 0, bd = 0, cursor="circle")
tip.bind_widget(small_box,balloonmsg="Inspect box")
small_box.place(x=592, y=445.5)

bin_img = PhotoImage(file='images/bin.png')
bin = Button(command = InspectBin,image=bin_img, highlightthickness = 0, bd = 0, cursor="circle")
tip.bind_widget(bin,balloonmsg="Inspect bin")
bin.place(x=802, y=315)

cupboard_img = PhotoImage(file='images/cupboard.png')
cupboard = Button(command = AskCupboardombination,image=cupboard_img, highlightthickness = 0, bd = 0, cursor="circle")
tip.bind_widget(cupboard,balloonmsg="Inspect cupboard")
cupboard.place(x=1120, y=295)

plant_img = PhotoImage(file='images/plant.png')
plant = Button(command = ViewPlant,image=plant_img, highlightthickness = 0, bd = 0, cursor="circle")
tip.bind_widget(plant,balloonmsg="Inspect plant")
plant.place(x=1170, y=350)

big_book_img = PhotoImage(file='images/bigbook.png')
big_book = Button(command = OpenBook,image=big_book_img, highlightthickness = 0, bd = 0, cursor="circle")
tip.bind_widget(big_book,balloonmsg="Inspect book")
big_book.place(x=1133, y=378)

window.mainloop()