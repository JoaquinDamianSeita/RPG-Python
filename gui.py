import pygame
import recursos
import items


class boton(pygame.sprite.Sprite):
	def __init__(self,imagen1,imagen2,x,y):
		self.boton1=imagen1
		self.boton2=imagen2
		self.boton_actual=self.boton1
		self.rect=self.boton_actual.get_rect()
		self.rect.left,self.rect.top=(x,y)
		self.T=0

	def update(self,pantalla,cursor):
		if cursor.colliderect(self.rect):
			self.boton_actual=self.boton1
		else:
			self.boton_actual=self.boton2

		pantalla.blit(self.boton_actual,self.rect)

	def click(self,pantalla,cursor):
		if cursor.colliderect(self.rect):
			self.boton_actual=self.boton1
		else:
			self.boton_actual=self.boton2

		pantalla.blit(self.boton_actual,self.rect)


class boton_menu_circulo(pygame.sprite.Sprite):
	def __init__(self,imagen1,imagen2,x,y,t):
		self.boton1=imagen1
		self.boton2=imagen2
		self.boton_actual=self.boton1
		self.rect=self.boton2.get_rect()
		self.rect.left,self.rect.top=(x,y)
		if t==1:
			self.rect1=self.boton1.get_rect()
			self.xg=x-89
			self.yg=y-90
			self.rect1.left,self.rect1.top=(self.xg,self.yg)
		if t==2:
			self.rect1=self.boton1.get_rect()
			self.xg=x
			self.yg=y-90
			self.rect1.left,self.rect1.top=(self.xg,self.yg)
		if t==3:
			self.rect1=self.boton1.get_rect()
			self.xg=x
			self.yg=y
			self.rect1.left,self.rect1.top=(self.xg,self.yg)
		if t==4:
			self.rect1=self.boton1.get_rect()
			self.xg=x-89
			self.yg=y
			self.rect1.left,self.rect1.top=(self.xg,self.yg)

	def update(self,pantalla,cursor):
		if cursor.colliderect(self.rect):
			self.boton_actual=self.boton1
		else:
			self.boton_actual=self.boton2
		if self.boton_actual==self.boton2:
			pantalla.blit(self.boton_actual,self.rect)
		if self.boton_actual==self.boton1:
			pantalla.blit(self.boton_actual,self.rect1)

class boton_lanzar(boton):
	def update(self,pantalla,cursor):
		global lanzar
		lanzar=False
		if cursor.colliderect(self.rect) and pygame.mouse.get_pressed()[0]:
			self.boton_actual=self.boton1
			lanzar=True
			self.T=1
		else:
			self.boton_actual=self.boton2
			self.T=0

		pantalla.blit(self.boton_actual,self.rect)

class boton_apoka(pygame.sprite.Sprite):
	def __init__(self,imagen1,imagen2,x,y):
		self.boton1=imagen1
		self.boton2=imagen2
		self.boton_actual=[self.boton1,self.boton2]
		self.rect=self.boton_actual[0].get_rect()
		self.rect.left,self.rect.top=(x,y)
		self.T=0
		global apoka_selec

		apoka_selec=False

	def update(self,pantalla,cursor):
		global apoka_selec

		if cursor.colliderect(self.rect) and pygame.mouse.get_pressed()[2]:
				self.T=1
				apoka_selec=True

		if cursor.colliderect(self.rect):
		 	if pygame.mouse.get_pressed()[0]:
		 		self.T=0
		 		apoka_selec=False
		 		
		pantalla.blit(self.boton_actual[self.T],self.rect)

class menu_hechizos(pygame.sprite.Sprite):
	def __init__(self,imagen,x,y):
		self.menu=imagen
		self.rect=self.menu.get_rect()
		self.rect.left,self.rect.top=(x,y)
		self.lanz1=recursos.botlan1.convert()
		self.lanz2=recursos.botlan2.convert()
		self.bot_lan=boton_lanzar(self.lanz1,self.lanz2,811,460)

		self.info1=recursos.botinfo1.convert()
		self.info2=recursos.botinfo2.convert()
		self.bot_info=boton(self.info1,self.info2,1128,460)

		self.apok1=recursos.botapoka1.convert()
		self.apok2=recursos.botapoka2.convert()
		self.bot_apok=boton_apoka(self.apok1,self.apok2,811,510)

		self.cer1=recursos.cerraricono1
		self.cer2=recursos.cerraricono2
		self.bot_cer=boton_lanzar(self.cer1,self.cer2,1180,430)

	def update(self,pantalla,cursor,valida):
		pantalla.blit(self.menu,self.rect)
		if valida==True:
			self.bot_lan.update(pantalla,cursor)
			self.bot_info.update(pantalla,cursor)
			self.bot_apok.update(pantalla,cursor)
			self.bot_cer.update(pantalla,cursor)

class interfaz_usuario(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.menu=recursos.interfazusuario
		self.rect=self.menu.get_rect()
		self.rect.left,self.rect.top=(x,y)
	def update(self,pantalla):
		pantalla.blit(self.menu,self.rect)

class inventario(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.menu=recursos.inventariomodelo
		self.rect=self.menu.get_rect()
		self.rect.left,self.rect.top=(x,y)

		self.cer1=recursos.cerraricono1
		self.cer2=recursos.cerraricono2
		self.bot_cer=boton_lanzar(self.cer1,self.cer2,120,180)
	def update(self,pantalla,cursor):
		pantalla.blit(self.menu,self.rect)
		self.bot_cer.update(pantalla,cursor)

class equipamento(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.imagenmain=recursos.equipocuadro
		self.menu=self.imagenmain.convert()
		self.rect=self.menu.get_rect()
		self.rect.left,self.rect.top=(x,y)
	def update(self,pantalla):
		pantalla.blit(self.menu,self.rect)

class menu_circulo(pygame.sprite.Sprite):
	def __init__(self):
		self.b1=recursos.menucirculo1
		self.bg1=recursos.menucirculog1
		self.b2=recursos.menucirculo2
		self.bg2=recursos.menucirculog2
		self.b3=recursos.menucirculo3
		self.bg3=recursos.menucirculog3
		self.b4=recursos.menucirculo4
		self.bg4=recursos.menucirculog4

		self.boton1=boton_menu_circulo(self.bg1,self.b1,400,200,1)
		self.boton2=boton_menu_circulo(self.bg2,self.b2,578,200,2)
		self.boton3=boton_menu_circulo(self.bg3,self.b3,578,380,3)
		self.boton4=boton_menu_circulo(self.bg4,self.b4,400,380,4)
	def update(self,pantalla,cursor):
		self.boton1.update(pantalla,cursor)
		self.boton2.update(pantalla,cursor)
		self.boton3.update(pantalla,cursor)
		self.boton4.update(pantalla,cursor)


class barras_estado(pygame.sprite.Sprite):
	def __init__(self,imagen,x,y):
		self.menu=imagen

		self.imagen1=pygame.Rect((0,0,17,16))
		self.imagen2=pygame.Rect((0,0,27,16))
		self.imagen3=pygame.Rect((0,0,37,16))
		self.imagen3=pygame.Rect((0,0,47,16))
		self.imagen4=pygame.Rect((0,0,57,16))
		self.imagen5=pygame.Rect((0,0,67,16))
		self.imagen6=pygame.Rect((0,0,77,16))
		self.imagen7=pygame.Rect((0,0,87,16))
		self.imagen8=pygame.Rect((0,0,97,16))
		self.imagen9=pygame.Rect((0,0,107,16))
		self.imagen10=pygame.Rect((0,0,117,16))
		self.imagen11=pygame.Rect((0,0,127,16))
		self.imagen12=pygame.Rect((0,0,137,16))
		self.imagen13=pygame.Rect((0,0,147,16))
		self.imagen14=pygame.Rect((0,0,157,16))
		self.imagen15=pygame.Rect((0,0,167,16))
		self.imagen16=pygame.Rect((0,0,177,16))
		self.imagen17=pygame.Rect((0,0,187,16))
		self.imagen18=pygame.Rect((0,0,197,16))
		self.imagen19=pygame.Rect((0,0,207,16))
		self.imagen20=pygame.Rect((0,0,216,16))

		self.rect=self.menu.get_rect()
		self.rect.left,self.rect.top=(x,y)

	def update(self,pantalla,vmax,vac):
		self.com=vmax*5/100
		if vac==self.com:
			pantalla.blit(self.menu.subsurface(self.imagen1),self.rect)
		if vac==self.com*2:
			pantalla.blit(self.menu.subsurface(self.imagen2),self.rect)		
		if vac==self.com*3:
			pantalla.blit(self.menu.subsurface(self.imagen3),self.rect)
		if vac==self.com*4:
			pantalla.blit(self.menu.subsurface(self.imagen4),self.rect)
		if vac==self.com*5:
			pantalla.blit(self.menu.subsurface(self.imagen5),self.rect)
		if vac==self.com*6:
			pantalla.blit(self.menu.subsurface(self.imagen6),self.rect)
		if vac==self.com*7:
			pantalla.blit(self.menu.subsurface(self.imagen7),self.rect)
		if vac==self.com*8:
			pantalla.blit(self.menu.subsurface(self.imagen8),self.rect)
		if vac==self.com*9:
			pantalla.blit(self.menu.subsurface(self.imagen9),self.rect)
		if vac==self.com*10:
			pantalla.blit(self.menu.subsurface(self.imagen10),self.rect)
		if vac==self.com*11:
			pantalla.blit(self.menu.subsurface(self.imagen11),self.rect)
		if vac==self.com*12:
			pantalla.blit(self.menu.subsurface(self.imagen12),self.rect)
		if vac==self.com*13:
			pantalla.blit(self.menu.subsurface(self.imagen13),self.rect)
		if vac==self.com*14:
			pantalla.blit(self.menu.subsurface(self.imagen14),self.rect)
		if vac==self.com*15:
			pantalla.blit(self.menu.subsurface(self.imagen15),self.rect)
		if vac==self.com*16:
			pantalla.blit(self.menu.subsurface(self.imagen16),self.rect)
		if vac==self.com*17:
			pantalla.blit(self.menu.subsurface(self.imagen17),self.rect)
		if vac==self.com*18:
			pantalla.blit(self.menu.subsurface(self.imagen18),self.rect)
		if vac==self.com*19:
			pantalla.blit(self.menu.subsurface(self.imagen19),self.rect)
		if vac==self.com*20:
			pantalla.blit(self.menu.subsurface(self.imagen20),self.rect)

class barras_exp(pygame.sprite.Sprite):
	def __init__(self,imagen,x,y):
		self.menu=imagen

		self.imagen1=pygame.Rect((0,0,17,8))
		self.imagen2=pygame.Rect((0,0,27,8))
		self.imagen3=pygame.Rect((0,0,37,8))
		self.imagen3=pygame.Rect((0,0,47,8))
		self.imagen4=pygame.Rect((0,0,57,8))
		self.imagen5=pygame.Rect((0,0,67,8))
		self.imagen6=pygame.Rect((0,0,77,8))
		self.imagen7=pygame.Rect((0,0,87,8))
		self.imagen8=pygame.Rect((0,0,97,8))
		self.imagen9=pygame.Rect((0,0,107,8))
		self.imagen10=pygame.Rect((0,0,117,8))
		self.imagen11=pygame.Rect((0,0,127,8))
		self.imagen12=pygame.Rect((0,0,137,8))
		self.imagen13=pygame.Rect((0,0,147,8))
		self.imagen14=pygame.Rect((0,0,157,8))
		self.imagen15=pygame.Rect((0,0,167,8))
		self.imagen16=pygame.Rect((0,0,177,8))
		self.imagen17=pygame.Rect((0,0,187,8))
		self.imagen18=pygame.Rect((0,0,197,8))
		self.imagen19=pygame.Rect((0,0,200,8))
		self.imagen20=pygame.Rect((0,0,206,8))

		self.rect=self.menu.get_rect()
		self.rect.left,self.rect.top=(x,y)

	def update(self,pantalla,vmax,vac):
		self.com=vmax*5/100
		if vac==self.com:
			pantalla.blit(self.menu.subsurface(self.imagen1),self.rect)
		if vac==self.com*2:
			pantalla.blit(self.menu.subsurface(self.imagen2),self.rect)		
		if vac==self.com*3:
			pantalla.blit(self.menu.subsurface(self.imagen3),self.rect)
		if vac==self.com*4:
			pantalla.blit(self.menu.subsurface(self.imagen4),self.rect)
		if vac==self.com*5:
			pantalla.blit(self.menu.subsurface(self.imagen5),self.rect)
		if vac==self.com*6:
			pantalla.blit(self.menu.subsurface(self.imagen6),self.rect)
		if vac==self.com*7:
			pantalla.blit(self.menu.subsurface(self.imagen7),self.rect)
		if vac==self.com*8:
			pantalla.blit(self.menu.subsurface(self.imagen8),self.rect)
		if vac==self.com*9:
			pantalla.blit(self.menu.subsurface(self.imagen9),self.rect)
		if vac==self.com*10:
			pantalla.blit(self.menu.subsurface(self.imagen10),self.rect)
		if vac==self.com*11:
			pantalla.blit(self.menu.subsurface(self.imagen11),self.rect)
		if vac==self.com*12:
			pantalla.blit(self.menu.subsurface(self.imagen12),self.rect)
		if vac==self.com*13:
			pantalla.blit(self.menu.subsurface(self.imagen13),self.rect)
		if vac==self.com*14:
			pantalla.blit(self.menu.subsurface(self.imagen14),self.rect)
		if vac==self.com*15:
			pantalla.blit(self.menu.subsurface(self.imagen15),self.rect)
		if vac==self.com*16:
			pantalla.blit(self.menu.subsurface(self.imagen16),self.rect)
		if vac==self.com*17:
			pantalla.blit(self.menu.subsurface(self.imagen17),self.rect)
		if vac==self.com*18:
			pantalla.blit(self.menu.subsurface(self.imagen18),self.rect)
		if vac==self.com*19:
			pantalla.blit(self.menu.subsurface(self.imagen19),self.rect)
		if vac==self.com*20:
			pantalla.blit(self.menu.subsurface(self.imagen20),self.rect)

class boton_item(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.boton1=recursos.botonitem1
		self.boton2=recursos.botonitem2
		self.boton_actual=[self.boton1,self.boton2]
		self.rect=self.boton_actual[0].get_rect()
		self.rect.left,self.rect.top=(x,y)
		self.T=0

	def update(self,pantalla,cursor):
		if cursor.colliderect(self.rect) and pygame.mouse.get_pressed()[2]:
				self.T=1

		if cursor.colliderect(self.rect):
		 	if pygame.mouse.get_pressed()[0]:
		 		self.T=0

		pantalla.blit(self.boton_actual[self.T],self.rect)

class tienda(pygame.sprite.Sprite):
	def __init__(self):
		self.queitem=""
		self.totalgasto=0
		self.cantitems=0
		self.menu=recursos.menucomercio
		self.rect=self.menu.get_rect()
		self.rect.left,self.rect.top=(100,100)

		self.ag1=recursos.botonagregar
		self.ag2=recursos.botonagregar2
		self.bot_ag=boton_lanzar(self.ag1,self.ag2,338,165)


		self.com1=recursos.botoncomprar2.convert()
		self.com2=recursos.botoncomprar.convert()
		self.bot_com=boton_lanzar(self.com1,self.com2,418,221)

		self.mas12=recursos.botonmas12.convert()
		self.mas1=recursos.botonmas1.convert()
		self.bot_mas1=boton_apoka(self.mas1,self.mas12,342,190)

		self.mas10=recursos.botonmas10
		self.mas102=recursos.botonmas102
		self.bot_mas10=boton_apoka(self.mas10,self.mas102,365,190)

		self.mas100=recursos.botonmas100
		self.mas1002=recursos.botonmas1002
		self.bot_mas100=boton_apoka(self.mas100,self.mas1002,395,190)

		self.fuente=pygame.font.Font(None,20)
		self.fuentegrande=pygame.font.Font(None,30)

	
	def update(self,superficie,cursor):
		superficie.blit(self.menu,self.rect)
		self.bot_ag.update(superficie,cursor)
		self.bot_com.update(superficie,cursor)
		self.bot_mas1.update(superficie,cursor)
		self.bot_mas10.update(superficie,cursor)
		self.bot_mas100.update(superficie,cursor)
		#pygame.draw.rect(superficie, (255,255,255), [150, 50, 400, 400], 0)

class tienda_comidas(pygame.sprite.Sprite):
	def __init__(self):

		self.totalgasto=0
		self.cantitems=0
		self.agrega=0
		self.totalsuma=0

		self.listacompra=[0,0,0,0,0,0,0,0,0]
		self.itemscant=[0,0,0,0,0,0,0,0,0]

		self.menu=recursos.menucomercio
		self.rect=self.menu.get_rect()
		self.rect.left,self.rect.top=(100,100)

		self.fle1=recursos.flechaizquierda
		self.fle2=recursos.flechaizquierda2
		self.bot_fle1=boton_lanzar(self.fle1,self.fle2,271,306)

		self.fleb1=recursos.flechaderecha
		self.fleb2=recursos.flechaderecha2
		self.bot_fle2=boton_lanzar(self.fleb1,self.fleb2,308,306)

		self.com1=recursos.botoncomprar2#.convert()
		self.com2=recursos.botoncomprar#.convert()
		self.bot_com=boton_lanzar(self.com1,self.com2,418,221)

		self.vac1=recursos.botonvaciar1
		self.vac2=recursos.botonvaciar2
		self.bot_vac=boton_lanzar(self.vac1,self.vac2,418,188)

		self.mas10=recursos.botonmas10
		self.mas102=recursos.botonmas102
		self.bot_mas10=boton_apoka(self.mas10,self.mas102,277,282)

		self.mas100=recursos.botonmas100
		self.mas1002=recursos.botonmas1002
		self.bot_mas100=boton_apoka(self.mas100,self.mas1002,308,282)

		self.listaitems=items.icomidas
		self.nombres=[]
		self.precios=[]
		self.desc=[]
		self.titulo="Comerciante de comidas"

		for i in self.listaitems:
			self.nombres.append(i[0])

		for i in self.listaitems:
			self.precios.append(i[1])

		for i in self.listaitems:
			self.desc.append(i[2])

		self.nombres=tuple(self.nombres)
		self.precios=tuple(self.precios)
		self.desc=tuple(self.desc)


		self.fuente=pygame.font.Font(None,20)
		self.fuentegrande=pygame.font.Font(None,30)
		self.fuentepequeño=pygame.font.Font(None,16)

		self.texttit=self.fuentegrande.render(self.titulo,0,(255,255,255))

		self.text1=self.fuente.render(self.nombres[0],0,(255,255,255))
		self.text2=self.fuente.render(self.nombres[1],0,(255,255,255))
		self.text3=self.fuente.render(self.nombres[2],0,(255,255,255))
		self.text4=self.fuente.render(self.nombres[3],0,(255,255,255))
		self.text5=self.fuente.render(self.nombres[4],0,(255,255,255))
		self.text6=self.fuente.render(self.nombres[5],0,(255,255,255))
		self.text7=self.fuente.render(self.nombres[6],0,(255,255,255))
		self.text8=self.fuente.render(self.nombres[7],0,(255,255,255))
		self.text9=self.fuente.render(self.nombres[8],0,(255,255,255))

		self.textd1=self.fuentepequeño.render(self.desc[0],0,(255,255,255))
		self.textd2=self.fuentepequeño.render(self.desc[1],0,(255,255,255))
		self.textd3=self.fuentepequeño.render(self.desc[2],0,(255,255,255))
		self.textd4=self.fuentepequeño.render(self.desc[3],0,(255,255,255))
		self.textd5=self.fuentepequeño.render(self.desc[4],0,(255,255,255))
		self.textd6=self.fuentepequeño.render(self.desc[5],0,(255,255,255))
		self.textd7=self.fuentepequeño.render(self.desc[6],0,(255,255,255))
		self.textd8=self.fuentepequeño.render(self.desc[7],0,(255,255,255))
		self.textd9=self.fuentepequeño.render(self.desc[8],0,(255,255,255))

		self.textp1=self.fuente.render(str(self.precios[0])+" $",0,(255,255,255))
		self.textp2=self.fuente.render(str(self.precios[1])+" $",0,(255,255,255))
		self.textp3=self.fuente.render(str(self.precios[2])+" $",0,(255,255,255))
		self.textp4=self.fuente.render(str(self.precios[3])+" $",0,(255,255,255))
		self.textp5=self.fuente.render(str(self.precios[4])+" $",0,(255,255,255))
		self.textp6=self.fuente.render(str(self.precios[5])+" $",0,(255,255,255))
		self.textp7=self.fuente.render(str(self.precios[6])+" $",0,(255,255,255))
		self.textp8=self.fuente.render(str(self.precios[7])+" $",0,(255,255,255))
		self.textp9=self.fuente.render(str(self.precios[8])+" $",0,(255,255,255))

		self.textb1=self.fuente.render(self.nombres[0],0,(0,0,0))
		self.textb2=self.fuente.render(self.nombres[1],0,(0,0,0))
		self.textb3=self.fuente.render(self.nombres[2],0,(0,0,0))
		self.textb4=self.fuente.render(self.nombres[3],0,(0,0,0))
		self.textb5=self.fuente.render(self.nombres[4],0,(0,0,0))
		self.textb6=self.fuente.render(self.nombres[5],0,(0,0,0))
		self.textb7=self.fuente.render(self.nombres[6],0,(0,0,0))
		self.textb8=self.fuente.render(self.nombres[7],0,(0,0,0))
		self.textb9=self.fuente.render(self.nombres[8],0,(0,0,0))

		self.textbp1=self.fuente.render(str(self.precios[0])+" $",0,(0,0,0))
		self.textbp2=self.fuente.render(str(self.precios[1])+" $",0,(0,0,0))
		self.textbp3=self.fuente.render(str(self.precios[2])+" $",0,(0,0,0))
		self.textbp4=self.fuente.render(str(self.precios[3])+" $",0,(0,0,0))
		self.textbp5=self.fuente.render(str(self.precios[4])+" $",0,(0,0,0))
		self.textbp6=self.fuente.render(str(self.precios[5])+" $",0,(0,0,0))
		self.textbp7=self.fuente.render(str(self.precios[6])+" $",0,(0,0,0))
		self.textbp8=self.fuente.render(str(self.precios[7])+" $",0,(0,0,0))
		self.textbp9=self.fuente.render(str(self.precios[8])+" $",0,(0,0,0))


		self.boti1=boton_item(105,279)
		self.boti2=boton_item(105,300)
		self.boti3=boton_item(105,322)
		self.boti4=boton_item(105,344)
		self.boti5=boton_item(105,366)
		self.boti6=boton_item(105,387)
		self.boti7=boton_item(105,409)
		self.boti8=boton_item(105,430)
		self.boti9=boton_item(105,452)

		self.listabotones=(self.boti1,self.boti2,self.boti3,self.boti4,self.boti5,self.boti6,self.boti7,self.boti8,self.boti9)
		self.momentosintervalo=(0,3,6,9,11,14,17,21,24,27,30,33,36,39,41,44,47,50,53,56,59,61,64,67,71,74,77,80,83,86,89,91,94,97)
	def suma_items(self):
		self.cantitems=self.cantitems+self.agrega
	def resta_items(self):
		self.cantitems=self.cantitems-self.agrega
		if self.cantitems<0:
			self.cantitems=0

	def suma_compra(self):
		self.totalsuma=self.itemscant[0]*self.precios[0]+self.itemscant[1]*self.precios[1]+self.itemscant[2]*self.precios[2]+self.itemscant[3]*self.precios[3]+self.itemscant[4]*self.precios[4]+self.itemscant[5]*self.precios[5]+self.itemscant[6]*self.precios[6]+self.itemscant[7]*self.precios[7]+self.itemscant[8]*self.precios[8]
	

	def update(self,superficie,cursor,intervalo):
		superficie.blit(self.menu,self.rect)

		if self.bot_mas10.T==1:
			self.agrega=10
		if self.bot_mas100.T==1:
			self.agrega=100
		if self.bot_mas10.T==0 and self.bot_mas100.T==0:
			self.agrega=1

		if self.bot_vac.T==1:
			self.cantitems=0

		self.suma_compra()

		if self.bot_fle2.T==1:
			for i in self.momentosintervalo:
				if i==intervalo:
					self.suma_items()

		if self.bot_fle1.T==1:
			for i in self.momentosintervalo:
				if i==intervalo:
					self.resta_items()


		

		self.boti1.update(superficie,cursor)
		self.boti2.update(superficie,cursor)
		self.boti3.update(superficie,cursor)
		self.boti4.update(superficie,cursor)
		self.boti5.update(superficie,cursor)
		self.boti6.update(superficie,cursor)
		self.boti7.update(superficie,cursor)
		self.boti8.update(superficie,cursor)
		self.boti9.update(superficie,cursor)

		superficie.blit(self.texttit,(180,110))

		for i in self.listabotones:
			if i.T==0:
				superficie.blit(self.text1,(110,285))
				superficie.blit(self.text2,(110,305))
				superficie.blit(self.text3,(110,325))
				superficie.blit(self.text4,(110,345))
				superficie.blit(self.text5,(110,365))
				superficie.blit(self.text6,(110,390))
				superficie.blit(self.text7,(110,415))
				superficie.blit(self.text8,(110,435))
				superficie.blit(self.text9,(110,455))

				superficie.blit(self.textp1,(220,285))
				superficie.blit(self.textp2,(220,305))
				superficie.blit(self.textp3,(220,325))
				superficie.blit(self.textp4,(220,345))
				superficie.blit(self.textp5,(220,365))
				superficie.blit(self.textp6,(220,390))
				superficie.blit(self.textp7,(220,415))
				superficie.blit(self.textp8,(220,435))
				superficie.blit(self.textp9,(220,455))


		for i in self.listabotones:
			if i.T==1:
				superficie.blit(self.textb1,(110,285))
				superficie.blit(self.textb2,(110,305))
				superficie.blit(self.textb3,(110,325))
				superficie.blit(self.textb4,(110,345))
				superficie.blit(self.textb5,(110,365))
				superficie.blit(self.textb6,(110,390))
				superficie.blit(self.textb7,(110,415))
				superficie.blit(self.textb8,(110,435))
				superficie.blit(self.textb9,(110,455))

				superficie.blit(self.textbp1,(220,285))
				superficie.blit(self.textbp2,(220,305))
				superficie.blit(self.textbp3,(220,325))
				superficie.blit(self.textbp4,(220,345))
				superficie.blit(self.textbp5,(220,365))
				superficie.blit(self.textbp6,(220,390))
				superficie.blit(self.textbp7,(220,415))
				superficie.blit(self.textbp8,(220,435))
				superficie.blit(self.textbp9,(220,455))

				if i==self.boti1:
					superficie.blit(items.imagengral.subsurface(items.comidas[0]),(170,175))
					superficie.blit(self.textd1,(110,230))
					if self.cantitems>0:
						self.listacompra[0]=self.text1
						self.itemscant[0]=self.cantitems
					if self.cantitems==0:
						self.listacompra[0]=0
						self.itemscant[0]=0
					
				if i==self.boti2:
					superficie.blit(items.imagengral.subsurface(items.comidas[1]),(170,175))
					superficie.blit(self.textd2,(110,230))
					if self.cantitems>0:
						self.listacompra[1]=self.text2
						self.itemscant[1]=self.cantitems
					if self.cantitems==0:
						self.listacompra[1]=0
						self.itemscant[1]=0

				if i==self.boti3:
					superficie.blit(items.imagengral.subsurface(items.comidas[2]),(170,175))
					superficie.blit(self.textd3,(110,230))
					if self.cantitems>0:
						self.listacompra[2]=self.text3
						self.itemscant[2]=self.cantitems
					if self.cantitems==0:
						self.listacompra[2]=0
						self.itemscant[2]=0
				if i==self.boti4:
					superficie.blit(items.imagengral.subsurface(items.comidas[3]),(170,175))
					superficie.blit(self.textd4,(110,230))
					if self.cantitems>0:
						self.listacompra[3]=self.text4
						self.itemscant[3]=self.cantitems
					if self.cantitems==0:
						self.listacompra[3]=0
						self.itemscant[3]=0
				if i==self.boti5:
					superficie.blit(items.imagengral.subsurface(items.comidas[4]),(170,175))
					superficie.blit(self.textd5,(110,230))
					if self.cantitems>0:
						self.listacompra[4]=self.text5
						self.itemscant[4]=self.cantitems
					if self.cantitems==0:
						self.listacompra[4]=0
						self.itemscant[4]=0

				if i==self.boti6:
					superficie.blit(items.imagengral.subsurface(items.comidas[5]),(170,175))
					superficie.blit(self.textd6,(110,230))
					if self.cantitems>0:
						self.listacompra[5]=self.text6
						self.itemscant[5]=self.cantitems
					if self.cantitems==0:
						self.listacompra[5]=0
						self.itemscant[5]=0
				if i==self.boti7:
					superficie.blit(items.imagengral.subsurface(items.comidas[6]),(170,175))
					superficie.blit(self.textd7,(110,230))
					if self.cantitems>0:
						self.listacompra[6]=self.text7
						self.itemscant[6]=self.cantitems
					if self.cantitems==0:
						self.listacompra[6]=0
						self.itemscant[6]=0
				if i==self.boti8:
					superficie.blit(items.imagengral.subsurface(items.comidas[7]),(170,175))
					superficie.blit(self.textd8,(110,230))
					if self.cantitems>0:
						self.listacompra[7]=self.text8
						self.itemscant[7]=self.cantitems
					if self.cantitems==0:
						self.listacompra[7]=0
						self.itemscant[7]=0
				if i==self.boti9:
					superficie.blit(items.imagengral.subsurface(items.comidas[8]),(170,175))
					superficie.blit(self.textd9,(110,230))
					if self.cantitems>0:
						self.listacompra[8]=self.text9
						self.itemscant[8]=self.cantitems
					if self.cantitems==0:
						self.listacompra[8]=0
						self.itemscant[8]=0


		self.iteras1=self.fuente.render(str(self.itemscant[0]),0,(255,255,255))
		self.iteras2=self.fuente.render(str(self.itemscant[1]),0,(255,255,255))
		self.iteras3=self.fuente.render(str(self.itemscant[2]),0,(255,255,255))
		self.iteras4=self.fuente.render(str(self.itemscant[3]),0,(255,255,255))
		self.iteras5=self.fuente.render(str(self.itemscant[4]),0,(255,255,255))
		self.iteras6=self.fuente.render(str(self.itemscant[5]),0,(255,255,255))
		self.iteras7=self.fuente.render(str(self.itemscant[6]),0,(255,255,255))
		self.iteras8=self.fuente.render(str(self.itemscant[7]),0,(255,255,255))
		self.iteras9=self.fuente.render(str(self.itemscant[8]),0,(255,255,255))


		self.textsumatotal=self.fuente.render(str(self.totalsuma),0,(255,255,255))


		for i in self.listacompra:
			if i!=0:
				if i==self.listacompra[0]:
					superficie.blit(self.listacompra[0],(365,285))
					superficie.blit(self.iteras1,(345,285))
				if i==self.listacompra[1]:
					superficie.blit(self.listacompra[1],(365,305))
					superficie.blit(self.iteras2,(345,305))
				if i==self.listacompra[2]:
					superficie.blit(self.listacompra[2],(365,325))
					superficie.blit(self.iteras3,(345,325))
				if i==self.listacompra[3]:
					superficie.blit(self.listacompra[3],(365,345))
					superficie.blit(self.iteras4,(345,345))
				if i==self.listacompra[4]:
					superficie.blit(self.listacompra[4],(365,365))
					superficie.blit(self.iteras5,(345,365))
				if i==self.listacompra[5]:
					superficie.blit(self.listacompra[5],(365,390))
					superficie.blit(self.iteras6,(345,390))
				if i==self.listacompra[6]:
					superficie.blit(self.listacompra[6],(365,415))
					superficie.blit(self.iteras7,(345,415))
				if i==self.listacompra[7]:
					superficie.blit(self.listacompra[7],(365,435))
					superficie.blit(self.iteras8,(345,435))
				if i==self.listacompra[8]:
					superficie.blit(self.listacompra[8],(365,455))
					superficie.blit(self.iteras9,(345,455))

		self.bot_fle1.update(superficie,cursor)
		self.bot_fle2.update(superficie,cursor)
		self.bot_com.update(superficie,cursor)
		self.bot_mas10.update(superficie,cursor)
		self.bot_mas100.update(superficie,cursor)
		self.bot_vac.update(superficie,cursor)
		superficie.blit(self.textsumatotal,(370,245))


class tienda_hechizos(pygame.sprite.Sprite):
	def __init__(self):

		self.totalgasto=0
		self.cantitems=0
		self.agrega=0
		self.totalsuma=0

		self.listacompra=[0,0,0,0,0,0,0,0,0]
		self.itemscant=[0,0,0,0,0,0,0,0,0]

		self.menu=recursos.menucomercio
		self.rect=self.menu.get_rect()
		self.rect.left,self.rect.top=(100,100)

		self.fle1=recursos.flechaizquierda
		self.fle2=recursos.flechaizquierda2
		self.bot_fle1=boton_lanzar(self.fle1,self.fle2,271,306)

		self.fleb1=recursos.flechaderecha
		self.fleb2=recursos.flechaderecha2
		self.bot_fle2=boton_lanzar(self.fleb1,self.fleb2,308,306)


		self.com1=recursos.botoncomprar2#.convert()
		self.com2=recursos.botoncomprar#.convert()
		self.bot_com=boton_lanzar(self.com1,self.com2,418,221)

		self.vac1=recursos.botonvaciar1
		self.vac2=recursos.botonvaciar2
		self.bot_vac=boton_lanzar(self.vac1,self.vac2,418,188)

		self.mas10=recursos.botonmas10
		self.mas102=recursos.botonmas102
		self.bot_mas10=boton_apoka(self.mas10,self.mas102,277,282)

		self.mas100=recursos.botonmas100
		self.mas1002=recursos.botonmas1002
		self.bot_mas100=boton_apoka(self.mas100,self.mas1002,308,282)

		self.listaitems=items.ihechizos
		self.nombres=[]
		self.precios=[]
		self.desc=[]
		self.titulo="Comerciante de hechizos"

		for i in self.listaitems:
			self.nombres.append(i[0])

		for i in self.listaitems:
			self.precios.append(i[1])

		for i in self.listaitems:
			self.desc.append(i[2])

		self.nombres=tuple(self.nombres)
		self.precios=tuple(self.precios)
		self.desc=tuple(self.desc)


		self.fuente=pygame.font.Font(None,20)
		self.fuentegrande=pygame.font.Font(None,30)
		self.fuentepequeño=pygame.font.Font(None,16)

		self.texttit=self.fuentegrande.render(self.titulo,0,(255,255,255))

		self.text1=self.fuente.render(self.nombres[0],0,(255,255,255))
		self.text2=self.fuente.render(self.nombres[1],0,(255,255,255))
		self.text3=self.fuente.render(self.nombres[2],0,(255,255,255))
		self.text4=self.fuente.render(self.nombres[3],0,(255,255,255))
		#self.text5=self.fuente.render(self.nombres[4],0,(255,255,255))
		#self.text6=self.fuente.render(self.nombres[5],0,(255,255,255))
		#self.text7=self.fuente.render(self.nombres[6],0,(255,255,255))
		#self.text8=self.fuente.render(self.nombres[7],0,(255,255,255))
		#self.text9=self.fuente.render(self.nombres[8],0,(255,255,255))

		self.textd1=self.fuentepequeño.render(self.desc[0],0,(255,255,255))
		self.textd2=self.fuentepequeño.render(self.desc[1],0,(255,255,255))
		self.textd3=self.fuentepequeño.render(self.desc[2],0,(255,255,255))
		self.textd4=self.fuentepequeño.render(self.desc[3],0,(255,255,255))
		#self.textd5=self.fuentepequeño.render(self.desc[4],0,(255,255,255))
		#self.textd6=self.fuentepequeño.render(self.desc[5],0,(255,255,255))
		#self.textd7=self.fuentepequeño.render(self.desc[6],0,(255,255,255))
		#self.textd8=self.fuentepequeño.render(self.desc[7],0,(255,255,255))
		#self.textd9=self.fuentepequeño.render(self.desc[8],0,(255,255,255))

		self.textp1=self.fuente.render(str(self.precios[0])+" $",0,(255,255,255))
		self.textp2=self.fuente.render(str(self.precios[1])+" $",0,(255,255,255))
		self.textp3=self.fuente.render(str(self.precios[2])+" $",0,(255,255,255))
		self.textp4=self.fuente.render(str(self.precios[3])+" $",0,(255,255,255))
		#self.textp5=self.fuente.render(str(self.precios[4])+" $",0,(255,255,255))
		#self.textp6=self.fuente.render(str(self.precios[5])+" $",0,(255,255,255))
		#self.textp7=self.fuente.render(str(self.precios[6])+" $",0,(255,255,255))
		#self.textp8=self.fuente.render(str(self.precios[7])+" $",0,(255,255,255))
		#self.textp9=self.fuente.render(str(self.precios[8])+" $",0,(255,255,255))

		self.textb1=self.fuente.render(self.nombres[0],0,(0,0,0))
		self.textb2=self.fuente.render(self.nombres[1],0,(0,0,0))
		self.textb3=self.fuente.render(self.nombres[2],0,(0,0,0))
		self.textb4=self.fuente.render(self.nombres[3],0,(0,0,0))
		#self.textb5=self.fuente.render(self.nombres[4],0,(0,0,0))
		#self.textb6=self.fuente.render(self.nombres[5],0,(0,0,0))
		#self.textb7=self.fuente.render(self.nombres[6],0,(0,0,0))
		#self.textb8=self.fuente.render(self.nombres[7],0,(0,0,0))
		#self.textb9=self.fuente.render(self.nombres[8],0,(0,0,0))

		self.textbp1=self.fuente.render(str(self.precios[0])+" $",0,(0,0,0))
		self.textbp2=self.fuente.render(str(self.precios[1])+" $",0,(0,0,0))
		self.textbp3=self.fuente.render(str(self.precios[2])+" $",0,(0,0,0))
		self.textbp4=self.fuente.render(str(self.precios[3])+" $",0,(0,0,0))
		#self.textbp5=self.fuente.render(str(self.precios[4])+" $",0,(0,0,0))
		#self.textbp6=self.fuente.render(str(self.precios[5])+" $",0,(0,0,0))
		#self.textbp7=self.fuente.render(str(self.precios[6])+" $",0,(0,0,0))
		#self.textbp8=self.fuente.render(str(self.precios[7])+" $",0,(0,0,0))
		#self.textbp9=self.fuente.render(str(self.precios[8])+" $",0,(0,0,0))


		self.boti1=boton_item(105,279)
		self.boti2=boton_item(105,300)
		self.boti3=boton_item(105,322)
		self.boti4=boton_item(105,344)
		#self.boti5=boton_item(105,366)
		#self.boti6=boton_item(105,387)
		#self.boti7=boton_item(105,409)
		#self.boti8=boton_item(105,430)
		#self.boti9=boton_item(105,452)

		self.listabotones=(self.boti1,self.boti2,self.boti3,self.boti4)
		self.momentosintervalo=(0,3,6,9,11,14,17,21,24,27,30,33,36,39,41,44,47,50,53,56,59,61,64,67,71,74,77,80,83,86,89,91,94,97)
	def suma_items(self):
		self.cantitems=self.cantitems+self.agrega
	def resta_items(self):
		self.cantitems=self.cantitems-self.agrega
		if self.cantitems<0:
			self.cantitems=0

	def suma_compra(self):
		self.totalsuma=self.itemscant[0]*self.precios[0]+self.itemscant[1]*self.precios[1]+self.itemscant[2]*self.precios[2]+self.itemscant[3]*self.precios[3]
	

	def update(self,superficie,cursor,intervalo):
		superficie.blit(self.menu,self.rect)

		if self.bot_mas10.T==1:
			self.agrega=10
		if self.bot_mas100.T==1:
			self.agrega=100
		if self.bot_mas10.T==0 and self.bot_mas100.T==0:
			self.agrega=1

		if self.bot_vac.T==1:
			self.cantitems=0

		self.suma_compra()

		if self.bot_fle2.T==1:
			for i in self.momentosintervalo:
				if i==intervalo:
					self.suma_items()

		if self.bot_fle1.T==1:
			for i in self.momentosintervalo:
				if i==intervalo:
					self.resta_items()


		

		self.boti1.update(superficie,cursor)
		self.boti2.update(superficie,cursor)
		self.boti3.update(superficie,cursor)
		self.boti4.update(superficie,cursor)
		#self.boti5.update(superficie,cursor)
		#self.boti6.update(superficie,cursor)
		#self.boti7.update(superficie,cursor)
		#self.boti8.update(superficie,cursor)
		#self.boti9.update(superficie,cursor)

		superficie.blit(self.texttit,(180,110))

		for i in self.listabotones:
			if i.T==0:
				superficie.blit(self.text1,(110,285))
				superficie.blit(self.text2,(110,305))
				superficie.blit(self.text3,(110,325))
				superficie.blit(self.text4,(110,345))
				#superficie.blit(self.text5,(110,365))
				#superficie.blit(self.text6,(110,390))
				#superficie.blit(self.text7,(110,415))
				#superficie.blit(self.text8,(110,435))
				#superficie.blit(self.text9,(110,455))

				superficie.blit(self.textp1,(220,285))
				superficie.blit(self.textp2,(220,305))
				superficie.blit(self.textp3,(220,325))#
				superficie.blit(self.textp4,(220,345))
				#superficie.blit(self.textp5,(220,365))
				#superficie.blit(self.textp6,(220,390))
				#superficie.blit(self.textp7,(220,415))
				#superficie.blit(self.textp8,(220,435))
				#superficie.blit(self.textp9,(220,455))


		for i in self.listabotones:
			if i.T==1:
				superficie.blit(self.textb1,(110,285))
				superficie.blit(self.textb2,(110,305))
				superficie.blit(self.textb3,(110,325))
				superficie.blit(self.textb4,(110,345))
				#superficie.blit(self.textb5,(110,365))
				#superficie.blit(self.textb6,(110,390))
				#superficie.blit(self.textb7,(110,415))
				#superficie.blit(self.textb8,(110,435))
				#superficie.blit(self.textb9,(110,455))

				superficie.blit(self.textbp1,(220,285))
				superficie.blit(self.textbp2,(220,305))
				superficie.blit(self.textbp3,(220,325))
				superficie.blit(self.textbp4,(220,345))
				#superficie.blit(self.textbp5,(220,365))
				#superficie.blit(self.textbp6,(220,390))
				#superficie.blit(self.textbp7,(220,415))
				#superficie.blit(self.textbp8,(220,435))
				#superficie.blit(self.textbp9,(220,455))

				if i==self.boti1:
					superficie.blit(items.imagengral.subsurface(items.hechizos[0]),(170,175))
					superficie.blit(self.textd1,(110,230))
					if self.cantitems>0:
						self.listacompra[0]=self.text1
						self.itemscant[0]=self.cantitems
					if self.cantitems==0:
						self.listacompra[0]=0
						self.itemscant[0]=0
					
				if i==self.boti2:
					superficie.blit(items.imagengral.subsurface(items.hechizos[1]),(170,175))
					superficie.blit(self.textd2,(110,230))
					if self.cantitems>0:
						self.listacompra[1]=self.text2
						self.itemscant[1]=self.cantitems
					if self.cantitems==0:
						self.listacompra[1]=0
						self.itemscant[1]=0

				if i==self.boti3:
					superficie.blit(items.imagengral.subsurface(items.hechizos[2]),(170,175))
					superficie.blit(self.textd3,(110,230))
					if self.cantitems>0:
						self.listacompra[2]=self.text3
						self.itemscant[2]=self.cantitems
					if self.cantitems==0:
						self.listacompra[2]=0
						self.itemscant[2]=0
				if i==self.boti4:
					superficie.blit(items.imagengral.subsurface(items.hechizos[3]),(170,175))
					superficie.blit(self.textd4,(110,230))
					if self.cantitems>0:
						self.listacompra[3]=self.text4
						self.itemscant[3]=self.cantitems
					if self.cantitems==0:
						self.listacompra[3]=0
						self.itemscant[3]=0
				#if i==self.boti5:
					#superficie.blit(items.imagengral.subsurface(items.comidas[4]),(170,175))
					#superficie.blit(self.textd5,(110,230))
					#if self.cantitems>0:
						#self.listacompra[4]=self.text5
						#self.itemscant[4]=self.cantitems
					#if self.cantitems==0:
						#self.listacompra[4]=0
						#self.itemscant[4]=0

				#if i==self.boti6:
					#superficie.blit(items.imagengral.subsurface(items.comidas[5]),(170,175))
					#superficie.blit(self.textd6,(110,230))
					#if self.cantitems>0:
						#self.listacompra[5]=self.text6
						#self.itemscant[5]=self.cantitems
					#if self.cantitems==0:
						#self.listacompra[5]=0
						#self.itemscant[5]=0
				#if i==self.boti7:
					#superficie.blit(items.imagengral.subsurface(items.comidas[6]),(170,175))
					#superficie.blit(self.textd7,(110,230))
					#if self.cantitems>0:
						#self.listacompra[6]=self.text7
						#self.itemscant[6]=self.cantitems
					#if self.cantitems==0:
						#self.listacompra[6]=0
						#self.itemscant[6]=0
				#if i==self.boti8:
					#superficie.blit(items.imagengral.subsurface(items.comidas[7]),(170,175))
					#superficie.blit(self.textd8,(110,230))
					#if self.cantitems>0:
						#self.listacompra[7]=self.text8
						#self.itemscant[7]=self.cantitems
					#if self.cantitems==0:
						#self.listacompra[7]=0
						#self.itemscant[7]=0
				#if i==self.boti9:
					#superficie.blit(items.imagengral.subsurface(items.comidas[8]),(170,175))
					#superficie.blit(self.textd9,(110,230))
					#if self.cantitems>0:
						#self.listacompra[8]=self.text9
						#self.itemscant[8]=self.cantitems
					#if self.cantitems==0:
						#self.listacompra[8]=0
						#self.itemscant[8]=0


		self.iteras1=self.fuente.render(str(self.itemscant[0]),0,(255,255,255))
		self.iteras2=self.fuente.render(str(self.itemscant[1]),0,(255,255,255))
		self.iteras3=self.fuente.render(str(self.itemscant[2]),0,(255,255,255))
		self.iteras4=self.fuente.render(str(self.itemscant[3]),0,(255,255,255))
		#self.iteras5=self.fuente.render(str(self.itemscant[4]),0,(255,255,255))
		#self.iteras6=self.fuente.render(str(self.itemscant[5]),0,(255,255,255))
		#self.iteras7=self.fuente.render(str(self.itemscant[6]),0,(255,255,255))
		#self.iteras8=self.fuente.render(str(self.itemscant[7]),0,(255,255,255))
		#self.iteras9=self.fuente.render(str(self.itemscant[8]),0,(255,255,255))


		self.textsumatotal=self.fuente.render(str(self.totalsuma),0,(255,255,255))


		for i in self.listacompra:
			if i!=0:
				if i==self.listacompra[0]:
					superficie.blit(self.listacompra[0],(365,285))
					superficie.blit(self.iteras1,(345,285))
				if i==self.listacompra[1]:
					superficie.blit(self.listacompra[1],(365,305))
					superficie.blit(self.iteras2,(345,305))
				if i==self.listacompra[2]:
					superficie.blit(self.listacompra[2],(365,325))
					superficie.blit(self.iteras3,(345,325))
				if i==self.listacompra[3]:
					superficie.blit(self.listacompra[3],(365,345))
					superficie.blit(self.iteras4,(345,345))
				#if i==self.listacompra[4]:
					#superficie.blit(self.listacompra[4],(365,365))
					#superficie.blit(self.iteras5,(345,365))
				#if i==self.listacompra[5]:
					#superficie.blit(self.listacompra[5],(365,390))
					#superficie.blit(self.iteras6,(345,390))
				#if i==self.listacompra[6]:
					#superficie.blit(self.listacompra[6],(365,415))
					#superficie.blit(self.iteras7,(345,415))
				#if i==self.listacompra[7]:
					#superficie.blit(self.listacompra[7],(365,435))
					#superficie.blit(self.iteras8,(345,435))
				#if i==self.listacompra[8]:
					#superficie.blit(self.listacompra[8],(365,455))
					#superficie.blit(self.iteras9,(345,455))

		self.bot_fle1.update(superficie,cursor)
		self.bot_fle2.update(superficie,cursor)
		self.bot_com.update(superficie,cursor)
		self.bot_mas10.update(superficie,cursor)
		self.bot_mas100.update(superficie,cursor)
		self.bot_vac.update(superficie,cursor)
		superficie.blit(self.textsumatotal,(370,245))


class tienda_armas1(pygame.sprite.Sprite):
	def __init__(self):

		self.totalgasto=0
		self.cantitems=0
		self.agrega=0
		self.totalsuma=0

		self.listacompra=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		self.itemscant=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

		self.menu=recursos.menucomercio
		self.rect=self.menu.get_rect()
		self.rect.left,self.rect.top=(100,100)

		self.fle1=recursos.flechaizquierda
		self.fle2=recursos.flechaizquierda2
		self.bot_fle1=boton_lanzar(self.fle1,self.fle2,271,306)

		self.fleb1=recursos.flechaderecha
		self.fleb2=recursos.flechaderecha2
		self.bot_fle2=boton_lanzar(self.fleb1,self.fleb2,308,306)

		self.com1=recursos.botoncomprar2#.convert()
		self.com2=recursos.botoncomprar#.convert()
		self.bot_com=boton_lanzar(self.com1,self.com2,418,221)

		self.vac1=recursos.botonvaciar1
		self.vac2=recursos.botonvaciar2
		self.bot_vac=boton_lanzar(self.vac1,self.vac2,418,188)

		self.mas10=recursos.botonmas10
		self.mas102=recursos.botonmas102
		self.bot_mas10=boton_apoka(self.mas10,self.mas102,277,282)

		self.mas100=recursos.botonmas100
		self.mas1002=recursos.botonmas1002
		self.bot_mas100=boton_apoka(self.mas100,self.mas1002,308,282)

		self.listaitems=items.iarmas1
		self.nombres=[]
		self.precios=[]
		self.desc=[]
		self.titulo="Comerciante de armas"

		for i in self.listaitems:
			self.nombres.append(i[0])

		for i in self.listaitems:
			self.precios.append(i[1])

		for i in self.listaitems:
			self.desc.append(i[2])

		self.nombres=tuple(self.nombres)
		self.precios=tuple(self.precios)
		self.desc=tuple(self.desc)


		self.fuente=pygame.font.Font(None,20)
		self.fuentegrande=pygame.font.Font(None,30)
		self.fuentepequeño=pygame.font.Font(None,16)

		self.texttit=self.fuentegrande.render(self.titulo,0,(255,255,255))

		self.text1=self.fuente.render(self.nombres[0],0,(255,255,255))
		self.text2=self.fuente.render(self.nombres[1],0,(255,255,255))
		self.text3=self.fuente.render(self.nombres[2],0,(255,255,255))
		self.text4=self.fuente.render(self.nombres[3],0,(255,255,255))
		self.text5=self.fuente.render(self.nombres[4],0,(255,255,255))
		self.text6=self.fuente.render(self.nombres[5],0,(255,255,255))
		self.text7=self.fuente.render(self.nombres[6],0,(255,255,255))
		self.text8=self.fuente.render(self.nombres[7],0,(255,255,255))
		self.text9=self.fuente.render(self.nombres[8],0,(255,255,255))
		self.text10=self.fuente.render(self.nombres[9],0,(255,255,255))
		self.text11=self.fuente.render(self.nombres[10],0,(255,255,255))
		self.text12=self.fuente.render(self.nombres[11],0,(255,255,255))
		self.text13=self.fuente.render(self.nombres[12],0,(255,255,255))
		self.text14=self.fuente.render(self.nombres[13],0,(255,255,255))
		self.text15=self.fuente.render(self.nombres[14],0,(255,255,255))


		self.textd1=self.fuentepequeño.render(self.desc[0],0,(255,255,255))
		self.textd2=self.fuentepequeño.render(self.desc[1],0,(255,255,255))
		self.textd3=self.fuentepequeño.render(self.desc[2],0,(255,255,255))
		self.textd4=self.fuentepequeño.render(self.desc[3],0,(255,255,255))
		self.textd5=self.fuentepequeño.render(self.desc[4],0,(255,255,255))
		self.textd6=self.fuentepequeño.render(self.desc[5],0,(255,255,255))
		self.textd7=self.fuentepequeño.render(self.desc[6],0,(255,255,255))
		self.textd8=self.fuentepequeño.render(self.desc[7],0,(255,255,255))
		self.textd9=self.fuentepequeño.render(self.desc[8],0,(255,255,255))
		self.textd10=self.fuentepequeño.render(self.desc[9],0,(255,255,255))
		self.textd11=self.fuentepequeño.render(self.desc[10],0,(255,255,255))
		self.textd12=self.fuentepequeño.render(self.desc[11],0,(255,255,255))
		self.textd13=self.fuentepequeño.render(self.desc[12],0,(255,255,255))
		self.textd14=self.fuentepequeño.render(self.desc[13],0,(255,255,255))
		self.textd15=self.fuentepequeño.render(self.desc[14],0,(255,255,255))


		self.textp1=self.fuente.render(str(self.precios[0])+" $",0,(255,255,255))
		self.textp2=self.fuente.render(str(self.precios[1])+" $",0,(255,255,255))
		self.textp3=self.fuente.render(str(self.precios[2])+" $",0,(255,255,255))
		self.textp4=self.fuente.render(str(self.precios[3])+" $",0,(255,255,255))
		self.textp5=self.fuente.render(str(self.precios[4])+" $",0,(255,255,255))
		self.textp6=self.fuente.render(str(self.precios[5])+" $",0,(255,255,255))
		self.textp7=self.fuente.render(str(self.precios[6])+" $",0,(255,255,255))
		self.textp8=self.fuente.render(str(self.precios[7])+" $",0,(255,255,255))
		self.textp9=self.fuente.render(str(self.precios[8])+" $",0,(255,255,255))
		self.textp10=self.fuente.render(str(self.precios[9])+" $",0,(255,255,255))
		self.textp11=self.fuente.render(str(self.precios[10])+" $",0,(255,255,255))
		self.textp12=self.fuente.render(str(self.precios[11])+" $",0,(255,255,255))
		self.textp13=self.fuente.render(str(self.precios[12])+" $",0,(255,255,255))
		self.textp14=self.fuente.render(str(self.precios[13])+" $",0,(255,255,255))
		self.textp15=self.fuente.render(str(self.precios[14])+" $",0,(255,255,255))

		self.textb1=self.fuente.render(self.nombres[0],0,(0,0,0))
		self.textb2=self.fuente.render(self.nombres[1],0,(0,0,0))
		self.textb3=self.fuente.render(self.nombres[2],0,(0,0,0))
		self.textb4=self.fuente.render(self.nombres[3],0,(0,0,0))
		self.textb5=self.fuente.render(self.nombres[4],0,(0,0,0))
		self.textb6=self.fuente.render(self.nombres[5],0,(0,0,0))
		self.textb7=self.fuente.render(self.nombres[6],0,(0,0,0))
		self.textb8=self.fuente.render(self.nombres[7],0,(0,0,0))
		self.textb9=self.fuente.render(self.nombres[8],0,(0,0,0))
		self.textb10=self.fuente.render(self.nombres[9],0,(0,0,0))
		self.textb11=self.fuente.render(self.nombres[10],0,(0,0,0))
		self.textb12=self.fuente.render(self.nombres[11],0,(0,0,0))
		self.textb13=self.fuente.render(self.nombres[12],0,(0,0,0))
		self.textb14=self.fuente.render(self.nombres[13],0,(0,0,0))
		self.textb15=self.fuente.render(self.nombres[14],0,(0,0,0))


		self.textbp1=self.fuente.render(str(self.precios[0])+" $",0,(0,0,0))
		self.textbp2=self.fuente.render(str(self.precios[1])+" $",0,(0,0,0))
		self.textbp3=self.fuente.render(str(self.precios[2])+" $",0,(0,0,0))
		self.textbp4=self.fuente.render(str(self.precios[3])+" $",0,(0,0,0))
		self.textbp5=self.fuente.render(str(self.precios[4])+" $",0,(0,0,0))
		self.textbp6=self.fuente.render(str(self.precios[5])+" $",0,(0,0,0))
		self.textbp7=self.fuente.render(str(self.precios[6])+" $",0,(0,0,0))
		self.textbp8=self.fuente.render(str(self.precios[7])+" $",0,(0,0,0))
		self.textbp9=self.fuente.render(str(self.precios[8])+" $",0,(0,0,0))
		self.textbp10=self.fuente.render(str(self.precios[9])+" $",0,(0,0,0))
		self.textbp11=self.fuente.render(str(self.precios[10])+" $",0,(0,0,0))
		self.textbp12=self.fuente.render(str(self.precios[11])+" $",0,(0,0,0))
		self.textbp13=self.fuente.render(str(self.precios[12])+" $",0,(0,0,0))
		self.textbp14=self.fuente.render(str(self.precios[13])+" $",0,(0,0,0))
		self.textbp15=self.fuente.render(str(self.precios[14])+" $",0,(0,0,0))

		self.boti1=boton_item(105,279)
		self.boti2=boton_item(105,300)
		self.boti3=boton_item(105,322)
		self.boti4=boton_item(105,344)
		self.boti5=boton_item(105,366)
		self.boti6=boton_item(105,387)
		self.boti7=boton_item(105,409)
		self.boti8=boton_item(105,430)
		self.boti9=boton_item(105,452)
		self.boti10=boton_item(105,472)
		self.boti11=boton_item(105,495)
		self.boti12=boton_item(105,517)
		self.boti13=boton_item(105,539)
		self.boti14=boton_item(105,560)
		self.boti15=boton_item(105,582)

		self.listabotones=(self.boti1,self.boti2,self.boti3,self.boti4,self.boti5,self.boti6,self.boti7,self.boti8,self.boti9,self.boti10,self.boti11,self.boti12,self.boti13,self.boti14,self.boti15)
		self.momentosintervalo=(0,3,6,9,11,14,17,21,24,27,30,33,36,39,41,44,47,50,53,56,59,61,64,67,71,74,77,80,83,86,89,91,94,97)
	def suma_items(self):
		self.cantitems=self.cantitems+self.agrega
	def resta_items(self):
		self.cantitems=self.cantitems-self.agrega
		if self.cantitems<0:
			self.cantitems=0

	def suma_compra(self):
		self.totalsuma1=self.itemscant[0]*self.precios[0]+self.itemscant[1]*self.precios[1]+self.itemscant[2]*self.precios[2]+self.itemscant[3]*self.precios[3]+self.itemscant[4]*self.precios[4]+self.itemscant[5]*self.precios[5]+self.itemscant[6]*self.precios[6]+self.itemscant[7]*self.precios[7]+self.itemscant[8]*self.precios[8]
		self.totalsuma2=self.itemscant[9]*self.precios[9]+self.itemscant[10]*self.precios[10]+self.itemscant[11]*self.precios[11]+self.itemscant[12]*self.precios[12]+self.itemscant[13]*self.precios[13]+self.itemscant[14]*self.precios[14]
		self.totalsuma=self.totalsuma1+self.totalsuma2
	def update(self,superficie,cursor,intervalo):
		superficie.blit(self.menu,self.rect)

		if self.bot_mas10.T==1:
			self.agrega=10
		if self.bot_mas100.T==1:
			self.agrega=100
		if self.bot_mas10.T==0 and self.bot_mas100.T==0:
			self.agrega=1

		if self.bot_vac.T==1:
			self.cantitems=0

		self.suma_compra()

		if self.bot_fle2.T==1:
			for i in self.momentosintervalo:
				if i==intervalo:
					self.suma_items()

		if self.bot_fle1.T==1:
			for i in self.momentosintervalo:
				if i==intervalo:
					self.resta_items()


		

		self.boti1.update(superficie,cursor)
		self.boti2.update(superficie,cursor)
		self.boti3.update(superficie,cursor)
		self.boti4.update(superficie,cursor)
		self.boti5.update(superficie,cursor)
		self.boti6.update(superficie,cursor)
		self.boti7.update(superficie,cursor)
		self.boti8.update(superficie,cursor)
		self.boti9.update(superficie,cursor)
		self.boti10.update(superficie,cursor)
		self.boti11.update(superficie,cursor)
		self.boti12.update(superficie,cursor)
		self.boti13.update(superficie,cursor)
		self.boti14.update(superficie,cursor)
		self.boti15.update(superficie,cursor)

		superficie.blit(self.texttit,(180,110))

		for i in self.listabotones:
			if i.T==0:
				superficie.blit(self.text1,(110,285))
				superficie.blit(self.text2,(110,305))
				superficie.blit(self.text3,(110,325))
				superficie.blit(self.text4,(110,345))
				superficie.blit(self.text5,(110,365))
				superficie.blit(self.text6,(110,390))
				superficie.blit(self.text7,(110,415))
				superficie.blit(self.text8,(110,435))
				superficie.blit(self.text9,(110,455))
				superficie.blit(self.text10,(110,475))
				superficie.blit(self.text11,(110,495))
				superficie.blit(self.text12,(110,518))
				superficie.blit(self.text13,(110,540))
				superficie.blit(self.text14,(110,560))
				superficie.blit(self.text15,(110,582))


				superficie.blit(self.textp1,(220,285))
				superficie.blit(self.textp2,(220,305))
				superficie.blit(self.textp3,(220,325))
				superficie.blit(self.textp4,(220,345))
				superficie.blit(self.textp5,(220,365))
				superficie.blit(self.textp6,(220,390))
				superficie.blit(self.textp7,(220,415))
				superficie.blit(self.textp8,(220,435))
				superficie.blit(self.textp9,(220,455))
				superficie.blit(self.textp10,(220,475))
				superficie.blit(self.textp11,(220,495))
				superficie.blit(self.textp12,(220,518))
				superficie.blit(self.textp13,(220,540))
				superficie.blit(self.textp14,(220,560))
				superficie.blit(self.textp15,(220,582))


		for i in self.listabotones:
			if i.T==1:
				superficie.blit(self.textb1,(110,285))
				superficie.blit(self.textb2,(110,305))
				superficie.blit(self.textb3,(110,325))
				superficie.blit(self.textb4,(110,345))
				superficie.blit(self.textb5,(110,365))
				superficie.blit(self.textb6,(110,390))
				superficie.blit(self.textb7,(110,415))
				superficie.blit(self.textb8,(110,435))
				superficie.blit(self.textb9,(110,455))
				superficie.blit(self.textb10,(110,475))
				superficie.blit(self.textb11,(110,495))
				superficie.blit(self.textb12,(110,518))
				superficie.blit(self.textb13,(110,540))
				superficie.blit(self.textb14,(110,560))
				superficie.blit(self.textb15,(110,582))

				superficie.blit(self.textbp1,(220,285))
				superficie.blit(self.textbp2,(220,305))
				superficie.blit(self.textbp3,(220,325))
				superficie.blit(self.textbp4,(220,345))
				superficie.blit(self.textbp5,(220,365))
				superficie.blit(self.textbp6,(220,390))
				superficie.blit(self.textbp7,(220,415))
				superficie.blit(self.textbp8,(220,435))
				superficie.blit(self.textbp9,(220,455))
				superficie.blit(self.textbp10,(220,475))
				superficie.blit(self.textbp11,(220,495))
				superficie.blit(self.textbp12,(220,518))
				superficie.blit(self.textbp13,(220,540))
				superficie.blit(self.textbp14,(220,560))
				superficie.blit(self.textbp15,(220,582))

				if i==self.boti1:
					superficie.blit(items.imagengral.subsurface(items.armas1[0]),(170,175))
					superficie.blit(self.textd1,(110,230))
					if self.cantitems>0:
						self.listacompra[0]=self.text1
						self.itemscant[0]=self.cantitems
					if self.cantitems==0:
						self.listacompra[0]=0
						self.itemscant[0]=0
					
				if i==self.boti2:
					superficie.blit(items.imagengral.subsurface(items.armas1[1]),(170,175))
					superficie.blit(self.textd2,(110,230))
					if self.cantitems>0:
						self.listacompra[1]=self.text2
						self.itemscant[1]=self.cantitems
					if self.cantitems==0:
						self.listacompra[1]=0
						self.itemscant[1]=0

				if i==self.boti3:
					superficie.blit(items.imagengral.subsurface(items.armas1[2]),(170,175))
					superficie.blit(self.textd3,(110,230))
					if self.cantitems>0:
						self.listacompra[2]=self.text3
						self.itemscant[2]=self.cantitems
					if self.cantitems==0:
						self.listacompra[2]=0
						self.itemscant[2]=0
				if i==self.boti4:
					superficie.blit(items.imagengral.subsurface(items.armas1[3]),(170,175))
					superficie.blit(self.textd4,(110,230))
					if self.cantitems>0:
						self.listacompra[3]=self.text4
						self.itemscant[3]=self.cantitems
					if self.cantitems==0:
						self.listacompra[3]=0
						self.itemscant[3]=0
				if i==self.boti5:
					superficie.blit(items.imagengral.subsurface(items.armas1[4]),(170,175))
					superficie.blit(self.textd5,(110,230))
					if self.cantitems>0:
						self.listacompra[4]=self.text5
						self.itemscant[4]=self.cantitems
					if self.cantitems==0:
						self.listacompra[4]=0
						self.itemscant[4]=0

				if i==self.boti6:
					superficie.blit(items.imagengral.subsurface(items.armas1[5]),(170,175))
					superficie.blit(self.textd6,(110,230))
					if self.cantitems>0:
						self.listacompra[5]=self.text6
						self.itemscant[5]=self.cantitems
					if self.cantitems==0:
						self.listacompra[5]=0
						self.itemscant[5]=0
				if i==self.boti7:
					superficie.blit(items.imagengral.subsurface(items.armas1[6]),(170,175))
					superficie.blit(self.textd7,(110,230))
					if self.cantitems>0:
						self.listacompra[6]=self.text7
						self.itemscant[6]=self.cantitems
					if self.cantitems==0:
						self.listacompra[6]=0
						self.itemscant[6]=0
				if i==self.boti8:
					superficie.blit(items.imagengral.subsurface(items.armas1[7]),(170,175))
					superficie.blit(self.textd8,(110,230))
					if self.cantitems>0:
						self.listacompra[7]=self.text8
						self.itemscant[7]=self.cantitems
					if self.cantitems==0:
						self.listacompra[7]=0
						self.itemscant[7]=0
				if i==self.boti9:
					superficie.blit(items.imagengral.subsurface(items.armas1[8]),(170,175))
					superficie.blit(self.textd9,(110,230))
					if self.cantitems>0:
						self.listacompra[8]=self.text9
						self.itemscant[8]=self.cantitems
					if self.cantitems==0:
						self.listacompra[8]=0
						self.itemscant[8]=0
				if i==self.boti10:
					superficie.blit(items.imagengral.subsurface(items.armas1[9]),(170,175))
					superficie.blit(self.textd10,(110,230))
					if self.cantitems>0:
						self.listacompra[9]=self.text10
						self.itemscant[9]=self.cantitems
					if self.cantitems==0:
						self.listacompra[9]=0
						self.itemscant[9]=0
				if i==self.boti11:
					superficie.blit(items.imagengral.subsurface(items.armas1[10]),(170,175))
					superficie.blit(self.textd11,(110,230))
					if self.cantitems>0:
						self.listacompra[10]=self.text11
						self.itemscant[10]=self.cantitems
					if self.cantitems==0:
						self.listacompra[10]=0
						self.itemscant[10]=0
				if i==self.boti12:
					superficie.blit(items.imagengral.subsurface(items.armas1[11]),(170,175))
					superficie.blit(self.textd12,(110,230))
					if self.cantitems>0:
						self.listacompra[11]=self.text12
						self.itemscant[11]=self.cantitems
					if self.cantitems==0:
						self.listacompra[11]=0
						self.itemscant[11]=0
				if i==self.boti13:
					superficie.blit(items.imagengral.subsurface(items.armas1[12]),(170,175))
					superficie.blit(self.textd13,(110,230))
					if self.cantitems>0:
						self.listacompra[12]=self.text13
						self.itemscant[12]=self.cantitems
					if self.cantitems==0:
						self.listacompra[12]=0
						self.itemscant[12]=0
				if i==self.boti14:
					superficie.blit(items.imagengral.subsurface(items.armas1[13]),(170,175))
					superficie.blit(self.textd14,(110,230))
					if self.cantitems>0:
						self.listacompra[13]=self.text14
						self.itemscant[13]=self.cantitems
					if self.cantitems==0:
						self.listacompra[13]=0
						self.itemscant[13]=0
				if i==self.boti15:
					superficie.blit(items.imagengral.subsurface(items.armas1[14]),(170,175))
					superficie.blit(self.textd15,(110,230))
					if self.cantitems>0:
						self.listacompra[14]=self.text15
						self.itemscant[14]=self.cantitems
					if self.cantitems==0:
						self.listacompra[14]=0
						self.itemscant[14]=0




		self.iteras1=self.fuente.render(str(self.itemscant[0]),0,(255,255,255))
		self.iteras2=self.fuente.render(str(self.itemscant[1]),0,(255,255,255))
		self.iteras3=self.fuente.render(str(self.itemscant[2]),0,(255,255,255))
		self.iteras4=self.fuente.render(str(self.itemscant[3]),0,(255,255,255))
		self.iteras5=self.fuente.render(str(self.itemscant[4]),0,(255,255,255))
		self.iteras6=self.fuente.render(str(self.itemscant[5]),0,(255,255,255))
		self.iteras7=self.fuente.render(str(self.itemscant[6]),0,(255,255,255))
		self.iteras8=self.fuente.render(str(self.itemscant[7]),0,(255,255,255))
		self.iteras9=self.fuente.render(str(self.itemscant[8]),0,(255,255,255))
		self.iteras10=self.fuente.render(str(self.itemscant[9]),0,(255,255,255))
		self.iteras11=self.fuente.render(str(self.itemscant[10]),0,(255,255,255))
		self.iteras12=self.fuente.render(str(self.itemscant[11]),0,(255,255,255))
		self.iteras13=self.fuente.render(str(self.itemscant[12]),0,(255,255,255))
		self.iteras14=self.fuente.render(str(self.itemscant[13]),0,(255,255,255))
		self.iteras15=self.fuente.render(str(self.itemscant[14]),0,(255,255,255))


		self.textsumatotal=self.fuente.render(str(self.totalsuma),0,(255,255,255))


		for i in self.listacompra:
			if i!=0:
				if i==self.listacompra[0]:
					superficie.blit(self.listacompra[0],(365,285))
					superficie.blit(self.iteras1,(345,285))
				if i==self.listacompra[1]:
					superficie.blit(self.listacompra[1],(365,305))
					superficie.blit(self.iteras2,(345,305))
				if i==self.listacompra[2]:
					superficie.blit(self.listacompra[2],(365,325))
					superficie.blit(self.iteras3,(345,325))
				if i==self.listacompra[3]:
					superficie.blit(self.listacompra[3],(365,345))
					superficie.blit(self.iteras4,(345,345))
				if i==self.listacompra[4]:
					superficie.blit(self.listacompra[4],(365,365))
					superficie.blit(self.iteras5,(345,365))
				if i==self.listacompra[5]:
					superficie.blit(self.listacompra[5],(365,390))
					superficie.blit(self.iteras6,(345,390))
				if i==self.listacompra[6]:
					superficie.blit(self.listacompra[6],(365,415))
					superficie.blit(self.iteras7,(345,415))
				if i==self.listacompra[7]:
					superficie.blit(self.listacompra[7],(365,435))
					superficie.blit(self.iteras8,(345,435))
				if i==self.listacompra[8]:
					superficie.blit(self.listacompra[8],(365,455))
					superficie.blit(self.iteras9,(345,455))

				if i==self.listacompra[9]:
					superficie.blit(self.listacompra[9],(365,475))
					superficie.blit(self.iteras10,(345,475))
				if i==self.listacompra[10]:
					superficie.blit(self.listacompra[10],(365,495))
					superficie.blit(self.iteras11,(345,495))
				if i==self.listacompra[11]:
					superficie.blit(self.listacompra[11],(365,515))
					superficie.blit(self.iteras12,(345,515))
				if i==self.listacompra[12]:
					superficie.blit(self.listacompra[12],(365,535))
					superficie.blit(self.iteras13,(345,535))
				if i==self.listacompra[13]:
					superficie.blit(self.listacompra[13],(365,555))
					superficie.blit(self.iteras14,(345,555))
				if i==self.listacompra[14]:
					superficie.blit(self.listacompra[14],(365,575))
					superficie.blit(self.iteras15,(345,575))




		self.bot_fle1.update(superficie,cursor)
		self.bot_fle2.update(superficie,cursor)
		self.bot_com.update(superficie,cursor)
		self.bot_mas10.update(superficie,cursor)
		self.bot_mas100.update(superficie,cursor)
		self.bot_vac.update(superficie,cursor)
		superficie.blit(self.textsumatotal,(370,245))

