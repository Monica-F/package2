import pygame
import pygame.locals as locals
import random
import datetime


FPS = 50
WINDOW_SIZE=(1080, 720)
GAME_ICON = pygame.image.load("./icon.png")
# pygame.mixer.init()
# BGM1 = pygame.mixer.Sound("./bgm1.wav")

class Game(object):
    def __init__(self):
        self.surface = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption('Coming Home 归途')
        pygame.display.set_icon(GAME_ICON)

        # BGM1.play(loops= 50)
        self.clock = pygame.time.Clock()
        self.game_start = False
    def init(self):
        self.background= Background()
        self.background_wall = Background_Wall()
        self.background_wall2 = Background_Wall2()
        self.background_wall3 = Background_Wall3()
        self.bgm = Bgm()
        self.issac = Issac()
        self.mainmenu= MainMenu()
        self.level2_pre = Level2_pre()
        self.level3_pre = Level3_pre()
        self.ending_pre =Ending_pre()
        self.graves=[]
        self.cliffs=[]
        self.background_level2 = Background_level2()
        self.background_level3 = Background_level3()
        self.ending_background = Ending_background()
        self.ending_animation = Ending_animation()
        self.traps=[]
        self.platforms=[]
        self.monsters=[]
        self.level2 = False
        self.level3 = False
        self.current_level = 1
        self.TIME = 0
        self.TIME2 = 0
        self.TIME3 = 0
        self.TIME4 = 0

        '''self.grave_factory = GraveFactory()
        self.cliff_factory = CliffFactory()'''

        self.is_running = True
        self.ivincible_time = 0
        self.time = 0
        self.time2 = 0
        self.time3 = 0
        self.time4 = 0
        self.ENDING = False
        self.ANI = False
    def draw(self):
        self.background.draw(self.surface)
        self.bgm.draw()
        if self.level2 == False and self.level3 == False:
            self.draw_grave(self.surface)
            self.draw_trap(self.surface)
        self.background_wall.draw(self.surface)
        if self.level2 == False and self.level3 == False:
            self.draw_platform(self.surface)
            self.draw_monster(self.surface)
            self.draw_cliff(self.surface)
        self.issac.draw(self.surface)
    def update(self):

        if self.issac.is_dead(self.graves,self.cliffs):
            self.is_running = False
        # if self.time%60 == 0:
        if self.issac.can_take_damage == False:
            self.ivincible_time += 1
        if self.ivincible_time >= 50:
            self.issac.can_take_damage = True
            self.ivincible_time = 0
        self.time += 1
        self.time3 += 1
        self.time2 = random.randint(80,120)
        self.time4 = random.randint(120,150)
        if self.time%self.time2 == 0 and self.level2 == False and self.level3 == False and self.TIME<= 780:
            ran = random.randint(0, 2)
            self.ran_create(ran)
            self.time = 0
        if self.time3%self.time4 ==0 and self.level2 == False and self.level3 ==False and self.TIME<= 780:
            ran1 = random.randint(0, 1)
            self.create_platform()
            if ran1 ==1 :
                self.create_monster()
            self.time3 =0
        # self.create_grave()
        # self.create_cliff()

        self.background.update()
        self.background_wall.update()
        self.bgm.update()

        self.update_graves()
        self.update_cliff()
        self.update_traps()
        self.update_platforms()
        self.update_monsters()
        self.issac.update()
    def draw_level2(self):
        self.background_level2.draw(self.surface)
        self.bgm.draw()
        self.background_wall2.draw(self.surface)
        if self.level3 == False:
            self.draw_trap(self.surface)
            self.draw_grave(self.surface)
            self.draw_platform(self.surface)
            self.draw_monster(self.surface)
            self.draw_cliff(self.surface)
            self.issac.draw(self.surface)


    def draw_level3(self):
        self.background_level3.draw(self.surface)
        self.bgm.draw()
        if self.ENDING == False:
            self.draw_trap(self.surface)
        self.background_wall3.draw(self.surface)
        if self.ENDING == False:
            self.draw_grave(self.surface)
            self.draw_platform(self.surface)
            self.draw_monster(self.surface)
            self.draw_cliff(self.surface)
            self.issac.draw(self.surface)
    def update_level2(self):
        if self.issac.is_dead(self.graves,self.cliffs):
            self.is_running = False
        # if self.time%60 == 0:
        self.time += 1
        self.time3 += 1
        self.time2 = random.randint(40, 80)
        self.time4 = random.randint(120,150)
        if self.time%self.time2 == 0 and self.level2 == True and self.level3 == False and self.TIME2<= 850:
            ran = random.randint(0, 2)
            self.ran_create(ran)
            self.time = 0
        if self.time3%self.time4 ==0 and self.level2 == True and self.level3 == False and self.TIME2<= 850:
            ran1 = random.randint(0, 1)
            self.create_platform()
            if ran1 ==1 :
                self.create_monster()
            self.time3 =0
        # self.create_grave()
        # self.create_cliff()
        self.background_level2.update()
        self.background_wall2.update()
        self.bgm.update()

        self.update_graves()
        self.update_cliff()
        self.update_traps()
        self.update_platforms()
        self.update_monsters()
        self.issac.update()
    def update_ending(self):
        self.ending_background.update()
        self.issac.update()
    def update_level3(self):
        if self.issac.is_dead(self.graves,self.cliffs):
            self.is_running = False
        # if self.time%60 == 0:
        self.time += 1
        self.time3 += 1
        self.time2 = random.randint(40, 80)
        self.time4 = random.randint(120,150)
        if self.time%self.time2 == 0 and self.level2 == True and self.level3 == True and self.TIME3<= 900 :
            ran = random.randint(0, 2)
            self.ran_create(ran)
            self.time = 0
        if self.time3%self.time4 ==0 and self.level2 == True and self.level3 == True and self.TIME3<= 900:
            ran1 = random.randint(0, 1)
            self.create_platform()
            if ran1 ==1 :
                self.create_monster()
            self.time3 =0
        # self.create_grave()
        # self.create_cliff()
        self.background_level3.update()
        self.background_wall3.update()
        self.bgm.update()

        self.update_graves()
        self.update_cliff()
        self.update_traps()
        self.update_platforms()
        self.update_monsters()
        self.issac.update()
    def draw_ending(self):
        self.ending_background.draw(self.surface)
        self.issac.draw(self.surface)

    def ran_create(self,ran):
        if ran == 0:
            return self.create_cliff()
        elif ran == 1:
            return self.create_grave()
        else:
            return self.create_trap()
    def create_grave(self):
            self.graves.append(Grave())
    def draw_grave(self, surface):
        for grave in self.graves:
            grave.draw(surface,self.current_level)
    def update_graves(self):
        index = len(self.graves)-1
        while index >= 0:
            if self.graves[index].need_remove():
                del(self.graves[index])
            else:
                self.graves[index].update()
            index -= 1

    def create_trap(self):
        self.traps.append(Trap())
    def draw_trap(self,surface):
        for trap in self.traps:
            trap.draw(surface, self.current_level)

    def update_traps(self):
        index = len(self.traps) - 1
        while index >= 0:
            if self.traps[index].need_remove():
                del (self.traps[index])
            else:
                self.traps[index].update()
            index -= 1

    def create_platform(self):
        self.platforms.append(Platform())

    def draw_platform(self, surface):
        for platform in self.platforms:
            platform.draw(surface, self.current_level)

    def update_platforms(self):
        index = len(self.platforms) - 1
        while index >= 0:
            if self.platforms[index].need_remove():
                del (self.platforms[index])
            else:
                self.platforms[index].update()
            index -= 1

    def create_cliff(self):
        self.cliffs.append(Cliff())
    def draw_cliff(self, surface):
        for cliff in self.cliffs:
            cliff.draw(surface, self.current_level)
    def update_cliff(self):
        index = len(self.cliffs)-1
        while index >= 0:
            if self.cliffs[index].need_remove():
                del(self.cliffs[index])
            else:
                self.cliffs[index].update()
            index -= 1

    def create_monster(self):
        self.monsters.append(Monster())
    def draw_monster(self, surface):
        for monster in self.monsters:
            monster.draw(surface, self.current_level)

    def update_monsters(self):
        index = len(self.monsters) - 1
        while index >= 0:
            if self.monsters[index].need_remove():
                del (self.monsters[index])
            else:
                self.monsters[index].update()
            index -= 1

    def start(self):
        self.init()
        while self.is_running:
            self.mouse_click()
            self.control()
            pygame.display.update()
            self.clock.tick(FPS)
            if self.game_start == False:
                self.mainmenu.draw(self.surface)
            if self.game_start == True and self.level2 == False and self.level3 == False and self.ENDING == False and self.ANI == False:

                self.TIME +=1
                self.draw()
                self.update()

                if self.TIME >= 1000:
                    self.level2 = True
                    self.current_level = 2
            if self.game_start == True and self.level2 == True and self.level3 == False and self.ENDING == False and self.ANI == False:

                self.TIME2 +=1
                self.draw()
                self.update()
                self.draw_level2()
                self.update_level2()
                self.level2_pre.draw(self.surface)
                self.level2_pre.update()
                if self.TIME2>= 1000:

                    self.level3 = True
                    self.current_level = 3
            if self.game_start == True and self.level2 == True and self.level3 == True and self.ENDING == False and self.ANI == False:
                self.TIME3+=1
                self.draw()
                self.update()
                self.draw_level2()
                self.update_level2()
                self.draw_level3()
                self.update_level3()
                self.level3_pre.draw(self.surface)
                self.level3_pre.update()
                if self.TIME3 >= 1000:
                    self.ENDING = True
            if self.ENDING == True and self.ANI == False:
                self.TIME4 +=1
                self.draw()
                self.update()
                self.draw_level2()
                self.update_level2()
                self.draw_level3()
                self.update_level3()
                self.draw_ending()
                self.update_ending()
                self.ending_pre.draw(self.surface)
                self.ending_pre.update()
                if self.TIME4 >= 350:
                    self.ANI = True
            if self.ANI == True:
                self.ending_animation.draw(self.surface)
    def mouse_click(self):
        buttons = pygame.mouse.get_pressed()
        x1,y1 =pygame.mouse.get_pos()
        # if self.mainmenu.MainMenu_IMG.x <= x1 <= self.mainmenu.MainMenu_IMG.x+self.mainmenu.MainMenu_IMG.width\
        #         and self.mainmenu.MainMenu_IMG.y <= y1 <= self.mainmenu.MainMenu_IMG.y+self.mainmenu.MainMenu_IMG.height\
        #         and buttons[0] == True:
        if 460 <= x1 <= 617 and 400 <= y1 <= 440 and buttons[0] == True:
            self.game_start = True

    def control(self):
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                exit()
            if event.type == locals.KEYDOWN:
                if event.key == locals.K_SPACE:
                    self.issac.jump()

class Background_Wall(object):
    WALL_IMG1 = pygame.image.load("./level1_img/wall1.png")
    WALL_IMG2 = pygame.image.load("./level1_img/wall1.png")
    def __init__(self):
        self.width = Background_Wall.WALL_IMG1.get_width()
        self.x1 = 0
        self.y1 = 560
        self.x2 =1080
        self.y2 = 560
        self.speed = 5
    def init(self):
        pass
    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed
        if self.need_reset_wall1_1() == True:
            self.x1 = 1080
        if self.need_reset_wall1_2() == True:
            self.x2 = 1080
    def draw(self, surface):
        surface.blit(self.WALL_IMG1, (self.x1, self.y1))
        surface.blit(self.WALL_IMG2, (self.x2, self.y2))

    def need_reset_wall1_1(self):
        if self.x1 <= -self.width:
            return True
        else:
            return False
    def need_reset_wall1_2(self):
        if self.x2 <= -self.width:
            return True
        else:
            return False
    def __del__(self):
        pass

class Background_Wall2(object):
    WALL2_IMG1 = pygame.image.load("./level2_img/wall2.png")
    WALL2_IMG2 = pygame.image.load("./level2_img/wall2.png")

    def __init__(self):
        self.width = Background_Wall.WALL_IMG1.get_width()
        self.x1 = 2160
        self.y1 = 560
        self.x2 = 1080
        self.y2 = 560
        self.speed = 8

    def init(self):
            pass

    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed
        if self.need_reset_wall2_1() == True:
            self.x1 = 1080
        if self.need_reset_wall2_2() == True:
            self.x2 = 1080

    def draw(self, surface):
        surface.blit(self.WALL2_IMG1, (self.x1, self.y1))
        surface.blit(self.WALL2_IMG2, (self.x2, self.y2))

    def need_reset_wall2_1(self):
        if self.x1 <= -self.width:
            return True
        else:
            return False

    def need_reset_wall2_2(self):
        if self.x2 <= -self.width:
            return True
        else:
            return False

    def __del__(self):
        pass

class Background_Wall3(object):
    WALL3_IMG1 = pygame.image.load("./level3_img/wall3.png")
    WALL3_IMG2 = pygame.image.load("./level3_img/wall3.png")

    def __init__(self):
        self.width = Background_Wall.WALL_IMG1.get_width()
        self.x1 = 2160
        self.y1 = 560
        self.x2 = 1080
        self.y2 = 560
        self.speed = 10

    def init(self):
        pass

    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed
        if self.need_reset_wall3_1() == True:
            self.x1 = 1080
        if self.need_reset_wall3_2() == True:
            self.x2 = 1080

    def draw(self, surface):
        surface.blit(self.WALL3_IMG1, (self.x1, self.y1))
        surface.blit(self.WALL3_IMG2, (self.x2, self.y2))

    def need_reset_wall3_1(self):
        if self.x1 <= -self.width:
            return True
        else:
            return False

    def need_reset_wall3_2(self):
        if self.x2 <= -self.width:
            return True
        else:
            return False

    def __del__(self):
        pass
class Level2_pre(object):
    level2_pre_img = pygame.image.load("./level2_img/level2_pre.png")
    def __init__(self):
        self.x = 1200
        self.y = 130
        self.width = Level2_pre.level2_pre_img.get_width()
        self.speed = 3
    def init(self):
        pass
    def update(self):
        self.x -=self.speed
    def need_remove(self):
        if self.x <= -self.width:
            return True
        else:
            return False
    def draw(self,surface):
        surface.blit(self.level2_pre_img,(self.x, self.y))
class Level3_pre(object):
    level3_pre_img = pygame.image.load("./level3_img/level3_pre.png")
    def __init__(self):
        self.x = 1200
        self.y = 130
        self.width = Level3_pre.level3_pre_img.get_width()
        self.speed = 3
    def init(self):
        pass
    def update(self):
        self.x -=self.speed
    def need_remove(self):
        if self.x <= -self.width:
            return True
        else:
            return False
    def draw(self,surface):
        surface.blit(self.level3_pre_img,(self.x, self.y))
class Ending_pre(object):
    ending_pre_img = pygame.image.load("./ending_img/ending_pre.png")
    def __init__(self):
        self.x = 2200
        self.y = 130
        self.width = Ending_pre.ending_pre_img.get_width()
        self.speed = 8
    def init(self):
        pass
    def update(self):
        self.x -=self.speed
    def need_remove(self):
        if self.x <= -self.width:
            return True
        else:
            return False
    def draw(self,surface):
        surface.blit(self.ending_pre_img,(self.x, self.y))
class Background(object):
    background_IMG1 = pygame.image.load("./level1_img/level_1_background.png")
    background_IMG2 = pygame.image.load("./level1_img/level_1_background.png")
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.width = Background.background_IMG1.get_width()
        self.x2 = 1080
        self.y2 = 0
        self.speed = 3
    def init(self):
        pass
    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed

        if self.need_reset_level1_1() == True:
           self.x1 = 1080
        if self.need_reset_level1_2() == True:
           self.x2 = 1080
    def draw(self, surface):
        # surface.fill((200,200,200))
        surface.blit(self.background_IMG1, (self.x1, self.y1))
        surface.blit(self.background_IMG2, (self.x2, self.y2))

    def need_reset_level1_1(self):
        if self.x1 <= -self.width:
            return True
        else:
            return False

    def need_reset_level1_2(self):
        if self.x2 <= -self.width:
            return True
        else:
            return False
    def __del__(self):
        pass
class Background_level3(object):
    background3_IMG1 = pygame.image.load("./level3_img/background_level3.png")
    background3_IMG2 = pygame.image.load("./level3_img/background_level3.png")
    def __init__(self):
        self.x1 = 1080
        self.y1 = 0
        self.width = Background_level3.background3_IMG1.get_width()
        self.x2 = 2160
        self.y2 = 0
        self.speed = 3
    def init(self):
        pass
    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed

        if self.need_reset_level3_1() == True:
           self.x1 = 1080
        if self.need_reset_level3_2() == True:
           self.x2 = 1080
    def draw(self, surface):
        # surface.fill((200,200,200))
        surface.blit(self.background3_IMG1, (self.x1, self.y1))
        surface.blit(self.background3_IMG2, (self.x2, self.y2))

    def need_reset_level3_1(self):
        if self.x1 <= -self.width:
            return True
        else:
            return False

    def need_reset_level3_2(self):
        if self.x2 <= -self.width:
            return True
        else:
            return False
class Background_level2(object):
    background2_IMG1 = pygame.image.load("./level2_img/background_level2.png")
    background2_IMG2 = pygame.image.load("./level2_img/background_level2.png")
    def __init__(self):
        self.x1 = 1080
        self.y1 = 0
        self.width = Background_level2.background2_IMG1.get_width()
        self.x2 = 2160
        self.y2 = 0


        self.speed = 3
    def init(self):
        pass
    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed

        if self.need_reset_level2_1() == True:
           self.x1 = 1080
        if self.need_reset_level2_2() == True:
           self.x2 = 1080
    def draw(self, surface):
        # surface.fill((200,200,200))
        surface.blit(self.background2_IMG1, (self.x1, self.y1))
        surface.blit(self.background2_IMG2, (self.x2, self.y2))

    def need_reset_level2_1(self):
        if self.x1 <= -self.width:
            return True
        else:
            return False

    def need_reset_level2_2(self):
        if self.x2 <= -self.width:
            return True
        else:
            return False
class Bgm(object):
    def __init__(self):
        pass

    def init(self):
        pass

    def draw(self):
        pass
    def update(self):
        pass
class Ending_background(object):
    background_IMG1 = pygame.image.load("./ending_img/1.png")

    def __init__(self):
        self.x = 1080
        self.y = 0
        self.speed = 4
    def init(self):
        pass
    def update(self):
        self.x -= self.speed
        if self.x == 0:
            self.speed =0
    def draw(self, surface):
        surface.blit(self.background_IMG1, (self.x, self.y))



class Obstacle():
    x=0
    y=0
    width=0
    height=0
    img = None
    speed = 0

    def update(self):
        self.x-=self.speed
    def need_remove(self):
        if self.x <= -self.width:
            return True
        else:
            return False
    def init(self):
        pass
    def __del__(self):
        pass
class Trap(Obstacle):
    img = pygame.image.load("./level1_img/trap.png")
    img2 = pygame.image.load("./level2_img/trap2.png")
    img3 = pygame.image.load("./level3_img/trap3.png")
    def __init__(self):
        self.damage=30
        self.x = 1080
        self.y = 500
        self.width = Trap.img.get_width()
        self.height = Trap.img.get_height()
        self.speed = 5
    def draw(self, surface, level):
        if level == 1:
            surface.blit(self.img,(self.x,self.y))
        if level == 2:
            surface.blit(self.img2,(self.x,self.y))
        if level == 3:
            surface.blit(self.img3,(self.x,self.y))
class Cliff(Obstacle):
    img = pygame.image.load("./level1_img/hole.png")
    img2 =pygame.image.load("./level2_img/hole2.png")
    img3 = pygame.image.load("./level1_img/hole.png")
    def __init__(self):
        self.x = 1080
        self.y = 560
        self.width = Cliff.img.get_width()
        self.height = Cliff.img.get_height()
        self.speed = 5
    def draw(self, surface, level):
        if level == 1:
            surface.blit(self.img,(self.x,self.y))
        if level == 2:
            surface.blit(self.img2,(self.x,self.y))
        if level == 3:
            surface.blit(self.img3,(self.x,self.y))
class Grave(Obstacle):
    img = pygame.image.load("./level1_img/cross.png")
    img2 = pygame.image.load("./level2_img/cross2.png")
    img3 = pygame.image.load("./level3_img/cross3.png")
    def __init__(self):
        self.x = 1080
        self.y = 500
        self.width = Grave.img.get_width()
        self.height = Grave.img.get_height()
        self.speed = 5

    def draw(self, surface, level):
        if level == 1:
            surface.blit(self.img, (self.x, self.y))
        if level == 2:
            surface.blit(self.img2, (self.x, self.y))
        if level == 3:
            surface.blit(self.img3, (self.x, self.y))
class Platform(Obstacle):
    img = pygame.image.load("./platform.png")
    img2 = pygame.image.load("./platform.png")
    img3 = pygame.image.load("./platform.png")
    def __init__(self):
        self.x = 1080
        self.y = 410
        self.width = Platform.img.get_width()
        self.height = Platform.img.get_height()
        self.speed = 5
    def draw(self, surface, level):
        if level == 1:
            surface.blit(self.img, (self.x, self.y))
        if level == 2:
            surface.blit(self.img2, (self.x, self.y))
        if level == 3:
            surface.blit(self.img3, (self.x, self.y))
class Monster(Obstacle):
    img = pygame.image.load("./level1_img/monster.png")
    img2 =pygame.image.load("./level2_img/monster2.png")
    img3 = pygame.image.load("./level3_img/monster3.png")
    def __init__(self):
        self.damage = 30
        self.x = 1200
        self.y = 366
        self.width = Monster.img.get_width()
        self.height = Monster.img.get_height()
        self.speed = 5

    def draw(self, surface, level):
        if level == 1:
            surface.blit(self.img, (self.x, self.y))
        if level == 2:
            surface.blit(self.img2, (self.x, self.y))
        if level == 3:
            surface.blit(self.img3, (self.x, self.y))
'''
class ObstacleFactory():
    def create_Obstacle(self, obs_type):
        pass
    def order_Obstacle(self, obs_type):
        obstacle = self.create_Obstacle(obs_type)
        obstacle.init()
        obstacle.draw()
        obstacle.update()
        return  obstacle

class GraveFactory(ObstacleFactory):
    def create_Obstacle(self, obs_type):
        if obs_type == 'grave':
            obstacle = GraveFactory()
        return obstacle

class CliffFactory(ObstacleFactory):
    def create_Obstacle(self, obs_type):
        if obs_type == 'cliff':
            obstacle = CliffFactory()
        return obstacle
'''
class MainMenu(object):
    MainMenu_IMG2 = pygame.image.load("./mainmenu_img/mainmenu_start.png")
    MainMenu_IMG3 = pygame.image.load("./mainmenu_img/background.png")
    def __init__(self):
        self.x2 = 460
        self.y2 = 400
        self.width2 = MainMenu.MainMenu_IMG2.get_width()
        self.height2 = MainMenu.MainMenu_IMG2.get_height()
        self.x3 = 0
        self.y3 = 0
        self.width3 = MainMenu.MainMenu_IMG3.get_width()
        self.height3 = MainMenu.MainMenu_IMG3.get_height()
    def draw(self, surface):
        surface.blit(MainMenu.MainMenu_IMG3, (self.x3, self.y3))
        surface.blit(MainMenu.MainMenu_IMG2, (self.x2, self.y2))
    def __del__(self):
        pass
class Ending_animation(object):
    E1_IMG = pygame.image.load("./ending_img/1.png")
    E2_IMG = pygame.image.load("./ending_img/2.png")
    E3_IMG = pygame.image.load("./ending_img/3.png")
    E4_IMG = pygame.image.load("./ending_img/4.png")
    E5_IMG = pygame.image.load("./ending_img/5.png")
    E6_IMG = pygame.image.load("./ending_img/6.png")
    E7_IMG = pygame.image.load("./ending_img/7.png")
    E8_IMG = pygame.image.load("./ending_img/8.png")
    E9_IMG = pygame.image.load("./ending_img/9.png")
    E10_IMG = pygame.image.load("./ending_img/10.png")
    E11_IMG = pygame.image.load("./ending_img/11.png")
    E12_IMG = pygame.image.load("./ending_img/12.png")
    E13_IMG = pygame.image.load("./ending_img/13.png")
    E14_IMG = pygame.image.load("./ending_img/14.png")
    E15_IMG = pygame.image.load("./ending_img/15.png")
    E16_IMG = pygame.image.load("./ending_img/16.png")
    def __init__(self):
        self.x = 0
        self.y = 0
        self.time = 0
    def draw(self, surface):
        self.time +=1
        if 0<= self.time <=5:
            surface.blit(Ending_animation.E1_IMG, (self.x, self.y))
        if 5 <= self.time <= 10:
            surface.blit(Ending_animation.E2_IMG, (self.x, self.y))
        if 10<= self.time <=15:
            surface.blit(Ending_animation.E3_IMG, (self.x, self.y))
        if 15<= self.time <=20:
            surface.blit(Ending_animation.E4_IMG, (self.x, self.y))
        if 20<= self.time <=25:
            surface.blit(Ending_animation.E5_IMG, (self.x, self.y))
        if 25 <= self.time <= 30:
            surface.blit(Ending_animation.E6_IMG, (self.x, self.y))
        if 30<= self.time <=35:
            surface.blit(Ending_animation.E7_IMG, (self.x, self.y))
        if 35 <= self.time <= 40:
            surface.blit(Ending_animation.E8_IMG, (self.x, self.y))
        if 40 <= self.time <= 45:
            surface.blit(Ending_animation.E9_IMG, (self.x, self.y))
        if 45 <= self.time <= 50:
            surface.blit(Ending_animation.E10_IMG, (self.x, self.y))
        if 50 <= self.time <= 55:
            surface.blit(Ending_animation.E11_IMG, (self.x, self.y))
        if 55 <= self.time <= 60:
             surface.blit(Ending_animation.E12_IMG, (self.x, self.y))
        if 60 <= self.time <= 65:
            surface.blit(Ending_animation.E13_IMG, (self.x, self.y))
        if 65 <= self.time <= 70:
            surface.blit(Ending_animation.E14_IMG, (self.x, self.y))
        if 70 <= self.time <= 75:
            surface.blit(Ending_animation.E15_IMG, (self.x, self.y))
        if self.time>=75:
            surface.blit(Ending_animation.E16_IMG, (self.x, self.y))

    def __del__(self):
        pass
class Issac(object):
    Issac_IMG = pygame.image.load("./character_img/hhhwj.png")
    FULL_HEALTH_IMG=pygame.image.load("./character_img/full_health.png")
    HIGH_HEALTH_IMG=pygame.image.load("./character_img/high_health.png")
    LOW_HEALTH_IMG=pygame.image.load("./character_img/low_health.png")
    EMPTY_HEALTH_IMG=pygame.image.load("./character_img/empty_health.png")
    def __init__(self):
        self.health_x=50
        self.health_y=50
        self.x = 50
        self.y = 500
        self.width = Issac.Issac_IMG.get_width()
        self.height= Issac.Issac_IMG.get_height()
        self.speed = 0
        self.SPACE_NUM = 0
        self.health = 100
        self.can_take_damage = True
        self.knocked = False
        self.take_damage_time = datetime.datetime.now()
    def init(self):
        pass
    def draw(self , surface):
        surface.blit(Issac.Issac_IMG,(self.x, self.y))
        if self.health==100:
            surface.blit(Issac.FULL_HEALTH_IMG,(self.health_x, self.health_y))
        if 60<=self.health<100:
            surface.blit(Issac.HIGH_HEALTH_IMG, (self.health_x, self.health_y))
        if 0<self.health<=60:
            surface.blit(Issac.LOW_HEALTH_IMG, (self.health_x, self.health_y))
        if self.health<=0:
            surface.blit(Issac.EMPTY_HEALTH_IMG, (self.health_x, self.health_y))
    def taking_damage(self, traps, monsters):
        for monster in monsters:
            if self.x + self.width-10 > monster.x \
                    and self.x < monster.x + monster.width\
             and monster.y< self.y + self.height <monster.y+ monster.height  \
                        and self.can_take_damage == True:
                    self.health -= monster.damage
                    self.can_take_damage = False
        for trap in traps:
            if self.x + self.width-10 > trap.x \
                    and self.x < trap.x + trap.width:
                if self.y + self.height > trap.y and self.can_take_damage == True:
                    self.damage = trap.damage
                    self.health -= self.damage
                    self.can_take_damage = False

    def update(self):
        self.y += self.speed
        if self.y >= 510:
            self.speed=0
            self.SPACE_NUM=0
            self.knocked = False
        elif self.speed<=12:
            self.speed += 1
        self.staying(game.platforms)
        self.fall(game.cliffs)
        self.taking_damage(game.traps, game.monsters)
    def jump(self):
        if self.SPACE_NUM < 1:
            self.speed = -18
            self.SPACE_NUM += 1
    def staying(self, platforms):
        for platform in platforms:
            if self.x + self.width > platform.x \
                    and self.x < platform.x + platform.width:
                if  platform.y+platform.height-12<=self.y<=platform.y+platform.height:
                    self.speed = 0
                    self.knocked = True
                if self.knocked == True:
                    self.speed += 1
                elif platform.y<= self.y + self.height <= platform.y+8 :
                    self.speed = 0
                    self.SPACE_NUM = 0

    def fall(self, cliffs):
        for cliff in cliffs:
            if self.x + self.width  > cliff.x \
                    and self.x < cliff.x + cliff.width:
                if self.y + self.height + 10 > cliff.y:
                    self.speed += 1


    def is_dead(self, graves, cliffs):
        if self.y > 680 or self.health <= 0:
            return True
        for grave in graves:
            if self.x + self.width - 10 > grave.x \
                    and self.x +10< grave.x + grave.width:
                if self.y + self.height-15 > grave.y:
                    return True
        for cliff in cliffs:
            if self.x + self.width -10 >= cliff.x +cliff.width\
                    and self.x +10< cliff.x + cliff.width\
                    and self.y + self.height > cliff.y:
                    return True
        return False

if __name__ == '__main__':
    game = Game()
    while True:
        game.start()





