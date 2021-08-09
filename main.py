# Importing Stuffz
import pygame, sys, random, math, time



# That's you
class Player():
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((200, 30, 30))
        self.rect = self.image.get_rect(center=(400, 400))
        self.current_health = 1000
        self.target_health = 1000
        self.max_health = 1000
        self.health_bar_length = 500
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 10
        self.x = 400
        self.y = 320
        self.playerSpeed = 2
        self.img = pygame.image.load('wizardquality.png')
        self.healthpotionsremaining = 5

    def get_damage(self, amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0

    def get_health(self, amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health = self.max_health

    def update(self):
        self.advanced_health()

    def advanced_health(self):
        transition_width = 0
        transition_color = (255, 0, 0)

        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (0, 255, 0)

        if self.current_health > self.target_health:
            self.current_health = self.current_health - self.health_change_speed
            transition_width = int((self.current_health - self.target_health) / self.health_ratio)
            transition_color = (255, 255, 0)

        health_bar_width = int(self.current_health / self.health_ratio)
        health_bar = pygame.Rect(10, 10, health_bar_width, 25)
        transition_bar = pygame.Rect(health_bar.right, 10, transition_width, 25)

        pygame.draw.rect(screen, (255, 0, 0), health_bar)
        pygame.draw.rect(screen, transition_color, transition_bar)
        pygame.draw.rect(screen, (255, 255, 255), (10, 10, self.health_bar_length, 25), 4)

    # Keybinds
    def key_hold(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if player.target_health < player.max_health:
                    self.heal()
                    print("f")
                    print(player.healthpotionsremaining)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.x > -10:
                print('left')
                self.x = self.x - self.playerSpeed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.x < 830:
                print('right')
                self.x = self.x + self.playerSpeed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.y > 305:
                print('up')
                self.y = self.y - self.playerSpeed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.y < 435:
                print('down')
                self.y = self.y + self.playerSpeed
        if keys[pygame.K_q]:
            print('quit')
            running = False

    # Dragonball Damage
    def hitbydragonball(self):
        for balls in dragonballs:
            if int(balls.x) in range(int(self.x), int(self.x) + 32) and balls.y in range(int(self.y), int(self.y) + 64):
                balls.y = -1000
                self.get_damage(100)
        for balls in dragonballs2:
            if int(balls.x) in range(int(self.x), int(self.x) + 32) and balls.y in range(int(self.y), int(self.y) + 64):
                balls.y = -1000
                self.get_damage(100)
        for balls in dragonballs3:
            if int(balls.x) in range(int(self.x), int(self.x) + 32) and balls.y in range(int(self.y), int(self.y) + 64):
                balls.y = -1000
                self.get_damage(100)
    def is_dead(self):
        if self.target_health == 0:
            over_font = pygame.font.Font('freesansbold.ttf', 64)
            over_text = over_font.render("GAME OVER", True, (0, 0, 0))
            screen.blit(over_text, (200, 250))
            pause = input("Game Over")
            pygame.quit()
    def heal(self):
        if self.healthpotionsremaining > 0:
            self.get_health(50)
            self.healthpotionsremaining = self.healthpotionsremaining - 1
    #shoot at mouse
    # def shoot2(self):
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         mouseX, mouseY = pygame.mouse.get_pos()
    #         distanceX = mouseX - self.x
    #         distanceY = mouseY - self.y
    #         angle = math.atan2(distanceY, distanceX)
    #         speedX = 2 * math.cos(angle)
    #         speedY = 2 * math.sin(angle)



# The player's enemy
class Dragon():
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('dragon.png')
        self.fly1 = pygame.image.load('dragonflying1.png')
        self.fly2 = pygame.image.load('dragonflying2.png')
        self.x = random.randint(300, 500)
        self.y = random.randint(60, 70)
        self.speed = 2
        self.health = 1000
        self.animation = 1
        self.choice = 1
    # If dragon gets hit by fireball
    def fireballed(self):
        if fireball.x in range(int(self.x), int(self.x) + 128) and fireball.y in range(int(self.y), int(self.y) + 64):
            fireball.x = -200
            fireball.y = -200
            self.health = self.health - 20
            print('hit', self.health, "hp left")
            if self.health <= 0:
                screen.blit(self.img, (-200, -200))
                win_font = pygame.font.Font('freesansbold.ttf', 64)
                win_text = win_font.render("VICTORY", True, (255, 255, 255))
                screen.blit(win_text, (200, 250))
                dead = input("Victory!")
                pygame.quit()

    # Very awesome and awe inspiring animation
    def flapping(self):
        if 1 <= self.animation < 20:
            screen.blit(dragon.img, (dragon.x, dragon.y))
            screen.blit(dragon.img, (-1000, -1000))
            dragon.dragonballattack()
            self.animation = self.animation + 1
        if 20 <= self.animation < 40:
            screen.blit(dragon.fly1, (dragon.x, dragon.y))
            screen.blit(dragon.fly1, (-1000, -1000))
            dragon.dragonballattack2()
            self.animation = self.animation + 1
        if 40 <= self.animation < 60:
            screen.blit(dragon.fly2, (dragon.x, dragon.y))
            screen.blit(dragon.fly2, (-1000, -1000))
            dragon.dragonballattack3()
            self.animation = self.animation + 1
        if self.animation >= 60:
            self.animation = 1

    def move(self):
        self.x += self.speed
        if self.x <= 100:
            self.speed = 2
            self.y += self.speed
        elif self.x >= 700:
            self.speed = -2
            self.y += self.speed

    def dragonballattack(self):
        for balls in dragonballs:
            if balls.state == True:
                balls.x = random.randint(0, 850)
                balls.y = 20
                screen.blit(balls.img, (balls.x, balls.y))

    def dragonballmovemet(self):
        for balls in dragonballs:
            if balls.y > 500:
                balls.state = True
            else:
                balls.state = False
                balls.y = balls.y + 5
                screen.blit(balls.img, (balls.x, balls.y))

    def dragonballattack2(self):
        for balls in dragonballs2:
            if balls.state == True:
                balls.x = random.randint(0, 850)
                balls.y = 20
                screen.blit(balls.img, (balls.x, balls.y))

    def dragonballmovemet2(self):
        for balls in dragonballs2:
            if balls.y > 500:
                balls.state = True
            else:
                balls.state = False
                balls.y = balls.y + 7
                screen.blit(balls.img, (balls.x, balls.y))

    def dragonballattack3(self):
        for balls in dragonballs3:
            if balls.state == True:
                balls.x = random.randint(0, 850)
                balls.y = 20
                screen.blit(balls.img, (balls.x, balls.y))

    def dragonballmovemet3(self):
        for balls in dragonballs3:
            if balls.y > 500:
                balls.state = True
            else:
                balls.state = False
                balls.y = balls.y + 9
                screen.blit(balls.img, (balls.x, balls.y))




# Target that indicates where Dragon will use lighting attack (might not be used :( )
class Lightning_Indicator():
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('target.png')
        self.x = -100
        self.y = -100

# Player's Attack
class Fireball():
    def __init__(self):
        super().__init__()
        self.x = player.x
        self.y = player.y
        self.speed = 10
        self.img = pygame.image.load('fireball.png')
        # True: Fireball is invisible
        # False: Fireball is visible and has been fired
        self.state = True

    def fire(self):
        if event.type == pygame.MOUSEBUTTONUP:
                print('click')
                global state
                self.state = False
                self.x = int(player.x + 16)
                self.y = int(player.y + 16)
                screen.blit(self.img, (self.x, self.y))

    def fireball_movement(self):
        if self.state == False:
            screen.blit(self.img, (self.x, self.y))
            self.y = self.y - self.speed
        if self.state == True or self.y < 0:
            screen.blit(self.img, (-100, -100))


# DragonBlaze Attack
class Dragonball():
    def __init__(self):
        super().__init__()
        self.x = -1000
        self.y = -1000
        self.speed = 10
        self.img = pygame.image.load('dragonblaze.png')
        self.state = True

potionImg = pygame.image.load('healthpotion.png')

pygame.init()
screen = pygame.display.set_mode((877, 500))
background = pygame.image.load('Space Background.png')
clock = pygame.time.Clock()
player = Player()
dragon = Dragon()
fireball = Fireball()

dragonballs = []
dragonballs2 = []
dragonballs3 = []
# I probably could do something better than this but I don't have time so deal with it
dragonball1 = Dragonball()
dragonballs.append(dragonball1)
dragonball2 = Dragonball()
dragonballs.append(dragonball2)
dragonball3 = Dragonball()
dragonballs.append(dragonball3)
dragonball4 = Dragonball()
dragonballs.append(dragonball4)
dragonball5 = Dragonball()
dragonballs.append(dragonball5)

dragonball6 = Dragonball()
dragonballs2.append(dragonball6)
dragonball7 = Dragonball()
dragonballs2.append(dragonball7)
dragonball8 = Dragonball()
dragonballs2.append(dragonball8)
dragonball9 = Dragonball()
dragonballs2.append(dragonball9)

dragonball10 = Dragonball()
dragonballs3.append(dragonball10)
dragonball11 = Dragonball()
dragonballs3.append(dragonball11)
dragonball12 = Dragonball()
dragonballs3.append(dragonball12)

target = Lightning_Indicator()
pygame.display.set_caption('DragonBlaze')
pygame.display.set_icon(pygame.image.load('wizard.png'))
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)


# Game Loop
while True:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()


    player.update()
    player.key_hold()
    fireball.fire()
    fireball.fireball_movement()
    dragon.fireballed()
    screen.blit(player.img, (player.x, player.y))
    dragon.flapping()
    dragon.move()
    dragon.dragonballmovemet()
    dragon.dragonballmovemet2()
    dragon.dragonballmovemet3()
    player.hitbydragonball()
    player.is_dead()
    screen.blit(target.img, (target.x, target.y))
    screen.blit(potionImg, (20, 416))
    f_font = pygame.font.Font('freesansbold.ttf', 25)
    f_text = f_font.render("F", True, (0, 0, 0))
    screen.blit(f_text, (45, 441))
    pygame.display.update()
    clock.tick(60)