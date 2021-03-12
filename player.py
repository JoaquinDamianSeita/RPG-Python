import pygame,recursos,lvl

class player(pygame.sprite.Sprite):

	def __init__(self,x,y):

		self.salud=100
		self.hpmax=100
		self.mana=300
		self.manamax=300
		self.nivel=1
		self.oro=0
		self.exp=0
		self.expmax=lvl.lvls[self.nivel]
		self.ataque=30
		self.defensa=0
		self.murio=False
		self.nombre="Jugador1"

		self.xreal=0
		self.yreal=0


		self.sheet =recursos.plantillamodelo.convert_alpha() #imagen maestra

		self.imagen1=pygame.Rect((0,174,25,53))#-----------------------defino rectangulos de la imagen maestra
		self.imagen2=pygame.Rect((25,174,25,53))
		self.imagen3=pygame.Rect((50,174,25,53))
		self.imagen4=pygame.Rect((75,174,25,53))
		self.imagen5=pygame.Rect((100,174,25,53))

		self.imagen6=pygame.Rect((0,118,25,58))
		self.imagen7=pygame.Rect((25,118,25,58))
		self.imagen8=pygame.Rect((50,118,25,58))
		self.imagen9=pygame.Rect((75,118,25,58))
		self.imagen10=pygame.Rect((100,118,25,58))

		self.imagen11=pygame.Rect((0,0,25,58))
		self.imagen12=pygame.Rect((50,0,25,58))
		self.imagen13=pygame.Rect((125,0,25,58))

		self.imagen14=pygame.Rect((0,58,25,58))
		self.imagen15=pygame.Rect((25,58,25,58))
		self.imagen16=pygame.Rect((100,58,25,58))


		self.imagenes=[self.imagen11]#--------------------primera imagen en aparecer


		self.imagenesxdq=self.imagen1#----------------------imagenes quieto
		self.imagenesxiq=self.imagen6
		self.imagenesyabq=self.imagen11
		self.imagenesyarq=self.imagen14

		self.imagenesxd=(self.imagen2,self.imagen3,self.imagen4,self.imagen5)#----------------imagenes moviendose
		self.imagenesxi=(self.imagen7,self.imagen8,self.imagen9,self.imagen10)
		self.imagenesyab=(self.imagen12,self.imagen13)
		self.imagenesyar=(self.imagen15,self.imagen16)

		self.imagen_actual=0        #--------------------el numero que dice cual imagen mostrar

		self.imagen=self.imagenes[self.imagen_actual]#la imagen que va a mostrar


		self.rect=self.sheet.get_rect()
		self.rect.inflate_ip(-150,-170)#-----------------esto me da el rectangulo de la imagen
		self.rect.top,self.rect.left=(x,y)

		self.text1=str(self.salud)
		self.text2="/"
		self.text3=str(self.hpmax)
		self.fuente=pygame.font.Font(None,15)
		self.fuente1=pygame.font.Font(None,25)
		self.fuente2=pygame.font.Font(None,20)
		self.textosalud=self.fuente.render(self.text1+self.text2+self.text3,0,(255,255,255))
		self.textonombre=self.fuente2.render(self.nombre,0,(255,255,255))


		self.semueve=False
		self.comienzo=True
		self.velocidad=1
		self.vx=0
		self.vy=0

	def mover(self,vx,vy):
		self.rect.move_ip(vx,vy)

	def update(self,superficie,tiempo,xf,yf,abajo,arriba,derecha,izquierda):

		self.abajo,self.arriba,self.derecha,self.izquierda=abajo,arriba,derecha,izquierda

		if self.abajo==True:
			self.vy=self.velocidad
		if self.arriba==True:
			self.vy=-self.velocidad
		if self.derecha==True:
			self.vx=self.velocidad
		if self.izquierda==True:
			self.vx=-self.velocidad


		if self.abajo==False:
			if self.arriba:self.vy-=self.velocidad
			else:self.vy=0
		if self.arriba==False:
			if self.abajo:self.vy=self.velocidad
			else:self.vy=0
		if self.derecha==False:
			if self.izquierda:self.vx-=self.velocidad
			else:self.vx=0
		if self.izquierda==False:
			if self.derecha:self.vx=self.velocidad
			else:self.vx=0

		self.xreal=xf
		self.yreal=yf

		print(self.rect.left,self.rect.top)

		self.tem=tiempo
		superficie.blit(self.textonombre,(585,405))

		if self.exp==self.expmax:
			self.nivel=self.nivel+1
			self.exp=0
			self.expmax=lvl.lvls[self.nivel]

		self.text4=str(self.oro)
		self.text6=str(self.nivel)

		self.text5=str(self.exp)
		self.text7=str(self.expmax)

		self.text8=str(self.mana)
		self.text9=str(self.manamax)

		self.textooro=self.fuente1.render(self.text4,0,(255,255,255))
		self.textolvl=self.fuente1.render(self.text6,0,(255,255,255))
		self.textoexp=self.fuente.render(self.text5+self.text2+self.text7,0,(255,255,255))
		self.textomana=self.fuente.render(self.text8+self.text2+self.text9,0,(255,255,255))

		if self.comienzo and self.semueve==False:
			superficie.blit(self.sheet.subsurface(self.imagen11),self.rect)#--------------primera imagen al comienzo
		else:
			self.comienzo=False
		

		if (self.vx,self.vy)==(0,0):self.semueve=False#--------------------sin velocidad no se mueve
		else:self.semueve=True


		if self.vx>0:
			self.imagenes=self.imagenesxd#---------------------esto define que lista de imagenes usar segun orientacion
		if self.vx<0:
			self.imagenes=self.imagenesxi
		if self.vy>0:
			self.imagenes=self.imagenesyab
		if self.vy<0:
			self.imagenes=self.imagenesyar

		if self.semueve==False:#-----------------------------esto dibuja cuando no se esta moviendo pero se movio antes
			if self.imagenes==self.imagenesxd:
				superficie.blit(self.sheet.subsurface(self.imagen1),self.rect)
			if self.imagenes==self.imagenesxi:
				superficie.blit(self.sheet.subsurface(self.imagen6),self.rect)
			if self.imagenes==self.imagenesyab:
				superficie.blit(self.sheet.subsurface(self.imagen11),self.rect)
			if self.imagenes==self.imagenesyar:
				superficie.blit(self.sheet.subsurface(self.imagen14),self.rect)

		if self.semueve:
			self.nextimagen() #llamo al bucle
			

		self.mover(self.vx,self.vy) #-------------------para que el fondo se mueva no el chaboncito



		#self.imagen=self.imagenes[self.imagen_actual] #-----define que imagen va a ser igual a dentro de la lista
		#--que este de turno la que le toque segun indice imagen_actual

		if self.semueve==True:
			superficie.blit(self.sheet.subsurface(self.imagenes[self.imagen_actual]),self.rect) #esto dibuja todas las
		#-----imagenes con su rectangulo en la pantalla cuando se mueve

		if self.salud<=0:
			self.murio=True

		if self.murio==True:
			pass



	def nextimagen(self): #bucle que determina cual imagen corresponde segun iteracion.
		cont=2

		if cont==self.tem:
			self.imagen_actual+=1

		if self.imagen_actual>(len(self.imagenes)-1):
			self.imagen_actual=0