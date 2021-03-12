import pygame

class obrero(pygame.sprite.Sprite):
	def __init__(self,x,y,imagen,infx,infy):
		super().__init__()
		self.image=imagen.convert()
		self.rect=self.image.get_rect()
		self.rect.inflate_ip(infx,infy)
		self.rect.left,self.rect.top=(x,y)