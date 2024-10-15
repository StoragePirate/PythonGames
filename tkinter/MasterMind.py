import tkinter
from random import randint

class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("MasterMind")
        self.resizable(False, False)

class TheLabelFrame(tkinter.LabelFrame):
    def __init__(self, root, headerText="GameBoard"):
        super().__init__(root)
        self.configure(text=headerText)
        self.pack(expand=True)
    def Button(self):
        self.Button=tkinter.Button(self, text="Check",command=CheckIfWin)
        self.Button.pack(expand=True )
    
class GameBoardCanvas(tkinter.Canvas):
    i=1
    colorList=['black','brown','orange', 'red', 'green', 'blue']
    colorList.sort()
    winningColorCombo=[]
    def __init__(self, root):
        self.headerText=f"Round {GameBoardCanvas.i}"
        self.LabelFrameName=TheLabelFrame(root, self.headerText)
        GameBoardCanvas.i+=1        
        super().__init__(self.LabelFrameName, bg='white',width=180, height=40)
        self.pack()
    @classmethod
    def SecretColors(cls):
        for _ in range(0,4):
            cls.winningColorCombo.append(cls.GetRandomColor())
        print ("Winning Colors:", cls.winningColorCombo)
        return cls.winningColorCombo
    @classmethod    
    def GetRandomColor(cls):
        return cls.colorList[randint(0,len(cls.colorList)-1)]    
    def isActive(self):
        self.configure(bg='yellow')        
    def wasActive(self):
        print (self)
        self.configure(bg='white')
    def GameCircle(self, x1:int, y1:int, x2:int, y2:int):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2        
        for _ in range(0,4):            
            self.create_oval(self.x1, self.y1, self.x2, self.y2, fill=GameBoardCanvas.GetRandomColor())
            self.x1+=30
            self.y1+=0
            self.x2+=30
            self.y2+=0            
            self.bind("<Button-3>",self.GetColor)
            self.bind("<Button-1>",self.ChangeColor)
    def GetColor(self, event):        
        clicked_item = self.find_overlapping(event.x - 2, event.y - 2, event.x + 2, event.y + 2)
        if clicked_item and clicked_item[0] < 5:
            color = self.itemcget(clicked_item[0], "fill")
        #gets all colors in this block (30 is the radius)
        self.items = self.find_overlapping(0, 30, 110, 30 + 2 * 30)
        self.colors = [self.itemcget(item, "fill") for item in self.items]
        # print (self.colors)       
            
    def ChangeColor(self, event):
        try:
            currentFrame=int(str(self.LabelFrameName)[-1])
            if currentFrame==0:
                currentFrame=10
        except:
            currentFrame=1
        
        if currentFrame > GameBoardCanvas.i:        
            clicked_item = self.find_overlapping(event.x - 2, event.y - 2, event.x + 2, event.y + 2)
            if clicked_item and clicked_item[0] < 5:
                currentColor= self.itemcget(clicked_item[0], "fill")            
                colorIndex=GameBoardCanvas.colorList.index(currentColor)            
                if colorIndex == len(GameBoardCanvas.colorList)-1:
                    colorIndex=0
                else:
                    colorIndex+=1
                self.itemconfig(clicked_item[0], fill=GameBoardCanvas.colorList[colorIndex])
    def PositionIndicator(self):
        self.y1/=2
        self.y2/=2
        for i in range(0,4):
            if i == 2:
                self.x1-=60
                self.y1+=15
                self.x2-=60
                self.y2+=15            
            self.create_oval(self.x1, self.y1, self.x2, self.y2, outline='black',width=1 )
            self.x1+=30
            self.y1+=0
            self.x2+=30
            self.y2+=0   

def CheckIfWin():
    #example: Framelabel 1 get me the colors in order
    items = list[GameBoardCanvas.i].find_overlapping(0, 30, 110, 30 + 2 * 30)
    colors = [list[GameBoardCanvas.i].itemcget(item, "fill") for item in items]    
    print (GameBoardCanvas.i+1, colors, GameBoardCanvas.winningColorCombo)
    if colors == GameBoardCanvas.winningColorCombo:
        print ("WINNER")
        MyLabelFrame.Button.configure(state=tkinter.DISABLED)
    elif GameBoardCanvas.i == 9:
        #disable the button on round 10
        MyLabelFrame.Button.configure(state=tkinter.DISABLED)
    else:        
        list[GameBoardCanvas.i].wasActive()
        GameBoardCanvas.i+=1
        list[GameBoardCanvas.i].isActive()


def main():
    root=MainWindow()
    global MyLabelFrame
    MyLabelFrame=TheLabelFrame(root)
    MyLabelFrame.Button()
    global list
    list=[]
    for i in range(0,10):
        list.append(GameBoardCanvas(MyLabelFrame))
        list[i].GameCircle(10,10,30,30)
        list[i].PositionIndicator()

    # Round 1 set to yellow
    GameBoardCanvas.i=0
    
    # create the secret combination
    GameBoardCanvas.SecretColors()

    #set Round 1 to active
    list[GameBoardCanvas.i].isActive()
    
    # the magic sauce
    # from the 'active' label it gets the 4 colors
    #Framelabel 1 get me the colors in order
    #items = list[GameBoardCanvas.i].find_overlapping(0, 30, 110, 30 + 2 * 30)
    #colors = [list[GameBoardCanvas.i].itemcget(item, "fill") for item in items]    
    #print (colors)


    root.mainloop()



if __name__ == "__main__":
    main()