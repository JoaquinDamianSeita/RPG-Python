import pygame
import gui
import constructor
import recursos
import player
import enemigos
import ataques
import elements


def main():

	#inicio basico del juego
	pygame.init()
	xpan=1200
	ypan=700
	pantalla=pygame.display.set_mode((xpan,ypan))
	salir=False
	reloj1=pygame.time.Clock()
	player1=player.player(ypan/2,xpan/2)#llamo a la clase player,hereda self e imagen y metodos
	cursor1=elements.cursor()
	ataquecuerpo=ataques.ataque_melee()



	tiendacomida=gui.tienda_comidas()
	tiendahechizos=gui.tienda_hechizos()
	tiendaarmas1=gui.tienda_armas1()


	menucirular=gui.menu_circulo()

	menuabro=False

	lobo1=enemigos.lobo_enemigo(450,2200,-170,-170)
	oso1=enemigos.oso_enemigo(800,3000,-100,-100)
	#asset_url18=resource_path("C:/Users/T-800/Desktop/Proyectos Python/Pygame/testexe/imagenes/7.mp3")
	
	#pygame.mixer.music.load(asset_url18)
	#pygame.mixer.music.play(-1)
	fondo1=elements.fondo()

	global tiempo
	global intervalo

	ataquemelee=False
	clickizquierdo=False
	tiendaactiva1,tiendaactiva2,tiendaactiva3=False,False,False
	hechizosactivo,inventarioactivo=False,False
	Dopreta,Rapreta,Lapreta,Upreta=False,False,False,False
	tiempo=0
	intervalo=0

	def reloj_tiempo():
		global tiempo
		cont=6
		if cont==tiempo:
			tiempo=0

	def reloj_intervalo():
		global intervalo
		cont=100
		if cont==intervalo:
			intervalo=0


	#--------variables que suavizan movimiento
	

	vx=0
	vy=0#aca defino los vectores de la velocidad
	rect_update=pygame.Rect(0,0,1200,700)


	#------------------------------defino la GUI
	imagen_hechizos=recursos.ventanahechizos.convert()
	hechizos_menu=gui.menu_hechizos(imagen_hechizos,800,448)

	usuariointerfaz=gui.interfaz_usuario(0,0)
	equipamento_cuadro=gui.equipamento(120,120)
	inventario_cuadro=gui.inventario(140,180)

	vida_barra=recursos.barravida.convert()
	barra_vida=gui.barras_estado(vida_barra,127,38)

	mana_barra=recursos.barramana.convert()
	barra_mana=gui.barras_estado(mana_barra,127,63)

	exp_barra=recursos.barraexp.convert()
	barra_exp=gui.barras_exp(exp_barra,141,101)

	#-------------------grupos de sprites y lista de la interfaz
	lista_anclado=[]
	lista_techos=pygame.sprite.Group()
	lista_puertas=pygame.sprite.Group()
	lista_pisos_puertas_techos=pygame.sprite.Group()
	lista_pisos=pygame.sprite.Group()
	lista_paredatras=pygame.sprite.Group()
	lista_paredescostado=pygame.sprite.Group()
	lista_paredfrente=pygame.sprite.Group()
	lista_bloqueofrente=pygame.sprite.Group()
	lista_sprites_fijos=pygame.sprite.Group()
	lista_enemigos=[]
	
	#------------------llamo al constructor de cosas
	#----------------------casas
	casa1_techo=constructor.obrero(630,295,recursos.techocasa2,0,0)
	casa1_puerta=constructor.obrero(648,446,recursos.puertascasa2,0,0)
	casa1_piso=constructor.obrero(635,350,recursos.pisocasa2,0,0)
	casa1_paredatras=constructor.obrero(634,352,recursos.paredatrascasa2,0,-40)
	casa1_paredcostadoiz=constructor.obrero(634,352,recursos.paredcostadocasa2,0,-50)
	casa1_paredcostadoder=constructor.obrero(806,352,recursos.paredcostadocasa2,0,-50)
	casa1_paredfrente=constructor.obrero(633,446,recursos.paredcasa2,0,-50)
	casa1_bloqueofrente=constructor.obrero(650,500,recursos.bloqueofrentecasa2,0,-5)


	casa2_techo=constructor.obrero(600,695,recursos.techocasa2,0,0)
	casa2_puerta=constructor.obrero(618,846,recursos.puertascasa2,0,0)
	casa2_piso=constructor.obrero(605,750,recursos.pisocasa2,0,0)
	casa2_paredatras=constructor.obrero(604,752,recursos.paredatrascasa2,0,-40)
	casa2_paredcostadoiz=constructor.obrero(604,752,recursos.paredcostadocasa2,0,-50)
	casa2_paredcostadoder=constructor.obrero(776,752,recursos.paredcostadocasa2,0,-50)
	casa2_paredfrente=constructor.obrero(603,846,recursos.paredcasa2,0,-50)
	casa2_bloqueofrente=constructor.obrero(620,900,recursos.bloqueofrentecasa2,0,-5)


	casa3_techo=constructor.obrero(1050,600,recursos.techocasa3,0,0)
	casa3_puerta=constructor.obrero(1050,834,recursos.puertascasa3,0,0)
	casa3_piso=constructor.obrero(1050,670,recursos.pisocasa3,0,0)
	casa3_paredatras=constructor.obrero(1050,670,recursos.paredatrascasa3,0,-40)
	casa3_paredcostadoiz=constructor.obrero(1050,670,recursos.paredcostadocasa3,0,-30)
	casa3_paredcostadoder=constructor.obrero(1350,670,recursos.paredcostadocasa3,0,-30)
	casa3_paredfrente=constructor.obrero(1050,834,recursos.paredcasa3,0,-50)
	casa3_bloqueofrente=constructor.obrero(0,0,recursos.bloqueofrentecasa3,0,-5)

	#--------------fences

	fence_costado1=constructor.obrero(380,180,recursos.fencecostado,0,-30)
	fence_frente1=constructor.obrero(381,235,recursos.fencefrente,0,0)
	fence_costado2=constructor.obrero(380,650,recursos.fencecostado2,0,-30)
	fence_frente2=constructor.obrero(381,1640,recursos.fencefrente,0,0)
	fence_costado3=constructor.obrero(1398,180,recursos.fencecostado,0,-30)
	fence_costado4=constructor.obrero(1398,650,recursos.fencecostado2,0,-30)

	#------------------decoracion

	pino1=constructor.obrero(850,350,recursos.pino,-30,-30)
	pajeral1=constructor.obrero(800,800,recursos.pajeral1,-30,-30)
	cajoncomi1=constructor.obrero(520,880,recursos.cajoncomi,0,-50)
	cajonagua1=constructor.obrero(430,880,recursos.cajonagua,0,-50)
	carretilla1=constructor.obrero(450,780,recursos.carretilla,-30,-30)
	cama1=constructor.obrero(650,390,recursos.cama1,-5,-20)
	biblio1=constructor.obrero(770,360,recursos.biblio1,-5,-15)
	sofa1=constructor.obrero(730,380,recursos.sofa1,-5,-30)
	mesaluz1=constructor.obrero(690,400,recursos.mesa_luz1,-5,-30)
	cuadro1=constructor.obrero(690,360,recursos.cuadro1,-5,-30)
	cama2=constructor.obrero(620,790,recursos.cama1,-5,-20)
	biblio2=constructor.obrero(740,760,recursos.biblio1,-5,-15)
	sofa2=constructor.obrero(700,780,recursos.sofa1,-5,-30)
	mesaluz2=constructor.obrero(660,800,recursos.mesa_luz1,-5,-30)
	cuadro2=constructor.obrero(660,760,recursos.cuadro1,-5,-30)
	cajagrande1=constructor.obrero(550,1048,recursos.caja3,0,-40)
	caja1=constructor.obrero(435,1220,recursos.caja1,0,-40)
	bolsas1=constructor.obrero(530,1220,recursos.bolsas2,0,-40)
	bolsas2=constructor.obrero(675,1220,recursos.bolsas2,0,-40)
	caja2=constructor.obrero(770,1220,recursos.caja2,0,-40)
	caja3=constructor.obrero(675,1070,recursos.caja2,0,-40)
	caja4=constructor.obrero(770,1070,recursos.caja1,0,-40)
	pino2=constructor.obrero(460,650,recursos.pino,-30,-30)
	pino3=constructor.obrero(1000,1000,recursos.pino,-30,-30)
	pino4=constructor.obrero(1250,1100,recursos.pino,-30,-30)
	ropas1=constructor.obrero(1000,450,recursos.ropas,0,-40)
	ropas2=constructor.obrero(1050,1400,recursos.ropas,0,-40)
	excusado1=constructor.obrero(1320,350,recursos.excusado1,0,-40)
	excusado2=constructor.obrero(1050,1500,recursos.excusado1,0,-40)
	hacha1=constructor.obrero(1300,500,recursos.hacha,0,-20)
	pozoagua1=constructor.obrero(1170,1120,recursos.pozoagua,-20,-20)

	#------------puestos y casas fijas

	casafija1=constructor.obrero(1100,300,recursos.casa1,0,-40)
	casafija2=constructor.obrero(670,1400,recursos.casa2,0,-40)
	casafija1b=constructor.obrero(450,1400,recursos.casa1,0,-40)
	casafija1c=constructor.obrero(1150,1400,recursos.casa1,0,-40)
	puestoarmas1=constructor.obrero(450,1000,recursos.puestoarmas,0,-40)
	puestovacio1=constructor.obrero(700,1050,recursos.puestovacio,0,-40)
	puestomagia1=constructor.obrero(460,1200,recursos.puestomagia,0,-40)
	puestocomidas1=constructor.obrero(700,1200,recursos.puestocomidas,0,-40)
	puestotecho1=constructor.obrero(700,1000,recursos.puestotecho,0,0)
	puestotecho2=constructor.obrero(460,1150,recursos.puestotecho,0,0)
	puestotecho3=constructor.obrero(700,1150,recursos.puestotecho,0,0)

	#-----------------------agrego a la lista de la interfaz y a los grupos los sprites


	lis_pisos_puertas_techos=(casa1_techo,casa1_puerta,casa1_piso,casa2_techo,casa2_puerta,casa2_piso,
		casa3_techo,casa3_puerta,casa3_piso,puestotecho1,puestotecho2,puestotecho3)
	for i in lis_pisos_puertas_techos:
		lista_pisos_puertas_techos.add(i)

	lis_sprites_fijos=(fence_costado1,fence_frente1,pino1,pajeral1,cajoncomi1,cajonagua1,	
	carretilla1,cama1,biblio1,sofa1,mesaluz1,cuadro1,cama2,biblio2,sofa2,mesaluz2,cuadro2,fence_costado2,
	fence_frente2,fence_costado3,fence_costado4,casafija1,casafija2,casafija1b,puestoarmas1,puestovacio1,puestomagia1,
	puestocomidas1,cajagrande1,caja1,bolsas1,bolsas2,caja2,caja3,caja4,pino2,pino3,pino4,ropas1,ropas2,casafija1c,
	excusado1,excusado2,hacha1,pozoagua1)
	for i in lis_sprites_fijos:
		lista_sprites_fijos.add(i)

	lis_enemigos=(lobo1,oso1)
	for i in lis_enemigos:
		lista_enemigos.append(i)

	lis_techos=(casa1_techo,casa2_techo,casa3_techo,puestotecho1,puestotecho2,puestotecho3)
	lis_puertas=(casa1_puerta,casa2_puerta,casa3_puerta)
	lis_pisos=(casa1_piso,casa2_piso,casa3_piso)
	lis_paredatras=(casa1_paredatras,casa2_paredatras,casa3_paredatras)
	lis_paredescostado=(casa1_paredcostadoder,casa1_paredcostadoiz,casa2_paredcostadoder,casa2_paredcostadoiz,casa3_paredcostadoder,casa3_paredcostadoiz)
	lis_paredfrente=(casa1_paredfrente,casa2_paredfrente,casa3_paredfrente)
	lis_bloqueofrente=(casa1_bloqueofrente,casa2_bloqueofrente,casa3_bloqueofrente)

	for i in lis_techos:
 		lista_techos.add(i)
	for i in lis_puertas:
 		lista_puertas.add(i)
	for i in lis_pisos:
 		lista_pisos.add(i)
	for i in lis_paredatras:
 		lista_paredatras.add(i)
	for i in lis_paredescostado:
 		lista_paredescostado.add(i)
	for i in lis_paredfrente:
 		lista_paredfrente.add(i)
	for i in lis_bloqueofrente:
 		lista_bloqueofrente.add(i)


#---------------------------listas actualizan el movimiento en el lugar sin colision
	lista_todos_sprites=pygame.sprite.Group()
	lista_todos_sprites.add(lista_sprites_fijos)
	lista_todos_sprites.add(lista_paredatras)
	lista_todos_sprites.add(lista_paredescostado)
	lista_todos_sprites.add(lista_paredfrente)
	lista_todos_sprites.add(lista_bloqueofrente)
	lista_todos_sprites.add(lista_pisos_puertas_techos)


	global velocidad	
	velocidad=10#---------------------aca defino el valor de la velocidad

	#-----------------------sonido del click
	#sonido_click1=pygame.mixer.Sound(recursos.clickson)


	#------------------------bucle while todo los eventos y animaciones aca adentro
	while salir!=True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				salir=True
			if event.type==pygame.KEYDOWN:#----------------movimiento suavizado con teclas
				if event.key==pygame.K_a:
					Lapreta=True#---------------avisa que esta apretada
				if event.key==pygame.K_d:
					Rapreta=True
				if event.key==pygame.K_w:
					Upreta=True
				if event.key==pygame.K_s:
					Dopreta=True
				if event.key==pygame.K_f:
					menuabro=True
				if event.key==pygame.K_LCTRL:
					ataquemelee=True

			if event.type==pygame.KEYUP:
				if event.key==pygame.K_a:
					Lapreta=False
					#------------------avisa que no esta apretada
				if event.key==pygame.K_d:
					Rapreta=False
				if event.key==pygame.K_w:
					Upreta=False
				if event.key==pygame.K_s:
					Dopreta=False
				if event.key==pygame.K_f:
					menuabro=False
				if event.key==pygame.K_LCTRL:
					ataquemelee=False

			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					tiendaactiva1=False
					tiendacomida.listacompra=[0,0,0,0,0,0,0,0,0]
					tiendacomida.itemscant=[0,0,0,0,0,0,0,0,0]
					tiendacomida.cantitems=0

					tiendaactiva2=False
					tiendahechizos.listacompra=[0,0,0,0,0,0,0,0,0]
					tiendahechizos.itemscant=[0,0,0,0,0,0,0,0,0]
					tiendahechizos.cantitems=0

					tiendaactiva3=False
					tiendaarmas1.listacompra=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
					tiendaarmas1.itemscant=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
					tiendaarmas1.cantitems=0

			if event.type==pygame.MOUSEBUTTONDOWN:
				if event.button==1:
					clickizquierdo=True
				

		tiempo+=1
		intervalo+=1
		reloj_intervalo()
		reloj_tiempo()
		reloj1.tick(60)

		#-----------------rellena el display con un color negro
		pantalla.fill((0,0,0))
		#-----------------dibuja el fondo del mapa
		fondo1.update(pantalla,vx,vy)


		#-------------------mueve todas las listas
		for i in lista_todos_sprites:
			i.rect.move_ip(-vx,-vy)
		
		#--------------------orden de dibujado sobre la pantalla y condiciones de colision/dibujo
		lista_pisos.draw(pantalla)
		lista_paredatras.draw(pantalla)
		lista_sprites_fijos.draw(pantalla)
		lista_paredescostado.draw(pantalla)
		if not pygame.sprite.spritecollide(player1,lista_paredfrente,False):
			lista_paredfrente.draw(pantalla)
		player1.update(pantalla,tiempo,fondo1.rect.left,fondo1.rect.top,Dopreta,Upreta,Rapreta,Lapreta)
		lista_puertas.draw(pantalla)

		if not pygame.sprite.spritecollide(player1,lista_techos,False):
			lista_techos.draw(pantalla)

		if pygame.sprite.spritecollide(player1,lista_techos,False) and pygame.sprite.spritecollide(player1,lista_paredfrente,False):
			lista_bloqueofrente.draw(pantalla)



		#--------------------update enemigos
		for i in lista_enemigos:
			i.update(pantalla,player1,player1.rect.left,player1.rect.top,tiempo)
			i.rect.move_ip(-vx,-vy)


			if i.murio==True:
				player1.oro=player1.oro+i.oro
				player1.exp=player1.exp+i.exp
				print(player1.oro)
				lista_enemigos.remove(i)

		#-----------------------------------------------------------
		#-------------------si ataca melee dibuja el aura
		if ataquemelee==True:
			ataquecuerpo.update(pantalla,vx,vy,clickizquierdo,lista_enemigos,player1,intervalo)


		cursor1.update()
		if menuabro==True and menucirular.boton3.boton_actual==menucirular.boton3.boton1 and pygame.mouse.get_pressed()[0]:
			hechizosactivo=True


		if menuabro==True and menucirular.boton1.boton_actual==menucirular.boton1.boton1 and pygame.mouse.get_pressed()[0]:
			inventarioactivo=True

		if hechizosactivo==True:
			hechizos_menu.update(pantalla,cursor1,True)
		if inventarioactivo==True:
			inventario_cuadro.update(pantalla,cursor1)
		if hechizos_menu.bot_cer.T==1:
			hechizosactivo=False
		if inventario_cuadro.bot_cer.T==1:
			inventarioactivo=False
		usuariointerfaz.update(pantalla)
		barra_vida.update(pantalla,player1.hpmax,player1.salud)
		barra_mana.update(pantalla,300,300)
		barra_exp.update(pantalla,player1.expmax,player1.exp)
		equipamento_cuadro.update(pantalla)
		pantalla.blit(player1.textosalud,(220,43))
		pantalla.blit(player1.textooro,(800,8))
		pantalla.blit(player1.textoexp,(230,100))
		pantalla.blit(player1.textolvl,(120,97))
		pantalla.blit(player1.textomana,(220,68))

		if menuabro==True:
			menucirular.update(pantalla,cursor1)



	
		if puestocomidas1.rect.colliderect(cursor1) and pygame.mouse.get_pressed()[0]:
			tiendaactiva1=True

		if puestomagia1.rect.colliderect(cursor1) and pygame.mouse.get_pressed()[0]:
			tiendaactiva2=True

		if puestoarmas1.rect.colliderect(cursor1) and pygame.mouse.get_pressed()[0]:
			tiendaactiva3=True


		if tiendaactiva1==True:
			tiendacomida.update(pantalla,cursor1,intervalo)

		if tiendaactiva2==True:
			tiendahechizos.update(pantalla,cursor1,intervalo)
		if tiendaactiva3==True:
			tiendaarmas1.update(pantalla,cursor1,intervalo)

		for i in lista_enemigos:
			pantalla.blit(i.textosalud,(i.rect.left,i.rect.top))




		#-------------------------detecta colisiones y guarda en una lista grande
		colisiones_pared1=pygame.sprite.spritecollide(player1,lista_paredatras,False)
		colisiones_pared2=pygame.sprite.spritecollide(player1,lista_paredescostado,False)
		colisiones_pared3=pygame.sprite.spritecollide(player1,lista_bloqueofrente,False)
		colisiones_pared4=pygame.sprite.spritecollide(player1,lista_sprites_fijos,False)
		colisiones_paredes=colisiones_pared1+colisiones_pared2+colisiones_pared3+colisiones_pared4

		#define que hacer en caso de que haya colisiones para cada elemento de las listas fondo aparte va
		for i in colisiones_paredes:
			for e in lista_todos_sprites:
				e.rect.move_ip(vx,vy)
			lobo1.rect.move_ip(vx,vy)

			for b in lista_anclado:
				b.rect.move_ip(0,0)
			fondo1.rect.move_ip(vx,vy)



		if intervalo==50:
			for i in lista_enemigos:
				if i.rect.colliderect(player1.rect):
					player1.salud=player1.salud-i.danio
					player1.text1=str(player1.salud)
					player1.text2="/"
					player1.text3=str(player1.hpmax)
					player1.fuente=pygame.font.Font(None,15)
					player1.textosalud=player1.fuente.render(player1.text1+player1.text2+player1.text3,0,(255,255,255))
			
				

		

		#ingresar las ordenes que dibujan en la pantalla
		pygame.display.update(rect_update)


	pygame.quit()







main()