
from  pygame import*



class Gamer(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed) :
        super().__init__()

        self.image = transform .scale(image.load(player_image), (25, 25 )  )
        self.speed = player_speed 


        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, syin_image, syin_x, syin_y, syin_width, syin_heigth) :
        super().__init__()
        
        self.image = transform .scale(image.load(syin_image), (syin_width, syin_heigth )  )  
        

        self.rect = self.image.get_rect()
        self.rect.x = syin_x
        self.rect.y = syin_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class cais(sprite.Sprite):
    def __init__(self, dio_image, dio_x, dio_y) :
        super().__init__()
        
        self.image = transform .scale(image.load(dio_image), (65, 65 )  )  
        

        self.rect = self.image.get_rect()
        self.rect.x = dio_x
        self.rect.y = dio_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_higth = 500 

window = display.set_mode((500, 500))
Clock = time.Clock()

player = Gamer("fff.png", 5 ,win_higth -250, 4)
monster = Gamer("OIP (2).png", win_higth -80, 280, 2)
syin = Wall("gold.png", win_higth -80, 7, 10, 100)
superkej = cais("Сундук_Края.gif",win_higth -80, 5 )
syin1 = Wall("gold.png", win_higth -80, 7, 88, 3)
syin2 = Wall("gold.png", win_higth -20, 18, 10, 100)
syin3 = Wall("gold.png", win_higth -500, 200, 300, 10)
syin4 = Wall("gold.png", win_higth -500, 350, 300, 10)
#syin5 = Wall("gold.png", win_higth -400, 350, 100, 10)
#syin6 = Wall("gold.png", win_higth -400, 200, 100, 10)
#syin7 = Wall("gold.png", win_higth -300, 200, 100, 10)
syin8 = Wall("gold.png", win_higth -200, 100, 10, 100)
syin9 = Wall("gold.png", win_higth -200, 50, 10, 100)
syin10 = Wall("gold.png", win_higth -90, 7, 10, 100)
syin11 = Wall("gold.png", win_higth -200, 50, 88, 3)
syin12 = Wall("gold.png", win_higth -100, 200, 10, 300)
#syin13 = Wall("gold.png", win_higth -300, 350, 100, 10)
syin14 = Wall("gold.png", win_higth -200, 350, 10, 100)
syin15 = Wall("gold.png", win_higth -500, 450, 300, 20)
syin16 = Wall("gold.png", win_higth -100, 150, 10, 100)
syin17 = Wall("gold.png", win_higth -200, 350, 10, 100)




picture = image.load('OIP.png')
resize_img = transform.scale(picture, (700,700))

mixer.init()
music = mixer.music.load("inecraft_droopy.mp3")
music = mixer.music.set_volume(20)
music = mixer.music.play(-1)


dereshen = "up"

won = transform.scale(image.load("al.png"), (700, 500))

while True:
    
    
    for e in event.get():
        if e.type == QUIT:
            exit()

    
        


    ds = key.get_pressed()
    if ds[K_d]:
        player.rect.x += player.speed 
    elif ds[K_a]:
        player.rect.x -= player.speed 
    elif ds[K_w]:
        player.rect.y -= player.speed 
    elif ds[K_s]:
        player.rect.y += player.speed 

    if dereshen == "up":
        monster.rect.y -= monster.speed
        if monster.rect.y <= 100 :
            dereshen = "down" 
    if dereshen == "down" :
        monster.rect.y += monster.speed
        if monster.rect.y >= 400:
            dereshen = "up"
    if player.rect.colliderect(monster.rect):
        player.rect.x = 5 
        player.rect.y = win_higth -250 
    if player.rect.colliderect(syin1.rect) or player.rect.colliderect(syin2.rect) or player.rect.colliderect(syin3.rect) or player.rect.colliderect(syin4.rect) or player.rect.colliderect(syin8.rect)  or player.rect.colliderect(syin9.rect) or player.rect.colliderect(syin10.rect) or player.rect.colliderect(syin11.rect) or player.rect.colliderect(syin12.rect) or player.rect.colliderect(syin14.rect) or player.rect.colliderect(syin15.rect) or player.rect.colliderect(syin16.rect) :
        player.rect.x = 5 
        player.rect.y = win_higth -250 



    
    window.blit(resize_img, (0, 0))



    player.reset()
    monster.reset()
    syin1.reset()
    syin1.reset()
    superkej.reset()
    syin2.reset()
    syin3.reset()
    syin4.reset()
    #syin5.reset()
    #syin6.reset()
    #syin7.reset()
    syin8.reset()
    syin9.reset()
    syin10.reset()
    syin11.reset()
    syin12.reset()
    #syin13.reset()
    syin14.reset()
    syin15.reset()
    syin16.reset()
    
    





    

    if sprite.collide_rect(player, superkej):
        window.blit(won, (000, 000))
 



    display.update()
    Clock.tick(60)


