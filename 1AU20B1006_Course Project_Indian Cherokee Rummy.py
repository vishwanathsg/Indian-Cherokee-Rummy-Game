from tkinter import *
import pygame
from PIL import ImageTk, Image
from tkinter import messagebox
from random import shuffle
root = Tk()
root.title("The Indian Cherokee Rummy game")
root.geometry("1024x763")


pygame.mixer.init()
def play():
    pygame.mixer.music.load("Nostalgia.mp3")
    pygame.mixer.music.play(loops=0)
    return

#Define background image
startwindow_bg = PhotoImage(file="startwindow_ff.png")
gamewindow_bg = PhotoImage(file="game_window.png")

#Define background image
#gamewindow_bg = PhotoImage(file="game_window.png")

#Define card button image
card_button = PhotoImage(file="card_background_small.png")

#Defining cards in images
AC = Image.open("AC.png")
resize = AC.resize((100, 140), Image.ANTIALIAS)
AC = ImageTk.PhotoImage(resize)
#AC = (PhotoImage(file="AC.png"),1)
AD = Image.open("AD.png")
resize = AD.resize((100, 140), Image.ANTIALIAS)
AD = ImageTk.PhotoImage(resize)
#AD = (PhotoImage(file="AD.png"),1)
AH = Image.open("AH.png")
resize = AH.resize((100, 140), Image.ANTIALIAS)
AH = ImageTk.PhotoImage(resize)
#AH = (PhotoImage(file="AH.png"),1)
AS = Image.open("AS.png")
resize = AS.resize((100, 140), Image.ANTIALIAS)
AS = ImageTk.PhotoImage(resize)
#AS = (PhotoImage(file="AS.png"),1)



TWC = Image.open("2C.png")
resize = TWC.resize((100, 140), Image.ANTIALIAS)
TWC = ImageTk.PhotoImage(resize)
#TWC = (PhotoImage(file="2C.png"),2)
TWD = Image.open("2D.png")
resize = TWD.resize((100, 140), Image.ANTIALIAS)
TWD = ImageTk.PhotoImage(resize)
#TWD = (PhotoImage(file="2D.png"),2)
TWH = Image.open("2H.png")
resize = TWH.resize((100, 140), Image.ANTIALIAS)
TWH = ImageTk.PhotoImage(resize)
#TWH = (PhotoImage(file="2H.png"),2)
TWS = Image.open("2S.png")
resize = TWS.resize((100, 140), Image.ANTIALIAS)
TWS = ImageTk.PhotoImage(resize)
#TWS = (PhotoImage(file="2S.png"),2)



THC = Image.open("3C.png")
resize = THC.resize((100, 140), Image.ANTIALIAS)
THC = ImageTk.PhotoImage(resize)
#THC = (PhotoImage(file="3C.png"), 3)
THD = Image.open("3D.png")
resize = THD.resize((100, 140), Image.ANTIALIAS)
THD = ImageTk.PhotoImage(resize)
#THD = (PhotoImage(file="3D.png"), 3)
THH = Image.open("3H.png")
resize = THH.resize((100, 140), Image.ANTIALIAS)
THH = ImageTk.PhotoImage(resize)
#THH = (PhotoImage(file="3H.png"), 3)
THS = Image.open("3S.png")
resize = THS.resize((100, 140), Image.ANTIALIAS)
THS = ImageTk.PhotoImage(resize)
#THS = (PhotoImage(file="3S.png"), 3)



FOC = Image.open("4C.png")
resize = FOC.resize((100, 140), Image.ANTIALIAS)
FOC = ImageTk.PhotoImage(resize)
#FOC = (PhotoImage(file="4C.png"), 4)
FOD = Image.open("4D.png")
resize = FOD.resize((100, 140), Image.ANTIALIAS)
FOD = ImageTk.PhotoImage(resize)
#FOD = (PhotoImage(file="4D.png"))# 4)
FOH = Image.open("4H.png")
resize = FOH.resize((100, 140), Image.ANTIALIAS)
FOH = ImageTk.PhotoImage(resize)
#FOH = (PhotoImage(file="4H.png"))# 4)
FOS = Image.open("4S.png")
resize = FOS.resize((100, 140), Image.ANTIALIAS)
FOS = ImageTk.PhotoImage(resize)
#FOS = (PhotoImage(file="4S.png"))# 4)



FIC = Image.open("5C.png")
resize = FIC.resize((100, 140), Image.ANTIALIAS)
FIC = ImageTk.PhotoImage(resize)
#FIC = (PhotoImage(file="5C.png"))# 5)
FID = Image.open("5D.png")
resize = FID.resize((100, 140), Image.ANTIALIAS)
FID = ImageTk.PhotoImage(resize)
#FID = (PhotoImage(file="5D.png"))# 5)
FIH = Image.open("5H.png")
resize = FIH.resize((100, 140), Image.ANTIALIAS)
FIH = ImageTk.PhotoImage(resize)
#FIH = (PhotoImage(file="5H.png"))# 5)
FIS = Image.open("5S.png")
resize = FIS.resize((100, 140), Image.ANTIALIAS)
FIS = ImageTk.PhotoImage(resize)
#FIS = (PhotoImage(file="5S.png"))# 5)



SIC = Image.open("6C.png")
resize = SIC.resize((100, 140), Image.ANTIALIAS)
SIC = ImageTk.PhotoImage(resize)
#SIC = (PhotoImage(file="6C.png"))# 6)
SID = Image.open("6D.png")
resize = SID.resize((100, 140), Image.ANTIALIAS)
SID = ImageTk.PhotoImage(resize)
#SID = (PhotoImage(file="6D.png"))# 6)
SIH = Image.open("6H.png")
resize = SIH.resize((100, 140), Image.ANTIALIAS)
SIH = ImageTk.PhotoImage(resize)
#SIH = (PhotoImage(file="6H.png"))# 6)
SIS = Image.open("6S.png")
resize = SIS.resize((100, 140), Image.ANTIALIAS)
SIS = ImageTk.PhotoImage(resize)
#SIS = (PhotoImage(file="6S.png"))#6)



SEC = Image.open("7C.png")
resize = SEC.resize((100, 140), Image.ANTIALIAS)
SEC = ImageTk.PhotoImage(resize)
#SEC = (PhotoImage(file="7C.png"))# 7)
SED = Image.open("7D.png")
resize = SED.resize((100, 140), Image.ANTIALIAS)
SED = ImageTk.PhotoImage(resize)
#SED = (PhotoImage(file="7D.png"))# 7)
SEH = Image.open("7H.png")
resize = SEH.resize((100, 140), Image.ANTIALIAS)
SEH = ImageTk.PhotoImage(resize)
#SEH = (PhotoImage(file="7H.png"))# 7)
SES = Image.open("7S.png")
resize = SES.resize((100, 140), Image.ANTIALIAS)
SES = ImageTk.PhotoImage(resize)
#SES = (PhotoImage(file="7S.png"))# 7)



EIC = Image.open("8C.png")
resize = EIC.resize((100, 140), Image.ANTIALIAS)
EIC = ImageTk.PhotoImage(resize)
#EIC = (PhotoImage(file="8C.png"))# 8)
EID = Image.open("8D.png")
resize = EID.resize((100, 140), Image.ANTIALIAS)
EID = ImageTk.PhotoImage(resize)
#EID = (PhotoImage(file="8D.png"))# 8)
EIH = Image.open("8H.png")
resize = EIH.resize((100, 140), Image.ANTIALIAS)
EIH = ImageTk.PhotoImage(resize)
#EIH = (PhotoImage(file="8H.png"))# 8)
EIS = Image.open("8S.png")
resize = EIS.resize((100, 140), Image.ANTIALIAS)
EIS = ImageTk.PhotoImage(resize)
#EIS = (PhotoImage(file="8S.png"))# 8)



NIC = Image.open("9C.png")
resize = NIC.resize((100, 140), Image.ANTIALIAS)
NIC = ImageTk.PhotoImage(resize)
#NIC = (PhotoImage(file="9C.png"))# 9)
NID = Image.open("9D.png")
resize = NID.resize((100, 140), Image.ANTIALIAS)
NID = ImageTk.PhotoImage(resize)
#NID = (PhotoImage(file="9D.png"))# 9)
NIH = Image.open("9H.png")
resize = NIH.resize((100, 140), Image.ANTIALIAS)
NIH = ImageTk.PhotoImage(resize)
#NIH = (PhotoImage(file="9H.png"))# 9)
NIS = Image.open("9S.png")
resize = NIS.resize((100, 140), Image.ANTIALIAS)
NIS = ImageTk.PhotoImage(resize)
#NIS = (PhotoImage(file="9S.png"))# 9)



TEC = Image.open("10C.png")
resize = TEC.resize((100, 140), Image.ANTIALIAS)
TEC = ImageTk.PhotoImage(resize)
#TEC = (PhotoImage(file="10C.png"))# 10)
TED = Image.open("10D.png")
resize = TED.resize((100, 140), Image.ANTIALIAS)
TED = ImageTk.PhotoImage(resize)
#TED = (PhotoImage(file="10D.png"))# 10)
TEH = Image.open("10H.png")
resize = TEH.resize((100, 140), Image.ANTIALIAS)
TEH = ImageTk.PhotoImage(resize)
#TEH = (PhotoImage(file="10H.png"))# 10)
TES = Image.open("10S.png")
resize = TES.resize((100, 140), Image.ANTIALIAS)
TES = ImageTk.PhotoImage(resize)
#TES = (PhotoImage(file="10S.png"))# 10)



JC = Image.open("JC.png")
resize = JC.resize((100, 140), Image.ANTIALIAS)
JC = ImageTk.PhotoImage(resize)
#JC = (PhotoImage(file="JC.png"))# 11)
JD = Image.open("JD.png")
resize = JD.resize((100, 140), Image.ANTIALIAS)
JD = ImageTk.PhotoImage(resize)
#JD = (PhotoImage(file="JD.png"))# 11)
JH = Image.open("JH.png")
resize = JH.resize((100, 140), Image.ANTIALIAS)
JH = ImageTk.PhotoImage(resize)
#JH = (PhotoImage(file="JH.png"))# 11)
JS = Image.open("JS.png")
resize = JS.resize((100, 140), Image.ANTIALIAS)
JS = ImageTk.PhotoImage(resize)
#JS = (PhotoImage(file="JS.png"))# 11)



QC = Image.open("QC.png")
resize = QC.resize((100, 140), Image.ANTIALIAS)
QC = ImageTk.PhotoImage(resize)
#QC = (PhotoImage(file="QC.png"))# 12)
QD = Image.open("QD.png")
resize = QD.resize((100, 140), Image.ANTIALIAS)
QD = ImageTk.PhotoImage(resize)
#QD = (PhotoImage(file="QD.png"))# 12)
QH = Image.open("QH.png")
resize = QH.resize((100, 140), Image.ANTIALIAS)
QH = ImageTk.PhotoImage(resize)
#QH = (PhotoImage(file="QH.png"))# 12)
QS = Image.open("QS.png")
resize = QS.resize((100, 140), Image.ANTIALIAS)
QS = ImageTk.PhotoImage(resize)
#QS = (PhotoImage(file="QS.png"))# 12)



KC = Image.open("KC.png")
resize = KC.resize((100, 140), Image.ANTIALIAS)
KC = ImageTk.PhotoImage(resize)
#KC = (PhotoImage(file="KC.png"))# 13)
KD = Image.open("KD.png")
resize = KD.resize((100, 140), Image.ANTIALIAS)
KD = ImageTk.PhotoImage(resize)
#KD = (PhotoImage(file="KD.png"))# 13)
KH = Image.open("KH.png")
resize = KH.resize((100, 140), Image.ANTIALIAS)
KH = ImageTk.PhotoImage(resize)
#KH = (PhotoImage(file="KH.png"))# 13)
KS = Image.open("KS.png")
resize = KS.resize((100, 140), Image.ANTIALIAS)
KS = ImageTk.PhotoImage(resize)
#KS = (PhotoImage(file="KS.png"))# 13)








def game_window():
    from PIL import ImageTk, Image
    #Creating a canvas
    gamewindow_canvas = Canvas(root, width=1024, height=763)
    gamewindow_canvas.pack(fill="both", expand=True)
    #Set image in canvas
    frame2 = gamewindow_canvas.create_image(0, 0, image=startwindow_bg, anchor="nw")

    #Setting set records
    gamewindow_canvas.create_text(128, 400, text="click to draw card", fill="white", font=("Calibri bold",12))
    gamewindow_canvas.create_text(280, 400, text="card preview", fill="white", font=("Calibri bold", 12))
    gamewindow_canvas.pack()

    player_textbg = Button(root, text="YOU : sets completed 0/3 - remaining (3,3,4)", font=("Calibri bold", 14), fg="white", height=1, width=36, bg="#8b4513")
    player_textbg_window = gamewindow_canvas.create_window(634, 20, anchor="nw", window=player_textbg)
    opponent_textbg = Button(root, text="OPPONENT : sets completed 1/3 - remaining (3,4)", font=("Calibri bold", 14), fg="white", height=1, width=40, bg="#8b4513")
    opponent_textbg_window = gamewindow_canvas.create_window(56, 20, anchor="nw", window=opponent_textbg)





    def how_to_play():
        messagebox.showinfo("How to play?", "Basically you'll have to make 3 pairs of 3,3, and 4 cards.\nThere are 2 ways to make a set in this game.\n\n1st : making a run - A run is basically a series of consecutive cards like (2,3,4), (J,Q,K), etc.\n\n2nd : making a set - A set is basically same cards, (the ones which share the similar value, but belong to other suits like (Ace of Clubs, Ace of Diamonds, Ace of Hearts), etc.\n\nThis applies to 4 cards too\n\nSo you have to make groups of 3-3-4 cards, doesn't matter whether they're all runs, or all sets")

    def begin_game():
        frame2 = gamewindow_canvas.create_image(0, 0, image=gamewindow_bg, anchor="nw")
        sbutton1.destroy()
        sbutton2.destroy()


    #Home screen buttons
    opponent_textbg = Button(root, text="OPPONENT : sets completed 0/3 - remaining (3,3,4)", font=("Calibri bold", 14), fg="white", height=1, width=40, bg="#8b4513")
    opponent_textbg_window = gamewindow_canvas.create_window(56, 20, anchor="nw", window=opponent_textbg)
    sbutton1 = Button(root, text="Play", font=('Hlevetica',20), bg=("green"), fg=("white"), command=begin_game)
    sbutton2 = Button(root, text="How to play", font=('Hlevetica',20), command=how_to_play)
    sbutton1_window = gamewindow_canvas.create_window(700, 660, anchor="nw", window=sbutton1)
    sbutton2_window = gamewindow_canvas.create_window(800, 660, anchor="nw", window=sbutton2)






    #Making draw pile list
    draw_pile = [AC,AD,AH,AS,
           TWC,TWD,TWH,TWS,
           THC,THD,THH,THS,
           FOC,FOD,FOH,FOS,
           FIC,FID,FIH,FIS,
           SIC,SID,SIH,SIS,
           SEC,SED,SEH,SES,
           EIC,EID,EIH,EIS,
           NIC,NID,NIH,NIS,
           TEC,TED,TEH,TES,
           JC,JD,JH,JS,
           QC,QD,QH,QS,
           KC,KD,KH,KS]

    shuffle(draw_pile)


    #Making player list
    player_list = [AC, AH, TWD, THD, FOH, SIC, SES, NIS, QS, QC, JD, KH, KS]

    #Defining in game functions
    def aceofclubs_info():
        messagebox.showinfo("In game function", "There are 2 Ace cards in the player list, you just need one more ace card to complete a set. Look out for one!")
    def aceofhearts_info():
        messagebox.showinfo("In game function", "There are 2 Ace cards in the player list, you just need one more ace card to complete a set. Look out for one!")
    def twoofdiamonds_info():
        messagebox.showinfo("In game function", "You already have the 3 of diamonds in your list. You just need an ace of diamonds, or 4 of diamonds to complete a run. Look out for them!")
    def threeofdiamonds_info():
        messagebox.showinfo("In game function", "You already have the 2 of diamonds in your list. You just need an ace of diamonds, or 4 of diamonds to complete a run. Look out for them!")
    def fourhearts_del():
        answer = messagebox.askquestion("In game function", "4 of Hearts will take time to build any run or set, want to discard it?")
        if answer == "yes":
            cardbutton5.destroy()
    def sevenofspades_info():
        messagebox.showinfo("In game function", "You already have a 9 of spades in your list. You just need the 8 of spades to complete a run. Look out for it!")
    def nineofspades_info():
        messagebox.showinfo("In game function", "You already have a 7 of spades in your list. You just need the 8 of spades to complete a run. Look out for it!")
    def queenofspades_info():
        messagebox.showinfo("In game function", "There are 2 Queen cards in the player list, you just need one more Queen card to complete a set. Look out for one!")
    def queenofclubs_info():
        messagebox.showinfo("In game function", "There are 2 Queen cards in the player list, you just need one more Queen card to complete a set. Look out for one!")
    def jackdiamonds_del():
        answer = messagebox.askquestion("In game function", "Jack of Diamonds will take time to build any run or set, want to discard it?")
        if answer == "yes":
            cardbutton10.destroy()


    #Add buttons
    cardbutton1 = Button(root, image=player_list[0], height=140, width=100, bg="green", command=aceofclubs_info)
    cardbutton2 = Button(root, image=player_list[1], height=140, width=100, bg="green", command=aceofhearts_info)
    cardbutton3 = Button(root, image=player_list[2], height=140, width=100, bg="yellow", command=twoofdiamonds_info)
    cardbutton4 = Button(root, image=player_list[3], height=140, width=100, bg="yellow", command=threeofdiamonds_info)
    cardbutton5 = Button(root, image=player_list[4], height=140, width=100, bg="red", command=fourhearts_del)
    cardbutton6 = Button(root, image=player_list[6], height=140, width=100, bg="yellow", command=sevenofspades_info)
    cardbutton7 = Button(root, image=player_list[7], height=140, width=100, bg="yellow", command=nineofspades_info)
    cardbutton8 = Button(root, image=player_list[8], height=140, width=100, bg="green", command=queenofspades_info)
    cardbutton9 = Button(root, image=player_list[9], height=140, width=100, bg="green", command=queenofclubs_info)
    cardbutton10 = Button(root, image=player_list[10], height=140, width=100, bg="red", command=jackdiamonds_del)

    cardbutton1_window = gamewindow_canvas.create_window(60, 420, anchor="nw", window=cardbutton1)
    cardbutton2_window = gamewindow_canvas.create_window(180, 420, anchor="nw", window=cardbutton2)
    cardbutton3_window = gamewindow_canvas.create_window(300, 420, anchor="nw", window=cardbutton3)
    cardbutton4_window = gamewindow_canvas.create_window(420, 420, anchor="nw", window=cardbutton4)
    cardbutton5_window = gamewindow_canvas.create_window(540, 420, anchor="nw", window=cardbutton5)
    cardbutton6_window = gamewindow_canvas.create_window(60, 580, anchor="nw", window=cardbutton6)
    cardbutton7_window = gamewindow_canvas.create_window(180, 580, anchor="nw", window=cardbutton7)
    cardbutton8_window = gamewindow_canvas.create_window(300, 580, anchor="nw", window=cardbutton8)
    cardbutton9_window = gamewindow_canvas.create_window(420, 580, anchor="nw", window=cardbutton9)
    cardbutton10_window = gamewindow_canvas.create_window(540, 580, anchor="nw", window=cardbutton10)


    #Defining draw cards

    def drawbutton10_del():
        answer = messagebox.askquestion("In game function", "Add Four of Diamonds to player list? (press no to discard the card)")
        if answer == "yes":
            button10.destroy()
            drawbutton10.destroy()
            cardbutton7 = Button(root, image=FOD, height=140, width=100, bg="yellow")
            cardbutton7_window = gamewindow_canvas.create_window(180, 580, anchor="nw", window=cardbutton7)
            player_textbg = Button(root, text="YOU : sets completed 3/3 - remaining (none)", font=("Calibri bold", 14), fg="white", height=1, width=36, bg="#8b4513")
            player_textbg_window = gamewindow_canvas.create_window(634, 20, anchor="nw", window=player_textbg)
            final_answer = messagebox.askquestion("YOU WIN!!", "Congratulations! with this 4 card run, you have completed all the 3 sets required for winning this game! You win! Want to restart?")
            if final_answer == "yes":
                game_window()
            elif final_answer == "no":
                exit()
        elif answer == "no":
            button10.destroy()
            drawbutton10.destroy()
    drawbutton10 = Button(root, image=FOD, height=180, width=133, state=DISABLED)
    drawbutton10_window = gamewindow_canvas.create_window(210, 200, anchor="nw", window=drawbutton10)
    button10 = Button(root, image=card_button, height=180, width=133, command=drawbutton10_del)
    button10_window = gamewindow_canvas.create_window(60, 200, anchor="nw", window=button10)




    def drawbutton9_del():
        answer = messagebox.askquestion("In game function", "Add Six of Spades to player list? (press no to discard the card)")
        if answer == "yes":
            button9.destroy()
            drawbutton9.destroy()
            cardbutton7 = Button(root, image=SIS, height=140, width=100, bg="red")
            cardbutton7_window = gamewindow_canvas.create_window(180, 580, anchor="nw", window=cardbutton7)
        elif answer == "no":
            button9.destroy()
            drawbutton9.destroy()
    drawbutton9 = Button(root, image=SIS, height=180, width=133, state=DISABLED)
    drawbutton9_window = gamewindow_canvas.create_window(210, 200, anchor="nw", window=drawbutton9)
    button9 = Button(root, image=card_button, height=180, width=133, command=drawbutton9_del)
    button9_window = gamewindow_canvas.create_window(60, 200, anchor="nw", window=button9)




    def drawbutton8_del():
        answer = messagebox.askquestion("In game function", "Add Seven of Hearts to player list? (press no to discard the card)")
        if answer == "yes":
            button8.destroy()
            drawbutton8.destroy()
            cardbutton7 = Button(root, image=SEH, height=140, width=100, bg="red")
            cardbutton7_window = gamewindow_canvas.create_window(180, 580, anchor="nw", window=cardbutton7)
        elif answer == "no":
            button8.destroy()
            drawbutton8.destroy()
    drawbutton8 = Button(root, image=SEH, height=180, width=133, state=DISABLED)
    drawbutton8_window = gamewindow_canvas.create_window(210, 200, anchor="nw", window=drawbutton8)
    button8 = Button(root, image=card_button, height=180, width=133, command=drawbutton8_del)
    button8_window = gamewindow_canvas.create_window(60, 200, anchor="nw", window=button8)



    def drawbutton7_del():
        answer = messagebox.askquestion("In game function", "Add Jack of Diamonds to player list? (press no to discard the card)")
        if answer == "yes":
            button7.destroy()
            drawbutton7.destroy()
            cardbutton7 = Button(root, image=JD, height=140, width=100, bg="red")
            cardbutton7_window = gamewindow_canvas.create_window(180, 580, anchor="nw", window=cardbutton7)
        elif answer == "no":
            button7.destroy()
            drawbutton7.destroy()
    drawbutton7 = Button(root, image=JD, height=180, width=133, state=DISABLED)
    drawbutton7_window = gamewindow_canvas.create_window(210, 200, anchor="nw", window=drawbutton7)
    button7 = Button(root, image=card_button, height=180, width=133, command=drawbutton7_del)
    button7_window = gamewindow_canvas.create_window(60, 200, anchor="nw", window=button7)



    def drawbutton6_del():
        answer = messagebox.askquestion("In game function", "Add Ace of Spades to player list? (press no to discard the card)")
        if answer == "yes":
            button6.destroy()
            drawbutton6.destroy()
            cardbutton6 = Button(root, image=AS, height=140, width=100, bg="green")
            cardbutton6_window = gamewindow_canvas.create_window(60, 580, anchor="nw", window=cardbutton6)
            messagebox.showinfo("In game function", "Congratulations! You completed a 3 card set!")
            player_textbg = Button(root, text="YOU : sets completed 2/3 - remaining (4)", font=("Calibri bold", 14), fg="white", height=1, width=36, bg="#8b4513")
            player_textbg_window = gamewindow_canvas.create_window(634, 20, anchor="nw", window=player_textbg)
        elif answer == "no":
            button6.destroy()
            drawbutton6.destroy()
    drawbutton6 = Button(root, image=AS, height=180, width=133, state=DISABLED)
    drawbutton6_window = gamewindow_canvas.create_window(210, 200, anchor="nw", window=drawbutton6)
    button6 = Button(root, image=card_button, height=180, width=133, command=drawbutton6_del)
    button6_window = gamewindow_canvas.create_window(60, 200, anchor="nw", window=button6)



    def drawbutton5_del():
        answer = messagebox.askquestion("In game function", "Add 10 of Clubs to player list? (press no to discard the card)")
        if answer == "yes":
            cardbutton6 = Button(root, image=NIC, height=140, width=100, bg="yellow")
            cardbutton6_window = gamewindow_canvas.create_window(60, 580, anchor="nw", window=cardbutton6)
            button5.destroy()
            drawbutton5.destroy()
            cardbutton7 = Button(root, image=TEC, height=140, width=100, bg="yellow")
            cardbutton7_window = gamewindow_canvas.create_window(180, 580, anchor="nw", window=cardbutton7)
            messagebox.showinfo("In game function", "Almost there! you have 9 & 10 of clubs with you, with 8 of clubs your 3 card run will be completed! Look out for it!")
        elif answer == "no":
            button5.destroy()
            drawbutton5.destroy()
    drawbutton5 = Button(root, image=TEC, height=180, width=133, state=DISABLED)
    drawbutton5_window = gamewindow_canvas.create_window(210, 200, anchor="nw", window=drawbutton5)
    button5 = Button(root, image=card_button, height=180, width=133, command=drawbutton5_del)
    button5_window = gamewindow_canvas.create_window(60, 200, anchor="nw", window=button5)



    def drawbutton4_del():
        answer = messagebox.askquestion("In game function", "Add 9 of Clubs to player list? (press no to discard the card)")
        if answer == "yes":
            cardbutton7 = Button(root, image=NIS, height=140, width=100, bg="red")
            cardbutton7_window = gamewindow_canvas.create_window(180, 580, anchor="nw", window=cardbutton7)
            button4.destroy()
            drawbutton4.destroy()
            cardbutton6 = Button(root, image=NIC, height=140, width=100, bg="red")
            cardbutton6_window = gamewindow_canvas.create_window(60, 580, anchor="nw", window=cardbutton6)
        elif answer == "no":
            button4.destroy()
            drawbutton4.destroy()
    drawbutton4 = Button(root, image=NIC, height=180, width=133, state=DISABLED)
    drawbutton4_window = gamewindow_canvas.create_window(210, 200, anchor="nw", window=drawbutton4)
    button4 = Button(root, image=card_button, height=180, width=133, command=drawbutton4_del)
    button4_window = gamewindow_canvas.create_window(60, 200, anchor="nw", window=button4)



    def drawbutton3_del():
        answer = messagebox.askquestion("In game function", "Add 5 of Diamonds to player list? (press no to discard the card)")
        if answer == "yes":
            button3.destroy()
            drawbutton3.destroy()
            cardbutton5 = Button(root, image=FID, height=140, width=100, bg="yellow")
            cardbutton5_window = gamewindow_canvas.create_window(540, 420, anchor="nw", window=cardbutton5)
            messagebox.showinfo("In game function", "Almost there! you have 2,3 & 5 of diamonds with you, with 4 of diamonds your 4 card run will be completed! Look out for it!")
        elif answer == "no":
            button3.destroy()
            drawbutton3.destroy()
            opponent_textbg = Button(root, text="OPPONENT : sets completed 2/3 - remaining (3)", font=("Calibri bold", 14), fg="white", height=1, width=40, bg="#8b4513")
            opponent_textbg_window = gamewindow_canvas.create_window(56, 20, anchor="nw", window=opponent_textbg)
    drawbutton3 = Button(root, image=FID, height=180, width=133, state=DISABLED)
    drawbutton3_window = gamewindow_canvas.create_window(210, 200, anchor="nw", window=drawbutton3)
    button3 = Button(root, image=card_button, height=180, width=133, command=drawbutton3_del)
    button3_window = gamewindow_canvas.create_window(60, 200, anchor="nw", window=button3)



    def drawbutton2_del():
        answer = messagebox.askquestion("In game function", "Add Queen of Hearts to player list? (press no to discard the card)")
        if answer == "yes":
            button2.destroy()
            drawbutton2.destroy()
            cardbutton10 = Button(root, image=QH, height=140, width=100, bg="green")
            cardbutton10_window = gamewindow_canvas.create_window(540, 580, anchor="nw", window=cardbutton10)
            messagebox.showinfo("1st set complete!", "Congratulations! you have completed a 3 card set!")
            player_textbg = Button(root, text="YOU : sets completed 1/3 - remaining (3,4)", font=("Calibri bold", 14),fg="white", height=1, width=36, bg="#8b4513")
            player_textbg_window = gamewindow_canvas.create_window(634, 20, anchor="nw", window=player_textbg)
            opponent_textbg = Button(root, text="OPPONENT : sets completed 1/3 - remaining (3,4)", font=("Calibri bold", 14), fg="white", height=1, width=40, bg="#8b4513")
            opponent_textbg_window = gamewindow_canvas.create_window(56, 20, anchor="nw", window=opponent_textbg)
        elif answer == "no":
            button2.destroy()
            drawbutton2.destroy()
    drawbutton2 = Button(root, image=QH, height=180, width=133, state=DISABLED)
    drawbutton2_window = gamewindow_canvas.create_window(210, 200, anchor="nw", window=drawbutton2)
    button2 = Button(root, image=card_button, height=180, width=133, command=drawbutton2_del)
    button2_window = gamewindow_canvas.create_window(60, 200, anchor="nw", window=button2)



    def drawbutton1_del():

        answer = messagebox.askquestion("In game function", "Add King of Hearts to player list? (press no to discard the card)")
        if answer == "yes":
            button1.destroy()
            drawbutton1.destroy()
            cardbutton5 = Button(root, image=KH, height=140, width=100, bg="red")
            cardbutton5_window = gamewindow_canvas.create_window(540, 420, anchor="nw", window=cardbutton5)
        elif answer == "no":
            button1.destroy()
            drawbutton1.destroy()
    drawbutton1 = Button(root, image=KH, height=180, width=133, state=DISABLED)
    drawbutton1_window = gamewindow_canvas.create_window(210, 200, anchor="nw", window=drawbutton1)
    button1 = Button(root, image=card_button, height=180, width=133, command=drawbutton1_del)
    button1_window = gamewindow_canvas.create_window(60, 200, anchor="nw", window=button1)




game_window()
play()

root.mainloop()
