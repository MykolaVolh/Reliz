from pygame import * 

#Зображення

#створення гравців (список)  
firstplayer = ['player.png' ,'player1.png' ,'player2.png' ,'player3.png', 'player4.png', 'player5.png', 'player6.png', 'player7.png', 'player8.png', 'player9.png']

secondplayer = ['anotherplayer1', 'anotherplayer2', 'anotherplayer3', 'anotherplayer4', 'anotherplayer5', 'anotherplayer6', 'anotherplayer7', 'anotherplayer8', 'anotherplayer9']

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset (self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#ігрова сцена:
back = (200, 255, 255)  #колір фону (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
player = 'player.png'
player2 = 'another'
colona = 'colona.png'

player1 = ('player.png', 50, 200, 50, 50, 5)
colona = ("bullet.png", 15, 20, -15 ) 
player2 = ('anotherplayer1.png', 500, 200, 50, 50, 5)

firstplayer = [Player('player.png',0, 200, 50, 50, 5),Player('player1.png',0, 200, 50, 50, 5),Player('player2.png',0, 200, 50, 50, 5),Player('player3.png',0, 200, 50, 50, 5),Player('player4.png',0, 200, 50, 50, 5),Player('player5.png',0, 200, 50, 50, 5),Player('player6.png',0, 200, 50, 50, 5),Player('player7.png',0, 200, 50, 50, 5)]

secondplayer = [Player('anotherplayer1',0, 200, 50, 50, 5),Player('anotherplayer2',0, 200, 50, 50, 5),Player('anotherplayer3',0, 200, 50, 50, 5),Player('anotherplayer4',0, 200, 50, 50, 5),Player('anotherplayer5',0, 200, 50, 50, 5),Player('anotherplayer6',0, 200, 50, 50, 5),Player('anotherplayer7',0, 200, 50, 50, 5),Player('anotherplayer8',0, 200, 50, 50, 5),Player('anotherplayer9',0, 200, 50, 50, 5)]
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

    # Оновлення стану гравця
    if keys[K_UP]:
        # Оновлення гравця вгору
        pass  # Додайте код для оновлення гравця вгору
    elif keys[K_DOWN]:
        # Оновлення гравця вниз
        pass  # Додайте код для оновлення гравця вниз
    secondplayer[anim_f].draw()
    # Відображення екрану
    display.update()



# Відображення гравців
player1.reset()
player2.reset()

# Відображення екрану
display.update()
# Завершення Pygame
quit()
