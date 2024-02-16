from pygame import * 

#ігрова сцена:
back = (200, 255, 255)  #колір фону (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

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