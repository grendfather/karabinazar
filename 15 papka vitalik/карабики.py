from  pygame import*
import random

font.init()

img_aqo = "61d183263a856e0004c6334a.png"

class Gamer(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, higth ,  player_speed) :
        super().__init__()

        self.image = transform.scale(image.load(player_image), (width, higth )  )
        self.speed = player_speed 


        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

class Player(Gamer):
    global fire_music
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x < win_width - 80:
                self.rect.x += self.speed 
        elif keys[K_a] and self.rect.x > 5:
                self.rect.x -= self.speed 
    
        if keys [K_SPACE]:
            fire_music.play()
            self.fire()
            
    def fire(self):
        bul = Bullet("bul).png" ,self.rect.centerx, self.rect.top, 15, 20, -15) 
        Bullets.append(bul)
        

class ayzen(Gamer):
    
    def update(self) :
        global count_lost
        self.rect.y += self.speed
        if self.rect.y > win_higth + 10 :
            count_lost += 1
            self.rect.y = - 80 
            self.rect.x = random.randint(0, win_width - 80)
            self.speed = random.uniform(5, 5)
            print(count_lost)


class Bullet(Gamer):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <= 0 :
            self.kill()

Bullets = []


count_lost = 0 
win_width = 700
win_higth = 500 


window = display.set_mode((700, 700))
Clock = time.Clock()
monster = []
player = Player("images (1).png",10 ,win_higth -20, 80, 30, 9)
for i in range(5):
    e = ayzen(img_aqo, random.randint(0, win_width - 100), -80, 80, 60, random.uniform(5, 5)  )
    monster.append(e)
    
picture = transform.scale(image.load("OIP.png"), (700, 700))

rachunok = 0 

mixer.init()
music = mixer.music.load("Опенинги Джоджо с 1 по 6 части.mp3")
music = mixer.music.set_volume(20)
music = mixer.music.play(-1)
fire_music = mixer.Sound("udamudamudamudamudamudamudamudamudamuda.ogg")
while True:
    
    
    for c in event.get():
        if c.type == QUIT:
            exit()
    
    
    player.update()






    window.blit(picture, (0, 0))
    player.reset()
    for e in monster:
        e.reset()
        e.update()



    for bul in Bullets:
        bul.update()
        bul.reset()


   
    

    for m in monster:
        m.update ()
        for bul in Bullets:
            if m.rect.colliderect(bul.rect):
                rachunok += 1 
                Bullets.remove(bul)
                m.rect.y = 0
                m.rect.x = random.randint(0, 400)
                break
    if rachunok > 100:
        Ront = font.Font(None, 90 ).render("Винер 288", True, (100,255,100) )
        window.blit(Ront, (200,260) )
    
        



    font.Font(None,12).render("adad", True, (0,0,0))    
    display.update()
    Clock.tick(60)
 