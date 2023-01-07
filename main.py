import pygame
import random

pygame.init()
events = pygame.event.get()
pygame.display.init()
window= pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
background = pygame.Surface((600,400))


def affiche(p1_x,p2_x,b_x,b_y): 
    pygame.draw.rect(window , (255,255,255),(0,p1_x,10,50))
    pygame.draw.rect(window , (255,255,255),(600-10,p2_x,10,50))
    pygame.draw.circle(window,(255,255,255),(b_x,b_y,),(10) )

def moove(p_x , key1 , key2): 
    if pygame.key.get_pressed()[key1]:
        if p_x < 350  :
            p_x += 2 
            print(p_x)
    if pygame.key.get_pressed()[key2]: 
        if p_x >  0 :
            p_x -=2
    return p_x


def ball(b_x,b_y,b_vector):
   
# test de bordure 
    if b_x > 600 :
        b_vector[0] = -b_vector[0]
        print("eeeeeeee")
    if b_x < 0 :
        b_vector[0] = -b_vector[0]
        print("eeeeeeee")
    if b_y > 400 :
        b_vector[1] = -b_vector[1]
        print("eeeeeeee")
    if b_y < 0 :
        b_vector[1] = -b_vector[1]
        print("eeeeeeee")
#tranforme le vecteur en cord 
    b_x = b_x + b_vector[0]
    b_y = b_y + b_vector[1]
    return (b_x,b_y)

    
#----  main -----
#var--
loop= True 
game_start =True
win=False 

#boucle
while loop: 
    for event in pygame.event.get(): 
        if event.type ==pygame.QUIT : 
            loop =False
            
    if win == True : 
        game_start=True



    if game_start == True  : 
        p1_x = 200-25
        p2_x = 200-25
        pos_b=[300,200]
        b_vector=[random.uniform(0.0,1.0),random.uniform(0.0,1.0)]

        print("-----start-----")
        game_start=False

    p1_x=moove(p1_x, pygame.K_UP, pygame.K_DOWN )
    p2_x=moove(p2_x, pygame.K_z , pygame.K_s)
    pos_b = ball(pos_b[0],pos_b[1],b_vector)

    affiche(p1_x ,p2_x,pos_b[0],pos_b[1])


    pygame.display.flip()
    clock.tick(1)
    print(clock)
    pygame.display.update()
    window.blit(background,(0,0))