'''
Calculadora.py
version 0.1
Programa que hace las operaciones basicas en una interfaz grafica.'''
#--------------------------Modulos_Importacion
import pygame, sys
from pygame.locals import *
from sys import exit
pygame.init()
#--------------------------Variables

col1 = 35
col2 = col1 + 45
col3 = col1 + 90

fil1 = 60
fil2 = fil1 + 45
fil3 = fil1 + 90
fil4 = fil1 + 135

#--------------------------Constantes

ancho = 200
alto = 270
tecla = None
tecla_nom = None
#--------------------------funciones
# Clase de tecla
class tecla():
    presionado = False
    encima = False

    def posicion(col = 0,fill = 0):
        return ((col,fill))
    def imagen(tecla = pygame.image.load('calculadora/null.png')):
        return (tecla)
    
def presionada(tecla, pantalla,evento,posicion):
    '''tecla tiene que ser surface --- pantalla: es la pantalla principal'''
    pantalla.blit(tecla,posicion)
    if evento.type ==MOUSEBUTTONDOWN:
        if evento.button ==1:
            print("tecla :",dir(tecla))
            print("tecla :",tecla.__gt__)
            tecla.set_alpha(70)
            tecla.fill((0,0,0))
            pantalla.blit(tecla,posicion)
    return 0

def ponernum(ltecla_nom):
    ''''''
    expresion = []
    letra_arial = pygame.font.SysFont('arial',14)
    pantalla.blit(letra_arial.render())
    pass
    
# Funcion principal
def main():
    '''IMAGENES_BOTONES'''
    cero = pygame.image.load('./calculadora/0.png')
    uno1 = pygame.image.load('./calculadora/1.png')
    dos2 = pygame.image.load('./calculadora/2.png')
    tres3 = pygame.image.load('./calculadora/3.png')
    cuatro4 = pygame.image.load('./calculadora/4.png')
    cinco5 = pygame.image.load('./calculadora/5.png')
    seis6 = pygame.image.load('./calculadora/6.png')
    siete7 = pygame.image.load('./calculadora/7.png')
    ocho8 = pygame.image.load('./calculadora/8.png')
    nueve9 = pygame.image.load('./calculadora/9.png')
    nullimg = pygame.image.load('./calculadora/null.png')
    '''Tamanio de una tecla'''
    tam_tec = nullimg.get_size()
    '''Imagen pantalla'''
    llita = pygame.image.load('./calculadora/Pantalla.png')
    cllita = pygame.transform.scale(llita,(190, 40))
    '''Codigo principal'''
    ready = True
    pantalla = pygame.display.set_mode((ancho,alto))
    while ready ==True:
        #for evento in pygame.event.get():
        evento = pygame.event.wait()
        if evento.type == QUIT:
            pygame.event.clear()
            print("Saliendo...")
            pygame.display.quit()
            exit()
        
        '''Relleno'''
        pantalla.fill((225,225,225))
        '''Pantallita'''
        pantalla.blit(cllita,(5,10)) 
        '''Numeros a pantalla'''
        pantalla.blit(siete7,(col1,fil1))
        pantalla.blit(ocho8,(col2,fil1))
        pantalla.blit(nueve9,(col3,fil1))
        pantalla.blit(cuatro4,(col1,fil2))
        pantalla.blit(cinco5,(col2,fil2))
        pantalla.blit(seis6,(col3,fil2))
        pantalla.blit(uno1,(col1,fil3))
        pantalla.blit(dos2,(col2,fil3))
        pantalla.blit(tres3,(col3,fil3))
        pantalla.blit(cero,(col2,fil4))
        if evento.type == KEYDOWN:
            if evento.key == K_a:
                print(dir(siete7))
        mouse_pos = pygame.mouse.get_pos()#obtengo la posicion del mouse

        arriba = False
        '''Fragmento de codigo que da el efecto de estar sobre una tecla'''
        #Tecla 7
        if(mouse_pos[0] >=col1 and mouse_pos[1] >= fil1 and mouse_pos[0]<=(col1 + tam_tec[0]) and mouse_pos[1]<=(fil1 + tam_tec[1])):
            arriba = True
            siete7_a = pygame.transform.smoothscale(siete7,(tam_tec[0]+6,tam_tec[1]+6))
            siete7_p = (col1-3,fil1-3)
            presionada(siete7_a, pantalla, evento,siete7_p) 
                                    
        #Tecla 8
        if(mouse_pos[0] >=col2 and mouse_pos[1] >= fil1 and mouse_pos[0]<=(col2 + tam_tec[0]) and mouse_pos[1]<=(fil1 + tam_tec[1])):
            arriba = True
            ocho8_a = pygame.transform.smoothscale(ocho8,(tam_tec[0]+6,tam_tec[1]+6))
            ocho8_p = (col2-3,fil1-3)
            presionada(ocho8_a, pantalla, evento,ocho8_p) 
        #Tecla 9
        if(mouse_pos[0] >=col3 and mouse_pos[1] >= fil1 and mouse_pos[0]<=(col3 + tam_tec[0]) and mouse_pos[1]<=(fil1 + tam_tec[1])):
            arriba = True
            nueve9_a = pygame.transform.smoothscale(nueve9,(tam_tec[0]+6,tam_tec[1]+6))
            nueve9_p = (col3-3,fil1-3)
            presionada(nueve9_a, pantalla, evento,nueve9_p) 
        #Tecla 4
        if(mouse_pos[0] >=col1 and mouse_pos[1] >= fil2 and mouse_pos[0]<=(col1 + tam_tec[0]) and mouse_pos[1]<=(fil2 + tam_tec[1])):
            arriba = True
            cuatro4_a = pygame.transform.smoothscale(cuatro4,(tam_tec[0]+6,tam_tec[1]+6))
            cuatro4_p = (col1-3,fil2-3)
            presionada(cuatro4_a, pantalla, evento,cuatro4_p)
        #Tecla 5
        if(mouse_pos[0] >=col2 and mouse_pos[1] >= fil2 and mouse_pos[0]<=(col2 + tam_tec[0]) and mouse_pos[1]<=(fil2 + tam_tec[1])):
            arriba = True
            cinco5_a = pygame.transform.smoothscale(cinco5,(tam_tec[0]+6,tam_tec[1]+6))
            cinco5_p = (col2-3,fil2-3)
            presionada(cinco5_a, pantalla, evento,cinco5_p)
        #Tecla 6
        if(mouse_pos[0] >=col3 and mouse_pos[1] >= fil2 and mouse_pos[0]<=(col3 + tam_tec[0]) and mouse_pos[1]<=(fil2 + tam_tec[1])):
            arriba = True
            seis6_a = pygame.transform.smoothscale(seis6,(tam_tec[0]+6,tam_tec[1]+6))
            seis6_p = (col3-3,fil2-3)
            presionada(seis6_a, pantalla, evento,seis6_p)
        #Tecla 1
        if(mouse_pos[0] >=col1 and mouse_pos[1] >= fil3 and mouse_pos[0]<=(col1 + tam_tec[0]) and mouse_pos[1]<=(fil3 + tam_tec[1])):
            arriba = True
            uno1_a = pygame.transform.smoothscale(uno1,(tam_tec[0]+6,tam_tec[1]+6))
            uno1_p = (col1-3,fil3-3)
            presionada(uno1_a, pantalla, evento,uno1_p)
        #Tecla 2
        if(mouse_pos[0] >=col2 and mouse_pos[1] >= fil3 and mouse_pos[0]<=(col2 + tam_tec[0]) and mouse_pos[1]<=(fil3 + tam_tec[1])):
            arriba = True
            dos2_a = pygame.transform.smoothscale(dos2,(tam_tec[0]+6,tam_tec[1]+6))
            dos2_p = (col2-3,fil3-3)
            presionada(dos2_a, pantalla, evento,dos2_p)
        #Tecla 3
        if(mouse_pos[0] >=col3 and mouse_pos[1] >= fil3 and mouse_pos[0]<=(col3 + tam_tec[0]) and mouse_pos[1]<=(fil3 + tam_tec[1])):
            arriba = True
            tre3_a = pygame.transform.smoothscale(tres3,(tam_tec[0]+6,tam_tec[1]+6))
            tre3_p = (col3-3,fil3-3)
            presionada(tre3_a, pantalla, evento,tre3_p)
        #Tecla 0
        if(mouse_pos[0] >=col2 and mouse_pos[1] >= fil4 and mouse_pos[0]<=(col2 + tam_tec[0]) and mouse_pos[1]<=(fil4 + tam_tec[1])):
            arriba = True
            cero_a = pygame.transform.smoothscale(cero,(tam_tec[0]+6,tam_tec[1]+6))
            cero_p = (col2-3,fil4-3)
            presionada(cero_a, pantalla, evento,cero_p)
        '''Fin fragmento sobre de'''   
        pygame.display.update()

        
        

if __name__ == '__main__':
    main()
