import pygame,recursos

class lobo_enemigo(pygame.sprite.Sprite):
	def __init__(self,x,y,infx,infy):
		self.salud=40
		self.hpmax=40
		self.danio=10
		self.atacado=False
		self.murio=False
		self.oro=100
		self.exp=50
		self.sheet=recursos.lobosheet.convert_alpha()

		self.imagen1=pygame.Rect((0,0,51,36))
		self.imagen2=pygame.Rect((51,0,51,36))
		self.imagen3=pygame.Rect((97,0,51,36))
		self.imagen4=pygame.Rect((149,0,51,36))

		self.imagen5=pygame.Rect((0,45,51,36))
		self.imagen6=pygame.Rect((51,45,51,36))
		self.imagen7=pygame.Rect((97,45,51,36))
		self.imagen8=pygame.Rect((149,45,51,36))

		self.imagen9=pygame.Rect((0,90,18,26))
		self.imagen10=pygame.Rect((15,90,18,26))
		self.imagen11=pygame.Rect((48,90,18,26))
		self.imagen12=pygame.Rect((82,90,18,26))

		self.imagen13=pygame.Rect((0,135,18,26))
		self.imagen14=pygame.Rect((15,135,18,26))
		self.imagen15=pygame.Rect((48,135,18,26))
		self.imagen16=pygame.Rect((82,135,18,26))

		self.quietoxer=self.imagen1
		self.quietoxiz=self.imagen5
		self.quietoyab=self.imagen9
		self.quietoyar=self.imagen13


		self.imagenesxer=(self.imagen2,self.imagen3,self.imagen4)
		self.imagenesxiz=(self.imagen6,self.imagen7,self.imagen8)
		self.imagenesyab=(self.imagen10,self.imagen11,self.imagen12)
		self.imagenesyar=(self.imagen14,self.imagen15,self.imagen16)

		self.imagenes=[self.imagen1]
		self.imagenactual=0
		self.imagen=self.imagenes[self.imagenactual]


		self.rect=recursos.lobosheet.get_rect()
		self.rect.inflate_ip(infx,infy)#-----------------esto me da el rectangulo de la imagen
		self.rect.top,self.rect.left=(x,y)

		self.text1=str(self.salud)
		self.text2="/"
		self.text3=str(self.hpmax)
		self.fuente=pygame.font.Font(None,20)
		self.textosalud=self.fuente.render(self.text1+self.text2+self.text3,0,(255,255,255))

		self.semueve=False
		self.comienzo=True

	def mover(self,vx,vy):
		self.rect.move_ip(vx,vy)
		self.antx=self.rect.left
		self.anty=self.rect.top

	def quieto(self):

		self.rect.left=self.antx
		self.rect.top=self.anty

	def update(self,superficie,player,playerx,playery,tiempo):


		self.tem=tiempo
		self.vx=0
		self.vy=0
		self.mover(0,0)


		if 100<=self.rect.left<600 and 100<=self.rect.top<350:
			if self.rect.left!=playerx:
				self.vx=2
				self.mover(2,0)
			else:
				self.mover(0,0)
			if self.rect.top!=playery:
				
				self.vy=2
				self.mover(0,2)
			else:
				self.mover(0,0)

		if 100<=self.rect.left<600 and 350<=self.rect.top<1000:
			if self.rect.left!=playerx:
				self.vx=2
				self.mover(2,0)
			else:
				self.mover(0,0)
			if self.rect.top!=playery:
				
				self.vy=-2
				self.mover(0,-2)
			else:
				self.mover(0,0)

		if 600<=self.rect.left<1000 and 100<=self.rect.top<350:
			if self.rect.left!=playerx:
				self.vx=-2
				self.mover(-2,0)
			else:
				self.mover(0,0)
			if self.rect.top!=playery:
				
				self.vy=2
				self.mover(0,2)
			else:
				self.mover(0,0)

		if 600<=self.rect.left<1000 and 350<=self.rect.top<1000:
			if self.rect.left!=playerx:
				self.vx=-2
				self.mover(-2,0)
			else:
				self.mover(0,0)
			if self.rect.top!=playery:
				
				self.vy=-2
				self.mover(0,-2)
			else:
				self.mover(0,0)

		if self.comienzo and self.semueve==False:
			superficie.blit(self.sheet.subsurface(self.imagen1),self.rect)#--------------primera imagen al comienzo
		else:
			self.comienzo=False

		if (self.vx,self.vy)==(0,0):self.semueve=False#--------------------sin velocidad no se mueve
		else:self.semueve=True

		if self.vx>0:
			self.imagenes=self.imagenesxer#---------------------esto define que lista de imagenes usar segun orientacion
		if self.vx<0:
			self.imagenes=self.imagenesxiz
		if self.vy>0:
			self.imagenes=self.imagenesyab
		if self.vy<0:
			self.imagenes=self.imagenesyar

		if self.semueve==False:#-----------------------------esto dibuja cuando no se esta moviendo pero se movio antes
			if self.imagenes==self.imagenesxer:
				superficie.blit(self.sheet.subsurface(self.imagen1),self.rect)
			if self.imagenes==self.imagenesxiz:
				superficie.blit(self.sheet.subsurface(self.imagen6),self.rect)
			if self.imagenes==self.imagenesyab:
				superficie.blit(self.sheet.subsurface(self.imagen11),self.rect)
			if self.imagenes==self.imagenesyar:
				superficie.blit(self.sheet.subsurface(self.imagen14),self.rect)

		if self.semueve:
			self.nextimagen() #llamo al bucle

		if self.semueve==True:
			superficie.blit(self.sheet.subsurface(self.imagenes[self.imagenactual]),self.rect)

		
		if self.salud<=0:
			self.murio=True


	def nextimagen(self): #bucle que determina cual imagen corresponde segun iteracion.
		cont=2

		if cont==self.tem:
			self.imagenactual+=1

		if self.imagenactual>(len(self.imagenes)-1):
			self.imagenactual=0


class oso_enemigo(lobo_enemigo):
	def __init__(self,x,y,infx,infy):
		self.salud=100
		self.hpmax=100
		self.danio=10
		self.atacado=False
		self.murio=False
		self.oro=100
		self.exp=50
		self.sheet=recursos.ososheet.convert_alpha()

		self.imagen1=pygame.Rect((3,10,60,39))
		self.imagen2=pygame.Rect((75,10,60,39))
		self.imagen3=pygame.Rect((145,10,60,39))
		self.imagen4=pygame.Rect((205,10,60,39))

		self.imagen5=pygame.Rect((3,65,60,39))
		self.imagen6=pygame.Rect((75,65,60,39))
		self.imagen7=pygame.Rect((145,65,60,39))
		self.imagen8=pygame.Rect((205,65,60,39))

		self.imagen9=pygame.Rect((0,180,49,70))
		self.imagen10=pygame.Rect((50,180,49,70))
		self.imagen11=pygame.Rect((101,180,49,70))
		self.imagen12=pygame.Rect((151,180,49,70))

		self.imagen13=pygame.Rect((0,115,49,50))
		self.imagen14=pygame.Rect((50,115,49,50))
		self.imagen15=pygame.Rect((101,115,49,50))
		self.imagen16=pygame.Rect((151,115,49,50))

		self.quietoxer=self.imagen1
		self.quietoxiz=self.imagen5
		self.quietoyab=self.imagen9
		self.quietoyar=self.imagen13


		self.imagenesxer=(self.imagen2,self.imagen3,self.imagen4)
		self.imagenesxiz=(self.imagen6,self.imagen7,self.imagen8)
		self.imagenesyab=(self.imagen10,self.imagen11,self.imagen12)
		self.imagenesyar=(self.imagen14,self.imagen15,self.imagen16)

		self.imagenes=[self.imagen1]
		self.imagenactual=0
		self.imagen=self.imagenes[self.imagenactual]


		self.rect=recursos.lobosheet.get_rect()
		self.rect.inflate_ip(infx,infy)#-----------------esto me da el rectangulo de la imagen
		self.rect.top,self.rect.left=(x,y)

		self.text1=str(self.salud)
		self.text2="/"
		self.text3=str(self.hpmax)
		self.fuente=pygame.font.Font(None,20)
		self.textosalud=self.fuente.render(self.text1+self.text2+self.text3,0,(255,255,255))

		self.semueve=False
		self.comienzo=True
