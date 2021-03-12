import recursos,pygame


class ataque_apoka(pygame.sprite.Sprite):
	def __init__(self):
		self.imagenbase=recursos.apoka.convert_alpha()

		self.imagen1=pygame.Rect(13,44,32,38)
		self.imagen2=pygame.Rect(100,26,51,57)
		self.imagen3=pygame.Rect(207,17,57,69)
		self.imagen4=pygame.Rect(320,14,55,70)
		self.imagen5=pygame.Rect(433,15,51,69)

		self.listaimagenes=[self.imagen1,self.imagen2,self.imagen3,self.imagen4,self.imagen5]
		self.rect=self.imagenbase.get_rect()
		self.rect.top,self.rect.left=pygame.mouse.get_pos()

	def update(self,superfice):
		pass


class ataque_melee(pygame.sprite.Sprite):
	def __init__(self):

		self.pego=False
		
		self.imagenbase=recursos.auraataque.convert()

		self.imagenar=pygame.Rect((53,77,65,17))
		self.imagenab=pygame.Rect((53,134,65,17))
		self.imagender=pygame.Rect((104,95,18,37))
		self.imageniz=pygame.Rect((54,95,18,37))
		self.imagenturno=self.imagenar

		self.rect=self.imagenbase.get_rect()
		self.rect.top,self.rect.left=(350,600)

		self.imagenespada1=recursos.espadaataque1.convert()
		self.imagenespada2=recursos.espadaataque2.convert()
		self.imagenespada3=recursos.espadaataque3.convert()
		self.imagenespada4=recursos.espadaataque4.convert()
		self.rect1=self.imagenespada1.get_rect()
		self.rect1.top,self.rect1.left=(300,600)

		self.rect2=self.imagenespada2.get_rect()
		self.rect2.top,self.rect2.left=(365,640)

		self.rect3=self.imagenespada3.get_rect()
		self.rect3.top,self.rect3.left=(410,600)

		self.rect4=self.imagenespada4.get_rect()
		self.rect4.top,self.rect4.left=(365,540)


	def update(self,superficie,vx,vy,click,lista_enemigos,jugador,intervalo):
		self.inter=intervalo
		if vy<0:
			superficie.blit(self.imagenespada1,self.rect1)
			self.imagenturno=self.imagenar
			superficie.blit(self.imagenbase.subsurface(self.imagenturno),(578,345))
		if vy>0:
			superficie.blit(self.imagenespada3,self.rect3)
			self.imagenturno=self.imagenab
			superficie.blit(self.imagenbase.subsurface(self.imagenturno),(578,397))
		if vx<0:
			superficie.blit(self.imagenespada4,self.rect4)
			self.imagenturno=self.imageniz
			superficie.blit(self.imagenbase.subsurface(self.imagenturno),(580,360))
		if vx>0:
			superficie.blit(self.imagenespada2,self.rect2)
			self.imagenturno=self.imagender
			superficie.blit(self.imagenbase.subsurface(self.imagenturno),(628,360))

			#def empuje():
				#for i in lista_enemigos:
					#if i.vx>0:
						#i.vx=-10
						#i.rect.move_ip(-10,i.vy)
					#if i.vx<0:
						#i.vx=10
						#i.rect.move_ip(10,i.vy)
					#if i.vy<0:
						#i.vy=-10
						#i.rect.move_ip(i.vx,-10)
					#if i.vy>0:
						#i.vy=10
						#i.rect.move_ip(i.vx,10)

		if click==True and intervalo==40:
			for i in lista_enemigos:
				if self.rect1.colliderect(i.rect):
					i.salud=i.salud-jugador.ataque
					i.text1=str(i.salud)
					i.text2="/"
					i.text3=str(i.hpmax)
					i.fuente=pygame.font.Font(None,20)
					i.textosalud=i.fuente.render(i.text1+i.text2+i.text3,0,(255,255,255))
					i.atacado=True
					i.mover(10,10)
				else:i.atacado=False


				if self.rect2.colliderect(i.rect):
					i.salud=i.salud-jugador.ataque
					i.text1=str(i.salud)
					i.text2="/"
					i.text3=str(i.hpmax)
					i.fuente=pygame.font.Font(None,20)
					i.textosalud=i.fuente.render(i.text1+i.text2+i.text3,0,(255,255,255))
					i.atacado=True
					i.quieto()
				else:i.atacado=False

			

				if self.rect3.colliderect(i.rect):
					i.salud=i.salud-jugador.ataque
					i.text1=str(i.salud)
					i.text2="/"
					i.text3=str(i.hpmax)
					i.fuente=pygame.font.Font(None,20)
					i.textosalud=i.fuente.render(i.text1+i.text2+i.text3,0,(255,255,255))
					i.atacado=True
					i.quieto()
				else:i.atacado=False
				

				if self.rect4.colliderect(i.rect):
					i.salud=i.salud-jugador.ataque
					i.text1=str(i.salud)
					i.text2="/"
					i.text3=str(i.hpmax)
					i.fuente=pygame.font.Font(None,20)
					i.textosalud=i.fuente.render(i.text1+i.text2+i.text3,0,(255,255,255))
					i.atacado=True
					i.quieto()
				else:i.atacado=False

					#i.vx=-i.vx*4
					#i.vy=-i.vy*4
					#i.rect.move_ip(i.vx,i.vy)