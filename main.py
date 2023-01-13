import pygame
import random

pygame.init()
pygame.display.init()
pygame.font.init()

events = pygame.event.get()
window= pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
background = pygame.Surface((600,400))
font_round = pygame.font.Font(pygame.font.get_default_font(), 50)




def affiche(p1_x,p2_x,b_x,b_y, font_round,point_p1,point_p2,): 
    pygame.draw.rect(window , (255,255,255),(0,p1_x,10,50))
    pygame.draw.rect(window , (255,255,255),(600-10,p2_x,10,50))
    i=0
    while i < 400 :
        i+=5
        pygame.draw.rect(window ,(255,255,255),(300-2.5,i,1,1))
            
    pygame.draw.rect(window , (255,255,255),(b_x,b_y,10,10))
    text_p1 = pygame.font.Font.render(font_round,str(point_p1), True, (255,255,255))
    text_p2 = pygame.font.Font.render(font_round,str(point_p2), True, (255,255,255))
    window.blit(text_p1, dest=(270, 0))
    window.blit(text_p2, dest=(300, 0))

def moove(p_y , key1 , key2): 
    if pygame.key.get_pressed()[key1]:
        if p_y < 350  :
            p_y += 2 
            
    if pygame.key.get_pressed()[key2]: 
        if p_y >  0 :
            p_y -=2
    return p_y


def colision(b_x,b_y,b_vector,p1_y,p2_y):
   
# test de bordure 
    if b_y > 400 :
        b_vector[1] = -b_vector[1]
        
    if b_y < 0 :
        b_vector[1] = -b_vector[1]
        
        
 #test de joueur 
    for i in range (50):
        if b_x == 10 and p1_y+i == b_y: 
            b_vector[0] = -b_vector[0]
            
        if b_x == 590 and p2_y+i == b_y :
            b_vector[0] = -b_vector[0]
            
        
    
#tranforme le vecteur en cord 
    b_x = b_x + b_vector[0]
    b_y = b_y + b_vector[1]
    return (b_x,b_y,False)


def point (b_x,point_p1,point_p2):
    if b_x> 600 :  
        point_p1+=1
        
        return [True,point_p1,point_p2]

    if b_x< 0 :
        point_p2+=1
        return [True,point_p1,point_p2]
    return[False,point_p1,point_p2]

def gagne(point_p1,point_p2):
    if point_p1 == 7: 
        return [True, point_p1]
    if point_p2 == 7 :
        return [True,point_p2]

    return [False,point_p1,]





    
#----  main -----
#var--
loop = True 
info_game = ['game_refrech','point_p1','point_p2']
win= [True] 


#boucle
while loop: 
    for event in pygame.event.get(): 
        if event.type ==pygame.QUIT : 
            loop =False

    if  win[0] == True :
        info_game = [True,0,0]
        print("-----start-----")
        
    


    if info_game[0] == True : 
        print("test")
        p1_y = 200-25
        p2_y = 200-25
        time_tick =100

        pos_b=[300,200]
        b_vector=[-1,1]#[random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)]
        info_game[0] =False

    p1_y=moove(p1_y, pygame.K_UP, pygame.K_DOWN )
    p2_y=moove(p2_y, pygame.K_z , pygame.K_s)
    pos_b = colision(pos_b[0],pos_b[1],b_vector,p1_y,p2_y)
    info_game = point(pos_b[0],info_game[1],info_game[2])
    win = gagne(info_game[1],info_game[2])
   


    

    affiche(p1_y ,p2_y,pos_b[0],pos_b[1],font_round,info_game[1],info_game[2])


    pygame.display.flip()

    
    clock.tick(time_tick+0.01)
    #print(clock)
    pygame.display.update()
    window.blit(background,(0,0))
