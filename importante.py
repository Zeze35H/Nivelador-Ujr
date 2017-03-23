from sense_hat import SenseHat
from guizero import App
from guizero import Text
from guizero import PushButton
    
app = App(title="Nivelador")

welcome_message = Text(app, text="Bem-vindo ao Nivelador", size=100, font="Times New Roman", color="black")

def start():
    update_text = PushButton(app, start, text="START")
    update_text.config(height=2, width=30)
    
app.display()

sense = SenseHat()

import pygame

pygame.init()

s = (pygame.mixer.music.load ("/home/pi/Downloads/Alien_AlarmDrum.wav"))
print(s)

r = [255, 0, 0]
o = [255, 127, 0]
w = [255, 255, 0]
g = [0, 255, 0]
b = [0, 0, 255]
i = [75, 0, 130]
v = [159, 0, 255]

e = [0, 0, 0]


vermelho = [
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
r,e,e,r,r,e,e,r,
e,r,e,r,r,e,r,e,
e,e,r,r,r,r,e,e,
e,e,e,r,r,e,e,e,
]

vermelho_diagonal = [
r,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
e,e,r,e,e,e,e,e,
e,e,e,r,e,e,e,r,
e,e,e,e,r,e,e,r,
e,e,e,e,e,r,e,r,
e,e,e,e,e,e,r,r,
e,e,e,r,r,r,r,r,
]

laranja_diagonal = [
o,e,e,e,e,e,e,e,
e,o,e,e,e,e,e,e,
e,e,o,e,e,e,e,e,
e,e,e,o,e,e,e,o,
e,e,e,e,o,e,e,o,
e,e,e,e,e,o,e,o,
e,e,e,e,e,e,o,o,
e,e,e,o,o,o,o,o,
]

laranja = [
e,e,e,o,o,e,e,e,
e,e,e,o,o,e,e,e,
e,e,e,o,o,e,e,e,
e,e,e,o,o,e,e,e,
o,e,e,o,o,e,e,o,
e,o,e,o,o,e,o,e,
e,e,o,o,o,o,e,e,
e,e,e,o,o,e,e,e,
]

green = [
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
]


def musica():
    pygame.mixer.music.load("/home/pi/Downloads/Alien_AlarmDrum.wav")
    pygame.mixer.music.play(0)
 

while True:
    x = sense.get_accelerometer_raw()['x']
    y = sense.get_accelerometer_raw()['y']
    z = sense.get_accelerometer_raw()['z']

    x = round(x, 1)
    y = round(y, 1)
    z = round(z, 1)

    print("pitch={0}, roll={1}, yaw={2}".format(x,y,z))
    
    
    if  x == 0 and y <= -0.5 and z <= 0.5 and z != 1:
        sense.set_rotation(180)
        sense.set_pixels(vermelho)
        musica()
    elif x == 0 and y >= -0.5 and  z >= 0.5 and z != 1 and y < 0:
        sense.set_rotation(180)
        sense.set_pixels(laranja)
        #(seta para baixo)
        
        
    elif x <= -0.5 and y == 0 and z <= 0.5 :
        sense.set_rotation(90)
        sense.set_pixels(vermelho)
        musica()
    elif x >= -0.5 and y == 0 and z >=0.5 and x < 0 and z != 1:
        sense.set_rotation(90)
        sense.set_pixels(laranja)
        #(seta para direita)
        
        
    elif x >= 0.5 and y == 0 and z <= 0.5:
        sense.set_rotation(270)
        sense.set_pixels(vermelho)
        musica()
    elif x <= 0.5 and y == 0 and z >= 0.5 and x > 0 and z != 1: 
        sense.set_rotation(270)
        sense.set_pixels(laranja)
        #(seta para esquerda)

        
    elif x == 0 and y >= 0.5 and z <= 0.5:
        sense.set_rotation(0)
        sense.set_pixels(vermelho)
        musica()
    elif x == 0 and y <= 0.5 and z >= 0.5 and y > 0 and z != 1:
        sense.set_rotation(0)
        sense.set_pixels(laranja)
        #(seta para cima)

        
    elif x <= -0.5 and y <= -0.5 and z <= 0.5:
        sense.set_rotation(180)
        sense.set_pixels(vermelho_diagonal)
        musica()
    elif x >= -0.3 and y <= -0.8 and z >= -0.1 and z <= 0.1 and x < 0:
        sense.set_rotation(180)
        sense.set_pixels(laranja_diagonal)
    elif x <= -0.8 and y >= -0.3 and z >= -0.1 and z <= 0.1 and y < 0:
        sense.set_rotation(180)
        sense.set_pixels(laranja_diagonal)
    elif x >= -0.5 and y >= -0.5 and z >= 0.5 and x < 0 and y < 0 and z != 1:
        sense.set_rotation(180)
        sense.set_pixels(laranja_diagonal)
        #(seta canto inferior direito)


    elif x <= -0.5 and y >= 0.5 and z <= 0.5:
        sense.set_rotation(90)
        sense.set_pixels(vermelho_diagonal)
        musica()
    elif x <= -0.8 and y <= 0.3 and z >= -0.1 and z <= 0.1 and y > 0:
        sense.set_rotation(90)
        sense.set_pixels(laranja_diagonal)
    elif x >= -0.5 and y <= 0.5 and z >= 0.5 and x < 0 and y > 0 and z != 1:
        sense.set_rotation(90)
        sense.set_pixels(laranja_diagonal)
    elif x >= -0.3 and y >= 0.8 and z >= -0.1 and z <= 0.1 and x < 0:
        sense.set_rotation(90)
        sense.set_pixels(laranja_diagonal)
        #(seta canto superior direito)


    elif x >= 0.5 and y >= 0.5 and z <= 0.5:
        sense.set_rotation(0)
        sense.set_pixels(vermelho_diagonal)
        musica()
    elif x <= 0.5 and y <= 0.5 and z >= 0.5 and x > 0 and y > 0 and z != 1:  
        sense.set_rotation(0)
        sense.set_pixels(laranja_diagonal)
    elif x <= 0.3 and y >= 0.8 and z >= -0.1 and z <= 0.1 and x > 0:
        sense.set_rotation(0)
        sense.set_pixels(laranja_diagonal)
    elif x >= 0.8 and y <= 0.3 and z >= -0.1 and z <= 0.1 and y > 0:
        sense.set_rotation(0)
        sense.set_pixels(laranja_diagonal)
        #(seta canto superior esquerdo)
        

    elif x >= 0.5 and y <= -0.5 and z <= 0.5:
        sense.set_rotation(270)
        sense.set_pixels(vermelho_diagonal)
        musica()
    elif x <= 0.5 and y >= -0.5 and z >= 0.5 and x > 0 and y < 0 and z != 1:
        sense.set_rotation(270)
        sense.set_pixels(laranja_diagonal)
    elif x >= 0.8 and y >= -0.3 and z >= -0.1 and z <= 0.1 and y < 0:
        sense.set_rotation(270)
        sense.set_pixels(laranja_diagonal)
    elif x <= 0.3 and y <= -0.8 and z >= -0.1 and z <= 0.1 and x > 0:
        sense.set_rotation(270)
        sense.set_pixels(laranja_diagonal)
        #(seta canto inferior esquerdo)


    elif x == 0 and y == 0 and z == 1:
        sense.set_rotation(180)
        sense.set_pixels(green)              
        #(verde)
   
