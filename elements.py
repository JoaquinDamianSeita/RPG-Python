import pygame,recursos

class cursor(pygame.Rect):
	def __init__(self):
		pygame.Rect.__init__(self,0,0,1,1)
	def update(self):
		self.left,self.top=pygame.mouse.get_pos()

class fondo(pygame.sprite.Sprite):
	def __init__(self):
		self.imagen=recursos.pasto_fondo.convert()
		self.rect=self.imagen.get_rect()
		self.rect.left,self.rect.top=(-100,-100)
	def update(self,pantalla,vx,vy):
		self.rect.move_ip(-vx,-vy)
		pantalla.blit(self.imagen,self.rect)