from turtle import Turtle,Screen
import pickle
import random


class Tablero():

	totalCeldas=0
	coords={}#{1:[(),(),(),()],2:(),(),(),()}
	coordsSimple={}#{(x,y):(f,c),(x,y):(f,c)}
	celdaOcupadaTablero=[]#Almacena las celdas ocupadas entre todos los jugadores en el tablero
	save_drawing=[]

	def __init__(
		self,lienzo,color='black',full=True,
		ancho_pantalla=810,alto_pantalla=430,
		visible=True,
		filas=3,celdas=3,
		alto_celda=20,ancho_celda=20,
		ejes=False,
		celdas_numeradas=False):


		self.widthScreen=ancho_pantalla
		self.heightScreen=alto_pantalla
		self.visible=visible
		self.alto=filas
		self.ancho=celdas
		self.alto_celda=alto_celda
		self.ancho_celda=ancho_celda


		self.t=Turtle()
		self.t.color(color)
		self.t.hideturtle()

		self.screen=Screen()
		self.screen.setup(self.widthScreen,self.heightScreen)
		self.screen.tracer(0,0)
		self.screen.delay(0)

		self.malla(full=True)
	
		if celdas_numeradas==True:
			self.celdasNumeradas()

		self.paleta()
		self.lienzo(color=lienzo)

		if ejes==True:
			self.ejes()


############################################################################################		
		
	def go(self,x,y,down=True):
		self.t.up()
		self.t.goto(x,y)
		if down:
			self.t.down()


############################################################################################		

	def malla(self,x=0,y=0,full=False):

		"""
		Dibuja la cuadricula base. Si full=True la fila 1 comienza en la esquina sup iz
		de screen.
		Crea lista de coordenadas
		self.coords={FILA_1:(x,y),FILA_2:(x,y)}
		self.coordsSimple={(x,y):(1,2)}

		"""
		if full:
			x=self.widthScreen/-2
			y=self.heightScreen/2
			self.ancho=int(self.widthScreen/self.ancho_celda)
			self.alto=int(self.heightScreen/self.alto_celda)

		self.go(x,y)#Va al punto de inicio, primera fila, primera celda
		
	
				
		for k in range(0,self.alto):
			# c calcula la coordenada de Y basada en la altura de la celda*fila
			c=(-k*self.alto_celda)+y

			self.go(x,c,down=self.visible)
			
			self.coords[k+1]=[]

			for i in range(1,self.ancho+1):
				self.celda(self.ancho_celda,self.alto_celda)
				#guardamos las coordenadas para cada celda
				#calcula el punto central de la celda basado en el ancho y alto de cada celda/2
				xCor=((self.ancho_celda*i)+x)-(self.ancho_celda/2)
				yCor=c-(self.alto_celda/2)
				
				self.coords[k+1].append( (xCor,yCor) )
				self.coordsSimple[(xCor,yCor)]=(k+1,i)
	
				self.go((self.ancho_celda*i)+x,c,down=self.visible)
				
				


	def celda(self,ancho,alto):
		angulo=360
		self.totalCeldas+=1#Lleva la cuenta de celdas dibujadas/veces llamado

		for i in range(1,5):
			angulo-=90
			if i%2 != 0:
				self.t.forward(ancho)
				self.t.seth(angulo)
			else:
				self.t.forward(alto)
				self.t.seth(angulo)
			

############################################################################################
	def onclick(self):
		
		self.screen.onclick(lambda x, y: self.gestion(x,y))

############################################################################################

	def gestion(self,xClick,yClick):
		
		#Obtiene la coordenada central de la celda
		coordenadas_celda=self.getCelCoords(xClick,yClick)
	
		#Obtiene la coordenada simple(1,1) de esa celda
		coordenadas_celda_simple=self.coordsSimple[coordenadas_celda]

		

		#print('coordenada completa ',coordenadas_celda)
		print('coordenada simple ',coordenadas_celda_simple)
		color='green'


		
		if coordenadas_celda_simple[0] >=3 and coordenadas_celda_simple[0] <=19	and coordenadas_celda_simple[1] >= 3 and coordenadas_celda_simple[1] <=38:
			self.celdaOcupadaTablero.append( (coordenadas_celda_simple[0],coordenadas_celda_simple[1],self.color) )
			self.relleno(coordenadas_celda)
		else:

			if coordenadas_celda_simple==(2,7):
				
				self.color='red'

			elif coordenadas_celda_simple==(2,9):
				
				self.color='blue'

			elif coordenadas_celda_simple==(2,11):
				self.color='green'

			elif coordenadas_celda_simple==(2,13):
				self.color='yellow'

			elif coordenadas_celda_simple==(2,15):
				self.color='grey'

			elif coordenadas_celda_simple==(2,17):
				self.color='purple'

			elif coordenadas_celda_simple==(20,5):#DELETE
				print('delete')
				self.lienzo(color='beige')
				self.celdaOcupadaTablero=[]

			elif coordenadas_celda_simple==(20,9):#SAVE
				print('save')
				file_name=self.screen.textinput('Save','Title:')
				
				outfile = open(file_name,'wb')
				pickle.dump(self.celdaOcupadaTablero,outfile)
				outfile.close()

			elif coordenadas_celda_simple==(20,13):#LOAD
				print('load')
				file_name=self.screen.textinput('Load','Title:')

				try:
					infile = open(file_name,'rb')
					drawing= pickle.load(infile)
					infile.close()
					self.setDrawing(drawing)
					self.loadDrawing()
				except:
					print('Nombre no válido')

				
			

		#print(self.celdaOcupadaTablero)



############################################################################################

	def getCoordsbySimple(self,f=0,c=0):
		for i in self.coordsSimple.items():
			if i[1]==(f,c):
				return i[0]


############################################################################################


	def getCelCoords(self,xClick,yClick):
		#devuelve las coordenadas de la celda respecto a las coordenadas del click
		#dicho de otra forma. Recibe las coordenadas del click y devuelve las coordenadas
		# de la celda
		for key in self.coords.keys():
			count=1
			for celda in self.coords[key]:
				x=celda[0]
				y=celda[1]
				"""
				Calcula las cordenadas centrales de cada lado de la celda
				Luego compara las coordenadas del click y comprueba si están 
				dentro de los extremos
				"""
				maxX=x+(self.ancho_celda/2)
				minX=x-(self.ancho_celda/2)
				maxY=y+(self.alto_celda/2)
				minY=y-(self.alto_celda/2)
				r=0
				if xClick < maxX and xClick > minX:
					r+=1
				if yClick < maxY and yClick > minY:
					r+=1

					if r==2:
						return (x,y)
					else:
						count+=1

############################################################################################

	def lienzo(self,color='grey'):
		self.color=color

		for fila in self.coords.keys():
			count=0
			if fila>2 and fila< len(self.coords.keys())-1:
				for celda in self.coords[fila]:
					
					if count< len(self.coords[fila])-2 and count > 1:
						self.relleno(celda)

					count+=1

		self.color='blue'

##########################################################################################

	def compruebaCeldaOcupada(self,celda=()):
		""" 
		Devuelve cierto! si la celda=(x,y) se encuentra en el atributo de clase self.celdaOcupada
		"""
		
		if celda in self.celdaOcupadaTablero:
			return True
		else:
			return False
############################################################################################

	def ejes(self,separacion=50):
		"""
		Dibuja ejes cartesianos de referencia
		"""
		self.t.color('black')
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

############################################################################################

	def celdasNumeradas(self):
		"""
		Muestra el numero de fila y celda en cada cuadro
		"""
		for coords in self.coordsSimple.keys():
			self.go(coords[0],coords[1])
			self.t.write(self.coordsSimple[coords])
		
############################################################################################


	def relleno(self,coordenadas):
	
		self.go(coordenadas[0],coordenadas[1]-(self.alto_celda/2))

		self.t.begin_fill()
		
		self.t.color(self.color)

		self.t.forward(self.ancho_celda/2)
		self.t.seth(90)
		self.t.forward(self.alto_celda)

		self.t.seth(180)
		self.t.forward(self.ancho_celda)

		self.t.seth(270)
		self.t.forward(self.alto_celda)

		self.t.seth(0)
		self.t.forward(self.ancho_celda)


		self.t.end_fill()

				
############################################################################################

	def paleta(self):

		choose=self.coords[2][1]
		self.go(x=choose[0],y=choose[1]-5)
		self.t.write('Choose a colour')

		#DELETE
		choose=self.coords[20][1]
		self.go(x=choose[0],y=choose[1]-5)
		self.t.write('Delete')

		self.color='black'
		button_delete=self.coords[20][4]
		self.relleno(button_delete)
		##################

		#SAVE
		choose=self.coords[20][6]
		self.go(x=choose[0],y=choose[1]-5)
		self.t.write('Save')

		self.color='black'
		button_save=self.coords[20][8]
		self.relleno(button_save)
		##################

		#LOAD
		choose=self.coords[20][10]
		self.go(x=choose[0],y=choose[1]-5)
		self.t.write('Load')

		self.color='black'
		button_save=self.coords[20][12]
		self.relleno(button_save)
		##################

		
		self.color='red'
		rojo=self.coords[2][6]
		self.relleno(rojo)

		self.color='blue'
		azul=self.coords[2][8]
		self.relleno(azul)

		self.color='green'
		verde=self.coords[2][10]
		self.relleno(verde)

		self.color='yellow'
		amarillo=self.coords[2][12]
		self.relleno(amarillo)

		self.color='grey'
		gris=self.coords[2][14]
		self.relleno(gris)

		self.color='purple'
		morado=self.coords[2][16]
		self.relleno(morado)


############################################################################################


	def loadDrawing(self):
		lista=self.celdaOcupadaTablero
		for celda in lista:
			self.color=celda[2]
			self.relleno(self.getCoordsbySimple(f=celda[0],c=celda[1]))


############################################################################################

	def setDrawing(self,lista):
		for celda in lista:
			self.celdaOcupadaTablero.append(celda)



