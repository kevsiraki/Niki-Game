import tkinter

okToPressReturn = True

hunger = 100
day = 0
entertainment = 100
hydration = 100
money = 999
work = 0


def startGame(event):

    global okToPressReturn

    if okToPressReturn == False:
        pass

    else:
        startLabel.config(text="")
        updateHunger()
        updateDay()
        updateEntertainment()
        updateDisplay()

        okToPressReturn = False

def updateDisplay():

    global hunger
    global day
    global entertainment
    
    if hunger <= 50:
        nik.config(image = hungryphoto)
    elif entertainment <=30:
        nik.config(image = boredphoto)
    else:
        nik.config(image = normalphoto)

    hungerLabel.config(text="Hunger: " + str(hunger))

    dayLabel.config(text="Day: " + str(day))

    entertainmentLabel.config(text="Entertainment: " + str(entertainment))

    nik.after(100, updateDisplay)

def updateHunger():

    global hunger

    hunger -= 10

    if isAlive():
        hungerLabel.after(500, updateHunger)

def updateDay():

    global day

    day += 1

    if isAlive():
        dayLabel.after(5000, updateDay)

def updateEntertainment():

    global entertainment

    entertainment -= 5

    if isAlive():
        entertainmentLabel.after(700, updateEntertainment)

def feed():

    global hunger

    if hunger <= 95:
        hunger += 20
    else:
        hunger -= 20

def entertain():

    global entertainment

    if entertainment <= 95:
        entertainment += 20
    else:
        entertainment -= 10
       
def isAlive():

    global hunger
    global entertainment

    if hunger <= 0:
        startLabel.config(text="You have failed to keep Niki alive.")
    elif entertainment <= 0:
        startLabel.config(text="Niki got so bored she ran away.")
    else:
        return True

root = tkinter.Tk()
root.title("Keep Niki Alive")
root.geometry("300x500")

startLabel = tkinter.Label(root, text="Press 'Enter' to begin.", font=('Helvetica', 13))
startLabel.pack()

hungerLabel = tkinter.Label(root, text="Hunger: " + str(hunger), font=('Helvetica', 12))
hungerLabel.pack()

entertainmentLabel = tkinter.Label(root, text="Entertainment: " + str(entertainment), font=('Helvetica', 12))
entertainmentLabel.pack()

dayLabel = tkinter.Label(root, text="Day: " + str(day), font=('Helvetica', 12))
dayLabel.pack()

hungryphoto = tkinter.PhotoImage(file="h.gif")
normalphoto = tkinter.PhotoImage(file="n.gif")
boredphoto = tkinter.PhotoImage(file="b.gif")

nik = tkinter.Label(root, image=normalphoto)
nik.pack()

btnFeed = tkinter.Button(root, text="Feed Niki", command = feed)
btnFeed.pack()

btnEntertain = tkinter.Button(root, text="Entertain Niki", command = entertain)
btnEntertain.pack()

root.configure(background='pink')
root.bind( '<Return>', startGame)
root.mainloop()



