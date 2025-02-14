import random
from tkinter import Tk, Frame, Button

color = "blue"
color2 = "grey"

window = Tk()
window.title("password generator")
window.config(background=color2)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9',' ', '!', '"', '#', '$', '%', '&',"'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '', '{', '|', '}', '~']

def calcul():
    mdp = random.sample(letters, 20)
    password = ''.join(mdp)
    with open('/storage/emulated/0/mot de passe/password_test.txt', 'a') as file:
        file.write(password + '\n')


def calcul2():
    mdp = random.sample(letters, 20)
    password = ''.join(mdp)
    with open('/storage/emulated/0/mot de passe/password.txt', 'a') as file:
        file.write(password + '\n')
    
        
calcul = Button(window, text= "generate password_test", command= calcul)
calcul.pack()

calcul2 = Button(window, text= "generate password", command= calcul2, fg="blue")
calcul2.pack()

window.mainloop()