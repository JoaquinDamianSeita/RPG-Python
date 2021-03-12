import pygame
import sys
import os



def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

asset_url1=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/fondos/pasto_fondo.gif")


asset_url2=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/hechizos/apoka.png")

asset_url3=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/modelos/plantilla_modelo.png")
asset_url4=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/modelos/aura_ataque.gif")
asset_url5=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/modelos/aura_defensa.gif")


#C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/.gif
asset_url6=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/boton_apocalipsis1.gif")
asset_url7=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/boton_apocalipsis2.gif")
asset_url8=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/boton_info1.gif")
asset_url9=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/boton_info2.gif")
asset_url10=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/Boton_lanzar1.gif")
asset_url11=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/Boton_lanzar2.gif")
asset_url12=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/ventana_hechizos.gif")

asset_url64=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/menucomercio.gif")
asset_url65=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/flechaizquierda.gif")
asset_url66=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/flechaizquierda2.gif")
asset_url67=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/botoncomprarcomercio.gif")
asset_url68=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/botoncomprarcomercio2.gif")
asset_url69=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/flechaderecha.gif")
asset_url70=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/flechaderecha2.gif")
asset_url71=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/botonmas10comercio.gif")
asset_url72=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/botonmas10comercio2.gif")
asset_url73=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/botonmas100comercio.gif")
asset_url74=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/botonmas100comercio2.gif")
asset_url76=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/botitem1.gif")
asset_url77=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/botitem2.gif")
asset_url78=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/vaciarcomercio1.gif")
asset_url79=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/vaciarcomercio2.gif")
asset_url80=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/barravida.gif")
asset_url81=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/barramana.gif")
asset_url82=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/barraexp.gif")
asset_url83=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/cerraricono1.gif")
asset_url84=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/cerraricono2.gif")
asset_url85=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/equipocuadro.gif")
asset_url86=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/inventariomodelo.gif")
asset_url87=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/menucirculo1.gif")
asset_url88=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/menucirculo2.gif")
asset_url89=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/menucirculo3.gif")
asset_url90=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/menucirculo4.gif")
asset_url91=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/menucirculog1.gif")
asset_url92=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/menucirculog2.gif")
asset_url93=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/menucirculog3.gif")
asset_url94=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/menucirculog4.gif")


asset_url13=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/fence_costado.gif")
asset_url14=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/fence_frente.gif")
asset_url15=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/pino.gif")

asset_url16=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/casas/bloqueo_frente_casa2.gif")
asset_url17=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/casa1.gif")
asset_url18=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/casa2.gif")
asset_url19=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/casas/pared_casa2.gif")
asset_url20=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/casas/paredatras_casa2.gif")
asset_url21=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/casas/paredcostado_casa2.gif")
asset_url22=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/casas/piso_casa2.gif")
asset_url23=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/casas/puertas_casa2.gif")
asset_url24=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/casas/techo_casa2.gif")


asset_url50=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/casas/bloqueo_frente_casa3.gif")
asset_url51=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/casas/pared_casa3.gif")
asset_url52=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/casas/paredatras_casa3.gif")
asset_url53=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/casas/paredcostado_casa3.gif")
asset_url54=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/casas/piso_casa3.gif")
asset_url55=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/casas/puertas_casa3.gif")
asset_url56=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/casas/techo_casa3.gif")

asset_url25=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/audio/click.wav")


#C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/.gif
asset_url26=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/pajeral1.gif")
asset_url27=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/cajon1.gif")
asset_url28=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/cajon2.gif")
asset_url29=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/carretilla1.gif")
asset_url30=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/cama1.gif")
asset_url31=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/biblio1.gif")
asset_url32=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/sofa1.gif")
asset_url33=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/mesa_luz1.gif")
asset_url34=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/cuadro1.gif")
asset_url35=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/fence_costado2.gif")
asset_url36=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/puestoarmas.gif")
asset_url37=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/puestotecho.gif")
asset_url38=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/puestovacio1.gif")
asset_url39=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/puestomagia1.gif")
asset_url40=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/puestocomidas1.gif")
asset_url41=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/pozoagua1.gif")
asset_url42=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/ropas1.gif")
asset_url43=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/hacha1.gif")
asset_url44=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/caja3.gif")
asset_url45=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/bolsas3.gif")
asset_url46=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/caja2.gif")
asset_url47=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/caja1.gif")
asset_url48=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/excusado1.gif")
asset_url49=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/Decoracion/bolsas2.gif")





#C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/modelos/.gif
asset_url57=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/modelos/espadaataque1.gif")
asset_url58=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/modelos/espadaataque2.gif")
asset_url59=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/modelos/espadaataque3.gif")
asset_url60=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/modelos/espadaataque4.gif")


#C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/enemigos/.png
asset_url61=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/enemigos/sheetlobo.png")
asset_url63=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/enemigos/sheetoso.png")


#C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/.gif
asset_url62=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/interfaz/interfazusuario.gif")


#C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/items/.gif
asset_url75=resource_path("C:/Users/Florencia/Desktop/Python_joaco/Proyectos Python/Pygame/modelos/lo que ya anda/imagenes/items/items1.gif")


pasto_fondo=pygame.image.load(asset_url1)

apoka=pygame.image.load(asset_url2)

plantillamodelo=pygame.image.load(asset_url3)
auraataque=pygame.image.load(asset_url4)
auradefensa=pygame.image.load(asset_url5)

botapoka1=pygame.image.load(asset_url6)
botapoka2=pygame.image.load(asset_url7)
botinfo1=pygame.image.load(asset_url8)
botinfo2=pygame.image.load(asset_url9)
botlan1=pygame.image.load(asset_url10)
botlan2=pygame.image.load(asset_url11)
ventanahechizos=pygame.image.load(asset_url12)
interfazusuario=pygame.image.load(asset_url62)

fencecostado=pygame.image.load(asset_url13)
fencefrente=pygame.image.load(asset_url14)
fencecostado2=pygame.image.load(asset_url35)
pino=pygame.image.load(asset_url15)

bloqueofrentecasa2=pygame.image.load(asset_url16)
casa1=pygame.image.load(asset_url17)
casa2=pygame.image.load(asset_url18)
paredcasa2=pygame.image.load(asset_url19)
paredatrascasa2=pygame.image.load(asset_url20)
paredcostadocasa2=pygame.image.load(asset_url21)
pisocasa2=pygame.image.load(asset_url22)
puertascasa2=pygame.image.load(asset_url23)
techocasa2=pygame.image.load(asset_url24)

bloqueofrentecasa3=pygame.image.load(asset_url50)
paredcasa3=pygame.image.load(asset_url51)
paredatrascasa3=pygame.image.load(asset_url52)
paredcostadocasa3=pygame.image.load(asset_url53)
pisocasa3=pygame.image.load(asset_url54)
puertascasa3=pygame.image.load(asset_url55)
techocasa3=pygame.image.load(asset_url56)

clickson=asset_url25

pajeral1=pygame.image.load(asset_url26)
cajoncomi=pygame.image.load(asset_url27)
cajonagua=pygame.image.load(asset_url28)
carretilla=pygame.image.load(asset_url29)
cama1=pygame.image.load(asset_url30)
biblio1=pygame.image.load(asset_url31)
sofa1=pygame.image.load(asset_url32)
mesa_luz1=pygame.image.load(asset_url33)
cuadro1=pygame.image.load(asset_url34)
puestoarmas=pygame.image.load(asset_url36)
puestotecho=pygame.image.load(asset_url37)
puestovacio=pygame.image.load(asset_url38)
puestomagia=pygame.image.load(asset_url39)
puestocomidas=pygame.image.load(asset_url40)
pozoagua=pygame.image.load(asset_url41)
ropas=pygame.image.load(asset_url42)
hacha=pygame.image.load(asset_url43)
caja3=pygame.image.load(asset_url44)
bolsas3=pygame.image.load(asset_url45)
caja2=pygame.image.load(asset_url46)
caja1=pygame.image.load(asset_url47)
excusado1=pygame.image.load(asset_url48)
bolsas2=pygame.image.load(asset_url49)

espadaataque1=pygame.image.load(asset_url57)
espadaataque2=pygame.image.load(asset_url58)
espadaataque3=pygame.image.load(asset_url59)
espadaataque4=pygame.image.load(asset_url60)

lobosheet=pygame.image.load(asset_url61)
ososheet=pygame.image.load(asset_url63)

menucomercio=pygame.image.load(asset_url64)
flechaizquierda=pygame.image.load(asset_url65)
flechaizquierda2=pygame.image.load(asset_url66)
botoncomprar=pygame.image.load(asset_url67)
botoncomprar2=pygame.image.load(asset_url68)
flechaderecha=pygame.image.load(asset_url69)
flechaderecha2=pygame.image.load(asset_url70)
botonmas10=pygame.image.load(asset_url71)
botonmas102=pygame.image.load(asset_url72)
botonmas100=pygame.image.load(asset_url73)
botonmas1002=pygame.image.load(asset_url74)
botonitem1=pygame.image.load(asset_url76)
botonitem2=pygame.image.load(asset_url77)
botonvaciar1=pygame.image.load(asset_url78)
botonvaciar2=pygame.image.load(asset_url79)
barravida=pygame.image.load(asset_url80)
barramana=pygame.image.load(asset_url81)
barraexp=pygame.image.load(asset_url82)
cerraricono1=pygame.image.load(asset_url83)
cerraricono2=pygame.image.load(asset_url84)
equipocuadro=pygame.image.load(asset_url85)
inventariomodelo=pygame.image.load(asset_url86)
menucirculo1=pygame.image.load(asset_url87)
menucirculo2=pygame.image.load(asset_url88)
menucirculo3=pygame.image.load(asset_url89)
menucirculo4=pygame.image.load(asset_url90)
menucirculog1=pygame.image.load(asset_url91)
menucirculog2=pygame.image.load(asset_url92)
menucirculog3=pygame.image.load(asset_url93)
menucirculog4=pygame.image.load(asset_url94)



items1=pygame.image.load(asset_url75)