import tkinter
from tkinter import messagebox
import itertools


class TheMainUI(tkinter.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Tic Tac Toe')
        self.resizable(False, False)
        self.iconbitmap('sol.ico')

root=TheMainUI()

buttonCoordinates ={
    1:(0,0),
    2:(0,1),
    3:(0,2),
    4:(1,0),
    5:(1,1),
    6:(1,2),
    7:(2,0),
    8:(2,1),
    9:(2,2)
    }

#sort the win list
win=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
for i in range(len(win)):
    win[i] = tuple(sorted(win[i]))

class MenuBar(tkinter.Menu):
    def __init__(self, root):
        super().__init__(root)
        file_menu = tkinter.Menu(self, tearoff=0)
        self.add_cascade(label="Menu", menu=file_menu)
        file_menu.add_command(label="New Game", command=resetGameBoard)
        file_menu.add_command(label="Quit", command=quit)
        root.config(menu=self)

class button(tkinter.Button):
    #tracks the pressed buttons
    winX=[]
    win0=[]
    def __init__(self, x, y):
        super().__init__(root, height=2, width=6, font = ("Calibri", 20), command=self.buttonPressed)
        self.x=x
        self.y=y          
        self.grid (row = self.x, column = self.y)
    def buttonPressed(self):
        global player        
        self['state']='disabled'
        if player == True:
            self['text']='X'
            checkWinning(self)
            player=False
        else:
            self['text']='0'
            checkWinning(self)
            player=True
        whoIsNext()
    
    def returnXY(self):
        return (self.x, self.y)

def whoIsNext():
    if player == True:
        playerName = 'X'
    else:
        playerName = 0
    statusBar = tkinter.Label(root, text=str(playerName)+" is going next.", anchor=tkinter.W, relief=tkinter.SUNKEN)
    statusBar.grid(row=9,columnspan=3, sticky='ew')
                              

# creates all possible permutations
# sort the elements and subelements
def generate_permutations(numbers):
    perms=list(itertools.combinations(numbers, 3))    
    for i in range(len(perms)):
        perms[i] = tuple(sorted(perms[i]))
    return perms

def checkWinning(myButton):
    global counter
    
    # converts button position to button Number
    for key, value in buttonCoordinates.items():
        if value == myButton.returnXY():
            if player == True:
                button.winX.append(int(key))
                break
            else:
                button.win0.append(int(key))
                break
            
    # it takes at least 5 moves to win
    if counter < 6:
        # creates every possible permutation that a player has pressed and records it
        if player == True:
            permu=generate_permutations(button.winX)
        else:
            permu=generate_permutations(button.win0)
        
        # take the first permutation out of the list
        for ele in permu:
            # check if the element is in the winning combo
            if ele in win:
                # if there is a winner, convert one button at a time to its position
                for buttonNum in ele:
                    # convert the button number to X, Y position
                    for but in buttonList:
                        # convert the background color of the winning buttons to green
                        if buttonCoordinates[buttonNum] == but.returnXY():
                            but.config(bg='#90EE90')
                        # flip every button to disabled
                        else:
                            but['state']='disabled'                            
                    
                # congratulate the winnter    
                messagebox.showwarning(myButton.config()['text'][-1],"Congratulations!")
                counter=9
                break
                
    counter-=1
    # throw game over if you are out of moves
    if counter == 0:
        messagebox.showwarning("GAMEOVER!", "GAMEOVER!")

def setGameBoard():
    global buttonList, player, counter    
    player=True
    buttonList=[]
    #global counter
    counter=9
    # create 3x3 board
    x=-1
    y=0

    #place the buttons
    for _ in range(0,9):    
        if x == 2:
            y+=1
            x=0
        else:
            x+=1
        buttonList.append(button(y, x))
    whoIsNext()

def destroyAllObjects():
    pass

def resetGameBoard():
    global buttonList
    setGameBoard()    
    #for i in buttonList:        
    #    i.gameButton.destroy()        
    #    del i
    print (len(buttonList))
    buttonList=[]
    setGameBoard()    
    button.winX=[]
    button.win0=[]

menubar=MenuBar(root)
setGameBoard()


root.mainloop()