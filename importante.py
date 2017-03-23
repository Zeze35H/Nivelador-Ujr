
from sense_hat import SenseHat

sense = SenseHat()


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
    elif x == 0 and y >= -0.5 and  z >= 0.5 and z != 1 and y < 0:
        sense.set_rotation(180)
        sense.set_pixels(laranja)
        #(seta para baixo)
        
    elif x <= -0.5 and y == 0 and z <= 0.5 :
        sense.set_rotation(90)
        sense.set_pixels(vermelho)
    elif x >= -0.5 and y == 0 and z >=0.5 and x < 0 and z != 1:
        sense.set_rotation(90)
        sense.set_pixels(laranja)
        #(seta para direita)
        
    elif x >= 0.5 and y == 0 and z <= 0.5:
        sense.set_rotation(270)
        sense.set_pixels(vermelho)
    elif x <= 0.5 and y == 0 and z >= 0.5 and x > 0 and z != 1: 
        sense.set_rotation(270)
        sense.set_pixels(laranja)
        #(seta para esquerda)
        
    elif x == 0 and y >= 0.5 and z <= 0.5:
        sense.set_rotation(0)
        sense.set_pixels(vermelho)
    elif x == 0 and y <= 0.5 and z >= 0.5 and y > 0 and z != 1:
        sense.set_rotation(0)
        sense.set_pixels(laranja)
        #(seta para cima)
        
    elif x == 0 and y == 0 and z == 1:
        sense.set_rotation(0)
        sense.set_pixels(green)

    elif 
                    
        #(verde)

   
    

    
