from tkinter import *

player = ['O','X']
turn = [1]
computerIndex = [0]
humanIndex = [1]


score = {"c1":[0,0], "c2":[0,0], "c3":[0,0], "r1":[0,0], "r2":[0,0] , "r3":[0,0], "d1":[0,0], "d2":[0,0]}

boardScore = {
      "1": [ "c1", "r1", "d1"],
      "2": [ "c2", "r1"],
      "3": [ "c3", "r1", "d2"],
      "4": [ "c1", "r2"],
      "5": [ "c2", "r2", "d1", "d2"],
      "6": [ "c3", "r2"],
      "7": [ "c1", "r3", "d2"],
      "8": [ "c2", "r3"],
      "9": [ "c3", "r3", "d1"]
}



def checkWin():
   for i in score.keys():
      if score[i][0] == 3:
         return 0
      elif score[i][1] == 3:
        return 1
   return 'NULL'

def checkTie():
   for i in score.keys():      
     if score[i][0] == 0 or score[i][1] == 0:
            return False
   return True

def showpveMenu():
  mainMenu.pack_forget()
  pvpMenu.pack_forget()
  pveMenu.pack(fill=BOTH,expand=True)

def showpvpMenu():
  mainMenu.pack_forget()
  pveMenu.pack_forget()
  pvpMenu.pack(fill=BOTH,expand=True)

def showMainMenu():
   pvpMenu.pack_forget()
   pveMenu.pack_forget()
   mainMenu.pack()
   reset()
   resetE()

def boardClicked(event):
   cw = checkWin()
   istie = checkTie()
   if cw != 'NULL' or istie:
      return
   clicked = event.widget
   if(clicked['text'] == 'X' or clicked['text'] == "O"):
      return
   if (turn[0] %2 == 1):
      XorO= 'X'
      gameplayLabel['text'] = "It's O move."
   else:
      XorO= "O"
      gameplayLabel['text'] = "It's X move."

   for i in boardScore[str(clicked['text'])]:
      score[i][turn[0]%2] += 1
      

   cw = checkWin() 
   if cw == 0 or cw == 1:
      gameplayLabel['text'] = player[cw] + " has won 🎉" 
    
   istie = checkTie()
   if(istie):
       gameplayLabel['text'] = "It's Tie!"
   clicked.config(state= 'normal',text=XorO,font=("Arial", 16))
   turn[0] = turn[0] + 1



def reset(): 
   gameplayLabel['text'] = "It's X move."
   turn[0] = 1
   x = 1
   for i in range(3):
    for j in range(3):
      Boardbtns[i][j]['text'] = x
      Boardbtns[i][j].config(state='normal',font=("Arial", 10))
      x += 1
   for i in score.keys():
      score[i] = [0,0]
      

def getEmptyButton(key):
    for i in range(3):
        for j in range(3):
            btn = BoardbtnsE[i][j]
            n = btn['text']
            if (btn['text'] != 'O' and btn['text'] != "X") and key in boardScore[str(n)]:
               
                btn.config(state='normal', text=player[computerIndex[0]],font=("Arial", 16))
                for line in boardScore[str(n)]:
                    score[line][computerIndex[0]] += 1
                return  

      

def computerMove():

   if checkTie == True:
      gameplayLabelE['text'] = "It's Tie!" 
      return
   if checkWin() != 'NULL':
      return
   for i in score.keys(): # Win oppurtunity
     if score[i][computerIndex[0]] == 2 and score[i][humanIndex[0]] == 0 :

        getEmptyButton(i)
        cw = checkWin() 
        if cw != 'NULL':
           gameplayLabelE['text'] = " Computer has won 🎉" 
        return
      
   for i in score.keys(): # Block oppurtunity
     if score[i][humanIndex[0]] == 2 and score[i][computerIndex[0]] == 0 :
  
        getEmptyButton(i)
        cw = checkWin() 
        if cw != 'NULL':
           gameplayLabelE['text'] = " Computer has won 🎉" 
        return
   
   for i in score.keys(): # Win oppurtunity
     if score[i][computerIndex[0]] == 1 and score[i][humanIndex[0]] == 0 :
   
        getEmptyButton(i)
        cw = checkWin() 
        if cw != 'NULL':
           gameplayLabelE['text'] = " Computer has won 🎉" 
        return
   # If no block nor win just play anywhere
   for i in range(3):
    for j in range(3):
      btn = BoardbtnsE[i][j]
      if (btn['text'] != 'O' and btn['text'] != 'X'):
         n = str(btn['text'])
         btn.config(state='normal', text=player[computerIndex[0]],font=("Arial", 16))
  
         for line in boardScore[n]:
            score[line][computerIndex[0]] += 1
         return
   
      
      
def boardClickedE(event):
   if choice.get() == 'N':
      return
   
   if checkTie == True:
      gameplayLabelE['text'] = "It's Tie!" 
      return
   if checkWin() != 'NULL':
      return
   
   clicked = event.widget
   if(clicked['text'] == 'X' or clicked['text'] == "O"):
      return
   
   

   for i in boardScore[str(clicked['text'])]:
      score[i][humanIndex[0]] += 1
      


   xOro = player[humanIndex[0]]
   

   
   
   clicked.config(state= 'normal',text=xOro,font=("Arial", 16))
   cw = checkWin() 
   if cw == 0 or cw == 1:
      gameplayLabelE['text'] = " You won 🎉" 
      return
    
   istie = checkTie()
   if(istie):
       gameplayLabelE['text'] = "It's Tie!"
       return   
   computerMove()
   

def resetE(): 
   gameplayLabelE['text'] = ""
   turn[0] = 1
   x = 1
   for i in range(3):
    for j in range(3):
      BoardbtnsE[i][j]['text'] = x
      BoardbtnsE[i][j].config(state='normal',font=("Arial", 10))
      x += 1
   for i in score.keys():
      score[i] = [0,0]
   choice.set('N')
   r1['state'] ='normal'
   r2['state'] ='normal'
   gameplayLabelE['text'] = ' '
   selectLabel['text'] = 'Select your role to start: '

   
   

def lockRadio():
   r1['state'] ='disabled'
   r2['state'] ='disabled'
   gameplayLabelE['text'] = 'Game has started!'
   selectLabel['text'] = ' '
   if(choice.get() == "O"):
      computerIndex[0] = 1
      humanIndex[0] = 0
      computerMove()
   else:
      computerIndex[0] = 0
      humanIndex[0] = 1


root = Tk()

root.title('Tic Tac Toe')
window_width = 600
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))


root.geometry(f"{window_width}x{window_height}+{x}+{y}")


# Frame 1 : Main Menu
mainMenu = Frame(root)
mmLabel = Label(mainMenu, text="Welcome to TicTacToe game!",font=("Arial", 16))
pvpBtn = Button(mainMenu, text="Player vs. Player", command=showpvpMenu,font=("Arial", 16))
pveButton = Button(mainMenu, text='Player vs. Computer', command=showpveMenu,font=("Arial", 16))
mmLabel.pack(side=TOP,pady=20)
pvpBtn.pack(fill=X,pady=5)
pveButton.pack(fill=X,pady=5)
mainMenu.pack()


# Frame 2 : PvP
pvpMenu = Frame(root)
pvpLabel = Label(pvpMenu,text='Player vs. Player')
gameplayLabel = Label(pvpMenu, text="It's X move.",font=("Arial", 16))
pvpLabel.pack(pady=5)
gameplayLabel.pack(pady=5)
boardPVP = Frame(pvpMenu)

Boardbtns =[[1,1,1],[1,1,1],[1,1,1]]
n = 1
for i in range(3):
  for j in range(3):
    Boardbtns[i][j] = Button(boardPVP,text=n,font=("Arial", 10), fg="black", bg="lightgray", activebackground="gray", activeforeground="white")
    Boardbtns[i][j].grid(row=i*4, column=j*4,sticky="nsew",rowspan=4,columnspan=4)
    Boardbtns[i][j].bind('<Button-1>', boardClicked)
    n += 1
for i in range(12):  
    boardPVP.rowconfigure(i, weight=1)
    boardPVP.columnconfigure(i, weight=1)

resetButton = Button(pvpMenu, text='Reset', command=reset)
resetButton.pack(pady=10)
backButton = Button(pvpMenu, text='Back', command=showMainMenu)
boardPVP.pack(fill=BOTH ,expand=True,padx=40,pady=40)
backButton.pack(pady=10)


   

# Frame 3: Player vs. Computer
pveMenu = Frame(root)
pveLabel = Label(pveMenu,text='Player vs. Computer')
pveLabel.pack(pady=5)
selectLabel = Label(pveMenu, text="Select your role to start:",font=("Arial", 16))
selectLabel.pack()
choiveLabel = Label(pveMenu, text="Play as:")
choiveLabel.pack(anchor='w',padx=10)
choice = StringVar(value='N')
r1 = Radiobutton(pveMenu, text="X", variable=choice, value="X",command=lockRadio)
r2 = Radiobutton(pveMenu, text="O", variable=choice, value="O",command=lockRadio)
r1.pack(anchor="w",padx=10)
r2.pack(anchor="w",padx=10)


gameplayLabelE = Label(pveMenu, text="",font=("Arial", 16))
gameplayLabelE.pack(pady=5)
boardPVe = Frame(pveMenu)

BoardbtnsE =[[1,1,1],[1,1,1],[1,1,1]]
n = 1
for i in range(3):
  for j in range(3):
    BoardbtnsE[i][j] = Button(boardPVe,text=n,font=("Arial", 10), fg="black", bg="lightgray", activebackground="gray", activeforeground="white")
    BoardbtnsE[i][j].grid(row=i*4, column=j*4,sticky="nsew",rowspan=4,columnspan=4)
    BoardbtnsE[i][j].bind('<Button-1>', boardClickedE)
    n += 1
for i in range(12):  
    boardPVe.rowconfigure(i, weight=1)
    boardPVe.columnconfigure(i, weight=1)

backButtonE = Button(pveMenu, text='Back', command=showMainMenu)
resetButtonE = Button(pveMenu, text='Reset', command=resetE)
resetButtonE.pack(pady=10)
boardPVe.pack(fill=BOTH ,expand=True,padx=40,pady=40)
backButtonE.pack(pady=10)



root.mainloop()
