from turtle import Turtle
import random


class Tortuga():
	#Bob ahora sabe cuanto mide el lienzo
	widthScreen=0
	heightScreen=0
	maxX=0
	maxY=0
	level=0
	memo=[]
	coords=0




###############################################################################################

	def __init__(self,color='red',visibility=False,shape='turtle',size=1,pantalla=[500,500],speed=1):
		t=Turtle()
		t.color(color)
		t.pensize(size)
		#t.speed(speed)
		self.widthScreen=pantalla[0]
		self.heightScreen=pantalla[1]
		self.maxX=self.widthScreen/2
		self.maxY=self.heightScreen/2

		if speed==1:
			t.speed(0)

		if visibility==False:
			t.hideturtle()
		else:
			t.shape(shape)
		
		#Crea a bob con el color y demas opciones
		self.t=t

###############################################################################################
	def go(self,x,y):
		self.t.up()
		self.t.goto(x,y)
		self.t.down()

###############################################################################################

	def celda(self,ancho,alto):
		angulo=360

		for i in range(1,5):
			angulo-=90
			if i%2 != 0:
				self.t.forward(ancho)
				self.t.seth(angulo)
			else:
				self.t.forward(alto)
				self.t.seth(angulo)
			

###############################################################################################

	def cuadricula(self,ancho,alto,x=0,y=0):
		#self.t.speed(0)
		ancho_celda=25
		alto_celda=25
		self.coords={}

		#ejemplo 	coords={(-50,14):((-51,56),(45,67),(45,67)),}

		self.go(x,y)

				
		for k in range(0,alto):
			c=(-k*alto_celda)+y

			self.t.goto(x,c)
			self.t.down()

			self.coords[x,c]=[]

			for i in range(1,ancho+1):
				self.celda(ancho_celda,alto_celda)

				#guardamos las coordenadas para cada celda
				
				self.coords[x,c].append(( ((ancho_celda*i)+x)-(ancho_celda/2) ,c-(alto_celda/2)   ))


				self.t.goto((ancho_celda*i)+x,c)
			self.t.up()


	
			


###############################################################################################

	def skyStarts(self):
		self.t.speed(1000)

		for i in range(10000):
			x=random.randint(-self.maxX,self.maxX)
			y=random.randrange(-self.maxY,self.maxY)

			self.t.up()
			self.t.goto(x,y)
			self.t.down()

			self.t.circle(5)




###############################################################################################

	def avance(self):
		self.t.speed(0)
		for i in range(10000):
			self.t.forward(1)
			#print(self.t.position()[0])
			if self.t.position()[0] > self.maxX-5:
				self.t.seth(90)
			if self.t.position()[1] > self.maxY-5:
				self.t.seth(180)

			if self.t.position()[0] < -self.maxX:
				self.t.seth(270)

			if self.t.position()[1] < -self.maxY:
				self.t.seth(0)



###############################################################################################



	def BorderScreen(self):

		self.t.up()
		self.t.goto(self.widthScreen/2,self.heightScreen/2)
		self.t.down()

		self.t.seth(180)
		self.t.forward(self.widthScreen)
		self.t.seth(270)
		self.t.forward(self.heightScreen)
		self.t.seth(0)
		self.t.forward(self.widthScreen)
		self.t.seth(90)
		self.t.forward(self.heightScreen)





###############################################################################################
	def ejes(self,separacion=25):
		self.go(self.widthScreen/-2,0)
		self.t.forward(self.widthScreen)

		self.go(0,self.heightScreen/2)
		self.t.seth(270)
		self.t.forward(self.heightScreen)

		for i in range(0,4):
			self.go(0,0)
			self.t.seth(90*i)

			if i==0 or i==1:
				if i==0:
					for i in range(1,int( (self.widthScreen/2) / separacion )):
						self.t.forward(separacion)
						self.t.write('+'+str(separacion*i),font=("Arial", 5, "normal"))
				else:
					for i in range(1,int( (self.heightScreen/2) / separacion )):
						self.t.forward(separacion)
						self.t.write('+'+str(separacion*i),font=("Arial", 5, "normal"))
			else:
				if i==2:
					for i in range(1,int( (self.widthScreen/2) /separacion )):
						self.t.forward(separacion)
						self.t.write('-'+str(separacion*i),font=("Arial", 5, "normal"))
				else:
					for i in range(1,int( (self.heightScreen/2)/separacion )):
						self.t.forward(separacion)
						self.t.write('-'+str(separacion*i),font=("Arial", 5, "normal"))

		self.go(0,0)
		self.t.seth(0)
		
	
###############################################################################################

	def equis(self,x=0,y=0):
		angulo=45
		
		self.go(x,y)
		for i in range(1,5):
			self.t.seth(angulo)
			self.t.forward(5)
			self.t.goto(x,y)
			angulo+=90







###############################################################################################






###############################################################################################