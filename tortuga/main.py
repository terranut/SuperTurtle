from turtle import *

from chachaclas import chachafunctions as cha
from chachaclas import Tortuga


import random

s=Screen()
width=900
height=700
s.setup(width,height)
s.tracer(2,20)
print(s.turtles())


#bob=cha.new('yellow')
#jesi=cha.new('blue',visibility=True)


bob=Tortuga.Tortuga(pantalla=[width,height],visibility=False,speed=1)
carl=Tortuga.Tortuga(pantalla=[width,height],shape='arrow',visibility=False,color='grey',speed=1)
carl.ejes()









#bob.celda(50,15)
#bob.celda(50,152

bob.cuadricula(3,3,x=-150,y=150)

carl.cuadricula(3,3,x=150,y=150)

print(bob.coords)
print(carl.coords)


'''
for key in bob.coords:
	for celda in bob.coords[key]:
		bob.equis(x=celda[0],y=celda[1])
'''















#cha.square(jesi,40)




















#print(help(s.screensize))



s.exitonclick()
#mainloop()

'''

t.write(t.position(), move=False, align="left", font=("Arial", 10, "normal"))
posiciones.append(t.position())

t.goto(0,0)

t.left(90)
t.forward(100)
t.write(t.position(), move=False, align="left", font=("Arial", 10, "normal"))
posiciones.append(t.position())

t.goto(0,0)


t.left(135)
t.forward(100)
t.write(t.position(), move=False, align="left", font=("Arial", 10, "normal"))
posiciones.append(t.position())


t.write(posiciones, move=False, align="left", font=("Arial", 10, "normal"))

for i in posiciones:
	t.goto(i)
	'''

'''



t.forward(100) 

t.write('gira 45', move=False, align="left", font=("Arial", 10, "normal"))
t.left(45)

t.write('Levanta lapiz', move=False, align="left", font=("Arial", 10, "normal"))
t.up()

t.write('Acanza sin pintar', move=False, align="left", font=("Arial", 10, "normal"))
t.forward(50)

t.write('Coloca lapiz', move=False, align="left", font=("Arial", 10, "normal"))
t.down()



t.write('Marcha atras 30', move=False, align="left", font=("Arial", 10, "normal"))
t.backward(30)


'''
