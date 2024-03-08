from pygame import * 

#Зображення

#створення гравців (список)  
firstplayer = [
    transform.scale(image.load('player.png'), (50, 50)),
    transform.scale(image.load('player1.png'), (50, 50)),
    transform.scale(image.load('player2.png'), (50, 50)),
    transform.scale(image.load('player3.png'), (50, 50)),
    transform.scale(image.load('player4.png'), (50, 50)),
    transform.scale(image.load('player5.png'), (50, 50)),
    transform.scale(image.load('player6.png'), (50, 50)),
    transform.scale(image.load('player7.png'), (50, 50)),
    transform.scale(image.load('player8.png'), (50, 50)),
    transform.scale(image.load('player9.png'), (50, 50))]

secondplayer = [image.load('anotherplayer1.png'), 
                image.load('anotherplayer2.png'), 
                image.load('anotherplayer3.png'), 
                image.load('anotherplayer4.png'), 
                image.load('anotherplayer5.png'), 
                image.load('anotherplayer6.png'), 
                image.load('anotherplayer7.png'), 
                image.load('anotherplayer8.png'), 
                image.load('anotherplayer9.png')]

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] :
            self.rect.x -= self.speed
            self.right = True

        elif keys[K_RIGHT] :
            self.right = True
            self.rect.x += self.speed
        else:
            self.right = self.left = False
            
    def update_l(self):
            keys = key.get_pressed()
            if keys[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
                self.left= True
            if keys[K_s] and self.rect.y < win_height - 80:
                self.left= True
                self.rect.y += self.speed
            else:
                self.right = self.left = False

    def animation(self):
        if self.left:
            self.count = (self.count + 1) % len(secondplayer)  
            window.blit(secondplayer[self.count], (self.rect.x, self.rect.y))
        elif self.right:
            self.count = (self.count + 1) % len(firstplayer)  
            window.blit(firstplayer[self.count], (self.rect.x, self.rect.y))
        else:
            self.count=0
            window.blit(secondplayer[self.count], (self.rect.x, self.rect.y))


#ігрова сцена:
back = (200, 255, 255)  #колір фону (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
player = 'player.png'
player2 = 'another'
colona = 'colona.png'

player1 = Player('player.png', 20, 200, 2, 2, 5)
colona = ("colona.jpg", 15, 20, -15 ) 
player2 = Player('anotherplayer1.png', 500, 200, 50, 50, 5)

#firstplayer = [Player('player.png',0, 200, 50, 50, 5),Player('player1.png',0, 200, 50, 50, 5),Player('player2.png',0, 200, 50, 50, 5),Player('player3.png',0, 200, 50, 50, 5),Player('player4.png',0, 200, 50, 50, 5),Player('player5.png',0, 200, 50, 50, 5),Player('player6.png',0, 200, 50, 50, 5),Player('player7.png',0, 200, 50, 50, 5)]

#secondplayer = [Player('anotherplayer1',0, 200, 50, 50, 5),Player('anotherplayer2',0, 200, 50, 50, 5),Player('anotherplayer3',0, 200, 50, 50, 5),Player('anotherplayer4',0, 200, 50, 50, 5),Player('anotherplayer5',0, 200, 50, 50, 5),Player('anotherplayer6',0, 200, 50, 50, 5),Player('anotherplayer7',0, 200, 50, 50, 5),Player('anotherplayer8',0, 200, 50, 50, 5),Player('anotherplayer9',0, 200, 50, 50, 5)]
# Ініціалізація Pygame
init()

# Створення вікна
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Гра")
anim_f=0
# Основний цикл гри
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    # Оновлення екрану
    window.fill(back)
    # Отримання введення користувача
    keys = key.get_pressed()

    player1.reset()
    player1.update()
    player1.animation()

    player2.reset()
    player2.update_l()
    player2.animation()

    

    # Відображення екрану
    display.update()
    time.delay(50)
