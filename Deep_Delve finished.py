##Deep Delve source code##
##Please change the path variable to your respective file path that holds this file##
##Please don't change any other variable##
##Controls##
##Walk: WASD keys##
##Attack: E key##
##Cannot attack while walking##

import pygame, random
TileSize = 60
MapWidth = 1000
MapHeight = 700
MapComplexity = 20
Enemy_Count = 10
Path = r"C:\Users\Ross\Desktop\Deep Delve" ##Please leave the inital r, as that tells the iterator that this is a raw string#
pygame.init()
Clock = pygame.time.Clock()


Icon = pygame.image.load(Path+"\Deep Delve\Player\\idle_stand (1).png")
pygame.display.set_icon(Icon)
display = pygame.display.set_mode((MapWidth,MapHeight))
pygame.display.set_caption("Deep Delve")

Tile_Hit = pygame.sprite.Group()
Tile_Group = pygame.sprite.Group()
Black_Tile_Group = pygame.sprite.Group()
Player_Group = pygame.sprite.Group()
Boss_Group = pygame.sprite.Group()
Enemy_Group = pygame.sprite.Group()
Entity_Group = pygame.sprite.Group()
Enemy_Spawn_Group = pygame.sprite.Group()


## Setting types of square
class Square_Type(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.finished = False
        self.x = 0
        self.y = 0
        self.Square = None
        self.Dark_Square = None
        self.Player_Spawn = None
        self.Enemy_Spawn = None
        self.Boss_Spawn = None
        self.Boss_Door = None
        self.Player_Door = None
        self.Boss_Room = None
        self.image = None
        self.rect = None
        self.spawned = False
        if self.Square != None or self.Boss_Door != None or self.Player_Door != None or self.Player_Spawn != None or self.Boss_Spawn != None or self.Boss_Room != None:
            self.Empty = False
        else:
            self.Empty = True

class Square():
    def __init__(self):
        self.LeftSide = False
        self.Rightside = False
        self.TopSide = False
        self.BottomSide = False
class Boss_Spawn(Square):
    def __init__(self):
        Square.__init__(self)
class Player_Spawn(Square):
    def __init__(self):
        Square.__init__(self)
class Door(Square):
    def __init__(self):
        Square.__init__(self)

class State_Machine_Core():
    def __init__(self):
        self.__list = []
        self.__image = ""
        self._animation = {
            "Run" : {
                "Player" : [pygame.image.load(Path+"\Deep Delve\Player\\run (1).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (2).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (3).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (4).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (5).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (6).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (7).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (8).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (9).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (10).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (11).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (12).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (13).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (14).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (15).png"),pygame.image.load(Path+"\Deep Delve\Player\\run (16).png")],
                "Enemy": [pygame.image.load(Path+"\Deep Delve\Enemy\\walk (1).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\walk (2).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\walk (3).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\walk (4).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\walk (5).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\walk (6).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\walk (7).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\walk (8).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\walk (9).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\walk (10).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\walk (11).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\walk (12).png")],
                "Boss" : [pygame.image.load(Path+"\Deep Delve\Boss\\walk (1).png"),pygame.image.load(Path+"\Deep Delve\Boss\\walk (2).png"),pygame.image.load(Path+"\Deep Delve\Boss\\walk (3).png"),pygame.image.load(Path+"\Deep Delve\Boss\\walk (4).png"),pygame.image.load(Path+"\Deep Delve\Boss\\walk (5).png"),pygame.image.load(Path+"\Deep Delve\Boss\\walk (6).png"),pygame.image.load(Path+"\Deep Delve\Boss\\walk (7).png"),pygame.image.load(Path+"\Deep Delve\Boss\\walk (8).png"),pygame.image.load(Path+"\Deep Delve\Boss\\walk (9).png"),pygame.image.load(Path+"\Deep Delve\Boss\\walk (10).png"),pygame.image.load(Path+"\Deep Delve\Boss\\walk (11).png"),pygame.image.load(Path+"\Deep Delve\Boss\\walk (12).png")]
                },
            "Attack" : {
                "Player" : [pygame.image.load(Path+"\Deep Delve\Player\\attack_stand (1).png"),pygame.image.load(Path+"\Deep Delve\Player\\attack_stand (2).png"),pygame.image.load(Path+"\Deep Delve\Player\\attack_stand (3).png"),pygame.image.load(Path+"\Deep Delve\Player\\attack_stand (4).png"),pygame.image.load(Path+"\Deep Delve\Player\\attack_stand (5).png"),pygame.image.load(Path+"\Deep Delve\Player\\attack_stand (6).png"),pygame.image.load(Path+"\Deep Delve\Player\\attack_stand (7).png"),pygame.image.load(Path+"\Deep Delve\Player\\attack_stand (8).png"),pygame.image.load(Path+"\Deep Delve\Player\\attack_stand (9).png"),pygame.image.load(Path+"\Deep Delve\Player\\attack_stand (10).png")],
                "Enemy" : [pygame.image.load(Path+"\Deep Delve\Enemy\\attack (1).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\attack (2).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\attack (3).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\attack (4).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\attack (5).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\attack (6).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\attack (7).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\attack (8).png")],
                "Boss" : [pygame.image.load(Path+"\Deep Delve\Boss\\attack (1).png"),pygame.image.load(Path+"\Deep Delve\Boss\\attack (2).png"),pygame.image.load(Path+"\Deep Delve\Boss\\attack (3).png"),pygame.image.load(Path+"\Deep Delve\Boss\\attack (4).png"),pygame.image.load(Path+"\Deep Delve\Boss\\attack (5).png"),pygame.image.load(Path+"\Deep Delve\Boss\\attack (6).png"),pygame.image.load(Path+"\Deep Delve\Boss\\attack (7).png"),pygame.image.load(Path+"\Deep Delve\Boss\\attack (8).png"),pygame.image.load(Path+"\Deep Delve\Boss\\attack (9).png")]
                },
            "Dead" : {
                "Player" : [pygame.image.load(Path+"\Deep Delve\Player\\dead (1).png"),pygame.image.load(Path+"\Deep Delve\Player\\dead (2).png"),pygame.image.load(Path+"\Deep Delve\Player\\dead (3).png"),pygame.image.load(Path+"\Deep Delve\Player\\dead (4).png"),pygame.image.load(Path+"\Deep Delve\Player\\dead (5).png"),pygame.image.load(Path+"\Deep Delve\Player\\dead (6).png"),pygame.image.load(Path+"\Deep Delve\Player\\dead (7).png")],
                "Enemy" : [pygame.image.load(Path+"\Deep Delve\Enemy\\dead (1).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\dead (2).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\dead (3).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\dead (4).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\dead (5).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\dead (6).png")],
                "Boss" : [pygame.image.load(Path+"\Deep Delve\Boss\\dead (1).png"),pygame.image.load(Path+"\Deep Delve\Boss\\dead (2).png"),pygame.image.load(Path+"\Deep Delve\Boss\\dead (3).png"),pygame.image.load(Path+"\Deep Delve\Boss\\dead (4).png"),pygame.image.load(Path+"\Deep Delve\Boss\\dead (5).png")]
                },
            "Idle" : {
                "Player" : [pygame.image.load(Path+"\Deep Delve\Player\\idle_stand (1).png"),pygame.image.load(Path+"\Deep Delve\Player\\idle_stand (2).png"),pygame.image.load(Path+"\Deep Delve\Player\\idle_stand (3).png"),pygame.image.load(Path+"\Deep Delve\Player\\idle_stand (4).png"),pygame.image.load(Path+"\Deep Delve\Player\\idle_stand (5).png"),pygame.image.load(Path+"\Deep Delve\Player\\idle_stand (6).png")],
                "Enemy" : [pygame.image.load(Path+"\Deep Delve\Enemy\\idle (1).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\idle (2).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\idle (3).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\idle (4).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\idle (5).png"),pygame.image.load(Path+"\Deep Delve\Enemy\\idle (6).png")],
                "Boss" : [pygame.image.load(Path+"\Deep Delve\Boss\\idle (1).png"),pygame.image.load(Path+"\Deep Delve\Boss\\idle (2).png"),pygame.image.load(Path+"\Deep Delve\Boss\\idle (3).png"),pygame.image.load(Path+"\Deep Delve\Boss\\idle (4).png"),pygame.image.load(Path+"\Deep Delve\Boss\\idle (5).png"),pygame.image.load(Path+"\Deep Delve\Boss\\idle (6).png")],
                }
            }
    def Get_Animation(self, state):
        self.__list = []
        for Image in range(0,len(self._animation[state][entity_type])):
            self.__image = self._animation[state][entity_type][Image]
            self.__image = pygame.transform.scale(self.__image,(49,50))
            self.__list.append(self.__image)
        return(self.__list)

class Player_machine(State_Machine_Core):
    def __init__(self):
        State_Machine_Core.__init__(self)
    def Get_Animation(self, state):
        self.__list = []
        for Image in range(0,len(self._animation[state]["Player"])):
            self.__image = self._animation[state]["Player"][Image]
            self.__image = pygame.transform.scale(self.__image,(49,50))
            self.__list.append(self.__image)
        return(self.__list)

class Boss_machine(State_Machine_Core):
    def __init__(self):
        State_Machine_Core.__init__(self)
    def Get_Animation(self, state):
        self.__list = []
        for Image in range(0,len(self._animation[state]["Boss"])):
            self.__image = self._animation[state]["Boss"][Image]
            self.__image = pygame.transform.scale(self.__image,(49,50))
            self.__list.append(self.__image)
        return(self.__list)

class Enemy_machine(State_Machine_Core):
    def __init__(self):
        State_Machine_Core.__init__(self)
    def Get_Animation(self, state):
        self.__list = []
        for Image in range(0,len(self._animation[state]["Enemy"])):
            self.__image = self._animation[state]["Enemy"][Image]
            self.__image = pygame.transform.scale(self.__image,(49,50))
            self.__list.append(self.__image)
        return(self.__list)

## Setting entities
class Entity(pygame.sprite.Sprite):
    def __init__(self,display,TileSize,MapWidth,MapHeight,MapComplexity):
        pygame.sprite.Sprite.__init__(self)
        self._tilemap = []
        self.Health = 0
        self._display = display
        self._TileSize = TileSize
        self._MapWidth = MapWidth
        self._MapHeight = MapHeight
        self._MapComplexity = MapComplexity
        self._Dist = 5
        self._Player_Spawn = ()
        self._Boss_Spawn = ()
        self._Enemy_Spawn = ()
        self._dead = False
        self.__finished = False
        self._moving = False
        self._x = 0
        self._y = 0
        self._rect = ""
        self._image = ""
        self.dead = False
        self._images = []
        self._dead_first = False
        self._walk_point = 0
        self._idle_point = 0
        self._dead_point = 0
        self._attack_point = 0
        self.attack = False

    def _Draw(self):
        self._display.blit(image,(x,y))

class Damage():
    def __init__(self,Entity1,Entity2):
        if Entity1.attack:
            self.__RandMultiplier = random.randint(1,5)
            Entity2.Health = Entity2.Health - self.__RandMultiplier
        if Entity2.attack:
            self.__RandMultiplier = random.randint(1,5)
            Entity1.Health = Entity1.Health - self.__RandMultiplier





class Player(Entity):
    def __init__(self,display,TileSize,MapWidth,MapHeight,MapComplexity):
        Entity.__init__(self,display,TileSize,MapWidth,MapHeight,MapComplexity)
        self._image = pygame.image.load(Path+"\Deep Delve\Player\\idle_stand (1).png")
        self._image = pygame.transform.scale(self._image,(49,50))
        self.rect = self._image.get_rect()
        self._x = Map._tilemap[Map._Player_Spawn[0]][Map._Player_Spawn[1]].x
        self._y = Map._tilemap[Map._Player_Spawn[0]][Map._Player_Spawn[1]].y
        self.rect.x = self._x
        self.rect.y = self._y
        self.Health = 300
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.__Machine = Player_machine()
        self.__Wait_Frame = 0
        self.__Caption = ""
    def Move(self):
        if self.Health > 0 and self.dead == False:
            self.up = False
            self.down = False
            self.left = False
            self.right = False
            self.__key = pygame.key.get_pressed()
            if self.__key[pygame.K_s] and self.dead == False:
                self.rect.y = self.rect.y + self._Dist
                if pygame.sprite.spritecollideany(Player,Black_Tile_Group) != None:
                    self.rect.y = self.rect.y - self._Dist
                    self.down = False
                else:
                    self.rect.y = self.rect.y - self._Dist
                    self.down = True
            elif self.__key[pygame.K_w] and self.dead == False:
                self.rect.y = self.rect.y - self._Dist
                if pygame.sprite.spritecollideany(Player,Black_Tile_Group) != None:
                    self.rect.y = self.rect.y + self._Dist
                    self.up = False
                else:
                    self.rect.y = self.rect.y + self._Dist
                    self.up = True
            if self.__key[pygame.K_d] and self.dead == False:
                self.rect.x = self.rect.x + self._Dist
                if pygame.sprite.spritecollideany(Player,Black_Tile_Group) != None:
                    self.rect.x = self.rect.x - self._Dist
                    self.right = False
                else:
                    self.rect.x = self.rect.x - self._Dist
                    self.right = True
            elif self.__key[pygame.K_a] and self.dead == False:
                self.rect.x = self.rect.x - self._Dist
                if pygame.sprite.spritecollideany(Player,Black_Tile_Group) != None:
                    self.rect.x = self.rect.x + self._Dist
                    self.left = False
                else:
                    self.rect.x = self.rect.x + self._Dist
                    self.left = True
            if self.__key[pygame.K_e] and self.dead == False and (self.up == False and self.down == False and self.left == False and self.right == False):
                self.attack = True
        else:
            if self._dead_first == False:
                self._dead_first = True
            self.dead = True
            self.attack = False
            self.up = False
            self.down = False
            self.left = False
            self.right = False
        self.__State_Machine()
    def __State_Machine(self):
        if self._dead_first and self.dead:
            self._images = self.__Machine.Get_Animation("Dead")
            self._image = self._images[self._dead_point]
            self.rect = self._image.get_rect()
            self.rect.x = self._x
            self.rect.y = self._y
            if (self._dead_point + 1) == len(self._images):
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
            else:
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
                self._dead_point = self._dead_point + 1
        elif self.dead:
            self._images = self.__Machine.Get_Animation("Dead")
            self._image = self._images[len(self._images)]
            self.rect = self._image.get_rect()
            self.rect.x = self._x
            self.rect.y = self._y
        elif self.up or self.down or self.left or self.right:
            if self.attack == True:
                self.attack = False
            self._images = self.__Machine.Get_Animation("Run")
            self._image = self._images[self._walk_point]
            self.rect = self._image.get_rect()
            self.rect.x = self._x
            self.rect.y = self._y
            if (self._walk_point + 1) == len(self._images):
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
            else:
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = self._walk_point + 1
        elif self.attack:
            self._images = self.__Machine.Get_Animation("Attack")
            self._image = self._images[self._attack_point]
            self.rect = self._image.get_rect()
            self.rect.x = self._x
            self.rect.y = self._y
            if (self._attack_point + 1)== len(self._images):
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
                self.attack = False
            else:
                self._idle_point = 0
                self._attack_point = self._attack_point + 1
                self._walk_point = 0
        elif self.up == False and self.down == False and self.left == False and self.right == False:
            self._images = self.__Machine.Get_Animation("Idle")
            self._image = self._images[self._idle_point]
            self.rect = self._image.get_rect()
            self.rect.x = self._x
            self.rect.y = self._y
            if (self._idle_point + 1) == len(self._images):
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
            else:
                self._idle_point = self._idle_point + 1
                self._attack_point = 0
                self._walk_point = 0
        self.__Draw()

    def __Draw(self):
        self._display.blit(self._image,(self._x,self._y))
        if self.__Wait_Frame == 40 and self.dead == False:
            self.__Wait_Frame = 0
            self.Health = self.Health + random.randint(10,50)
            if self.Health > 300:
                self.Health = 300
        else:
            self.__Wait_Frame = self.__Wait_Frame + 1
        if self.Health < 0:
            self.Health = 0
        if Boss.Health < 0:
            Boss.Health = 0
        self.__Caption = "Deep Delve - "+"Player Health: "+str(self.Health)+" - Boss Health: "+str(Boss.Health)+" - Enemy Count: "+str(Enemy_Count)
        pygame.display.set_caption(self.__Caption)

class Entity_eyes(Entity):
    def __init__(self,x,y,image):
        Entity.__init__(self,display,TileSize,MapWidth,MapHeight,MapComplexity)
        image = pygame.transform.scale(image,(139,140))
        self.rect = image.get_rect()
        self.rect.x = x - 43
        self.rect.y = y - 35
    def Move(self,x,y):
        self.rect.x = x - 43
        self.rect.y = y - 35

class Boss(Entity):
    def __init__(self,display,TileSize,MapWidth,MapHeight,MapComplexity):
        Entity.__init__(self,display,TileSize,MapWidth,MapHeight,MapComplexity)
        self._image = pygame.image.load(Path+"\Deep Delve\Player\\idle_stand (1).png")
        self._image = pygame.transform.scale(self._image,(49,50))
        self.rect = self._image.get_rect()
        self._x = Map._tilemap[Map._Boss_Spawn[0]][Map._Boss_Spawn[1]].x
        self._y = Map._tilemap[Map._Boss_Spawn[0]][Map._Boss_Spawn[1]].y
        self.__Spawn_X = self._x
        self.__Spawn_Y = self._y
        self.rect.x = self._x
        self.rect.y = self._y
        self.Health = 600
        self.__Wait_Frame = 0
        self.__Machine = Boss_machine()
        self.Eyes = Entity_eyes(self._x,self._y,self._image)
    def Move(self):
        self.__Spawn_X = Map._tilemap[Map._Boss_Spawn[0]][Map._Boss_Spawn[1]].x
        self.__Spawn_Y = Map._tilemap[Map._Boss_Spawn[0]][Map._Boss_Spawn[1]].y
        if self.Health > 0 and self.dead == False:
            self._moving = False
            if pygame.sprite.collide_rect(Player,Boss) == False:
                if pygame.sprite.collide_rect(Player,self.Eyes) == True:
                    if Player._x > self._x:
                        if Player._y > self._y:
                            self._x = self._x + 2
                            self._y = self._y + 2
                            if pygame.sprite.spritecollideany(Boss,Black_Tile_Group) != None:
                                self._x = self._x - 2
                                self._y = self._y - 2
                            else:
                                self._moving = True
                        if Player._y < self._y and self._moving == False:
                            self._x = self._x + 2
                            self._y = self._y - 2
                            if pygame.sprite.spritecollideany(Boss,Black_Tile_Group) != None:
                                self._x = self._x - 2
                                self._y = self._y + 2
                            else:
                                self._moving = True
                        if Player._y == self._y and self._moving == False:
                            self._x = self._x + 2
                            if pygame.sprite.spritecollideany(Boss,Black_Tile_Group) != None:
                                self._x = self._x - 2
                            else:
                                self._moving = True
                    if Player._x < self._x and self._moving == False:
                        if Player._y > self._y:
                            self._x = self._x - 2
                            self._y = self._y + 2
                            if pygame.sprite.spritecollideany(Boss,Black_Tile_Group) != None:
                                self._x = self._x + 2
                                self._y = self._y - 2
                            else:
                                self._moving = True
                        if Player._y < self._y and self._moving == False:
                            self._x = self._x - 2
                            self._y = self._y - 2
                            if pygame.sprite.spritecollideany(Boss,Black_Tile_Group) != None:
                                self._x = self._x + 2
                                self._y = self._y + 2
                            else:
                                self._moving = True
                        if Player._y == self._y and self._moving == False:
                            self._x = self._x - 2
                            if pygame.sprite.spritecollideany(Boss,Black_Tile_Group) != None:
                                self._x = self._x - 2
                            else:
                                self._moving = True
                    if Player._x == self._x and self._moving == False:
                        if Player._y > self._y:
                            self._y = self._y + 2
                            if pygame.sprite.spritecollideany(Boss,Black_Tile_Group) != None:
                                self._y = self._y - 2
                            else:
                                self._moving = True
                        if Player._y < self._y and self._moving == False:
                            self._y = self._y - 2
                            if pygame.sprite.spritecollideany(Boss,Black_Tile_Group) != None:
                                self._y = self._y + 2
                            else:
                                self._moving = True
                else:           
                    if self.__Spawn_X > self._x:
                        if self.__Spawn_Y > self._y:
                            self._x = self._x + 2
                            self._y = self._y + 2
                            self._moving = True
                        elif self.__Spawn_Y < self._y:
                            self._x = self._x + 2
                            self._y = self._y - 2
                            self._moving = True
                        elif self.__Spawn_Y == self._y:
                            self._x = self._x + 2
                            self._moving = True
                    elif self.__Spawn_X < self._x:
                        if self.__Spawn_Y > self._y:
                            self._x = self._x - 2
                            self._y = self._y + 2
                            self._moving = True
                        elif self.__Spawn_Y < self._y:
                            self._x = self._x - 2
                            self._y = self._y - 2
                            self._moving = True
                        elif self.__Spawn_Y == self._y:
                            self._x = self._x - 2
                            self._moving = True
                    elif self.__Spawn_X == self._x:
                        if self.__Spawn_Y > self._y:
                            self._y = self._y + 2
                            self._moving = True
                        elif self.__Spawn_Y < self._y:
                            self._y = self._y - 2
                            self._moving = True


            if pygame.sprite.collide_rect(Player,Boss) and self.dead == False and self._moving == False and Player.dead == False:
                self.attack = True
        else:
            if self._dead_first == False:
                self._dead_first = True
            self.dead = True
            self._moving = False
            self.attack = False
        self.__State_Machine()
    def __State_Machine(self):
        if self._dead_first and self.dead:
            self._images = self.__Machine.Get_Animation("Dead")
            self._image = self._images[self._dead_point]
            self.rect = self._image.get_rect()
            self.rect.x = self._x
            self.rect.y = self._y
            if (self._dead_point + 1) == len(self._images):
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
                self._dead_first = None
            else:
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
                self._dead_point = self._dead_point + 1
        elif self.dead:
            self._images = self.__Machine.Get_Animation("Dead")
            self._image = self._images[len(self._images)-1]
            self.rect = self._image.get_rect()
            self.rect.x = self._x
            self.rect.y = self._y
        elif self._moving:
            self.attack = False
            self._images = self.__Machine.Get_Animation("Run")
            self._image = self._images[self._walk_point]
            self.rect = self._image.get_rect()
            self.rect.x = self._x
            self.rect.y = self._y
            if (self._walk_point + 1) == len(self._images):
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
            else:
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = self._walk_point + 1
        elif self.attack:
            self._images = self.__Machine.Get_Animation("Attack")
            self._image = self._images[self._attack_point]
            self.rect = self._image.get_rect()
            self.rect.x = self._x
            self.rect.y = self._y
            if (self._attack_point + 1)== len(self._images):
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
                self.attack = False
            else:
                self._idle_point = 0
                self._attack_point = self._attack_point + 1
                self._walk_point = 0
        elif self._moving == False:
            self.attack = False
            self._images = self.__Machine.Get_Animation("Idle")
            self._image = self._images[self._idle_point]
            self.rect = self._image.get_rect()
            self.rect.x = self._x
            self.rect.y = self._y
            if (self._idle_point + 1) == len(self._images):
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
            else:
                self._idle_point = self._idle_point + 1
                self._attack_point = 0
                self._walk_point = 0
        self.__Draw()

    def __Draw(self):
        if self.__Wait_Frame == 40 and self.dead == False:
            self.__Wait_Frame = 0
            self.Health = self.Health + random.randint(10,20)
            if self.Health > 600:
                self.Health = 600
        else:
            self.__Wait_Frame = self.__Wait_Frame + 1
        self.Eyes.Move(self._x,self._y)
        self._display.blit(self._image,(self._x,self._y))

class Enemy(Entity):
    def __init__(self,display,TileSize,MapWidth,MapHeight,MapComplexity):
        Entity.__init__(self,display,TileSize,MapWidth,MapHeight,MapComplexity)
        self._image = pygame.image.load(Path+"\Deep Delve\Player\\idle_stand (1).png")
        self._image = pygame.transform.scale(self._image,(49,50))
        self.rect = self._image.get_rect()
        self.x = 0
        self.y = 0
        self.rect.x = self.x
        self.rect.y = self.y
        self.Health = 100
        self.dead_sign = False
        self.__Machine = Enemy_machine()
        self.Eyes = Entity_eyes(self.x,self.y,self._image)
    def Move(self):
        if self.Health > 0 and self.dead == False:
            self._moving = False
            if pygame.sprite.collide_rect(Player,self) == False:
                if pygame.sprite.collide_rect(Player,self.Eyes) == True:
                    if Player._x > self.x:
                        if Player._y > self.y:
                            self.x = self.x + 2
                            self.y = self.y + 2
                            self._moving = True
                        if Player._y < self.y:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self._moving = True
                        if Player._y == self.y:
                            self.x = self.x + 2
                            self._moving = True
                    if Player._x < self.x:
                        if Player._y > self.y:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self._moving = True
                        if Player._y < self.y:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self._moving = True
                        if Player._y == self.y:
                            self.x = self.x - 2
                            self._moving = True
                    if Player._x == self.x:
                        if Player._y > self.y:
                            self.y = self.y + 2
                            self._moving = True
                        if Player._y < self.y:
                            self.y = self.y - 2
                            self._moving = True
            if pygame.sprite.collide_rect(Player,self) and self.dead == False and self._moving == False and Player.dead == False:
                self.attack = True
        else:
            if self._dead_first == False:
                self._dead_first = True
            self.dead = True
            self._moving = False
            self.attack = False
        self.__State_Machine()
    def __State_Machine(self):
        if self._dead_first and self.dead:
            self._images = self.__Machine.Get_Animation("Dead")
            self._image = self._images[self._dead_point]
            self.rect = self._image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            if (self._dead_point + 1) == len(self._images):
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
                self._dead_first = None
                self.dead_sign = True
            else:
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
                self._dead_point = self._dead_point + 1
        elif self.dead:
            self._images = self.__Machine.Get_Animation("Dead")
            self._image = self._images[len(self._images)-1]
            self.rect = self._image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
        elif self._moving:
            self.attack = False
            self._images = self.__Machine.Get_Animation("Run")
            self._image = self._images[self._walk_point]
            self.rect = self._image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            if (self._walk_point + 1) == len(self._images):
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
            else:
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = self._walk_point + 1
        elif self.attack:
            self._images = self.__Machine.Get_Animation("Attack")
            self._image = self._images[self._attack_point]
            self.rect = self._image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            if (self._attack_point + 1)== len(self._images):
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
                self.attack = False
            else:
                self._idle_point = 0
                self._attack_point = self._attack_point + 1
                self._walk_point = 0
        elif self._moving == False:
            self.attack = False
            self._images = self.__Machine.Get_Animation("Idle")
            self._image = self._images[self._idle_point]
            self.rect = self._image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            if (self._idle_point + 1) == len(self._images):
                self._idle_point = 0
                self._attack_point = 0
                self._walk_point = 0
            else:
                self._idle_point = self._idle_point + 1
                self._attack_point = 0
                self._walk_point = 0
        self.__Draw()

    def __Draw(self):
        self.Eyes.Move(self.x,self.y)
        self._display.blit(self._image,(self.x,self.y))




class Map(Entity):
    def __init__(self,display,TileSize,MapWidth,MapHeight,MapComplexity):
        Entity.__init__(self,display,TileSize,MapWidth,MapHeight,MapComplexity)
        self.__tile = ""
        self.__count = 0
        self.__randrow = 0
        self.__randcol = 0
        self.__randside = 0
        self.__Boss_Door = ()
        self.__Last_Square_Location = []
        self.__Loop = True
        self.__Generate()

    def __Generate(self):
        self.__get_tile_map()
        self.__Draw()
        ## Start map display setup
    def __Draw(self):
        for row in range(self._MapHeight):
            for column in range(self._MapWidth):
                self._tilemap[row][column].x = column * self._TileSize
                self._tilemap[row][column].y = row * self._TileSize
                if self._tilemap[row][column].Square != None or self._tilemap[row][column].Player_Spawn != None or self._tilemap[row][column].Boss_Door != None or self._tilemap[row][column].Player_Door != None or self._tilemap[row][column].Enemy_Spawn != None or self._tilemap[row][column].Boss_Spawn != None or self._tilemap[row][column].Boss_Room != None:
                    self._tilemap[row][column].image = pygame.image.load(Path+"\Deep Delve\Map\\1,1,1,1.png")
                    self._tilemap[row][column].image = pygame.transform.scale(self._tilemap[row][column].image,(60,60))
                    self._tilemap[row][column].image = self._tilemap[row][column].image.convert()
                    self._tilemap[row][column].rect = self._tilemap[row][column].image.get_rect()
                    self._tilemap[row][column].rect.x = self._tilemap[row][column].x
                    self._tilemap[row][column].rect.y = self._tilemap[row][column].y
                    self._display.blit(self._tilemap[row][column].image,(self._tilemap[row][column].x,self._tilemap[row][column].y))
                    Tile_Group.add(self._tilemap[row][column])
                    ## Visable tile
                else:
                    self._tilemap[row][column].image = pygame.image.load(Path+"\Deep Delve\Map\\0,0,0,0.png")
                    self._tilemap[row][column].image = pygame.transform.scale(self._tilemap[row][column].image,(60,60))
                    self._tilemap[row][column].image = self._tilemap[row][column].image.convert()
                    self._tilemap[row][column].rect = self._tilemap[row][column].image.get_rect()
                    self._tilemap[row][column].rect.x = self._tilemap[row][column].x
                    self._tilemap[row][column].rect.y = self._tilemap[row][column].y
                    self._display.blit(self._tilemap[row][column].image,(self._tilemap[row][column].x,self._tilemap[row][column].y))
                    Black_Tile_Group.add(self._tilemap[row][column])
                    Tile_Group.add(self._tilemap[row][column])
                    ## Black tile
        
    ## Setting up the list-map
    def re_draw(self):
        ## Re-draw the dirty map
        for row in range(self._MapHeight):
            for tile in (self._tilemap[row]):
                if Player.down:
                    tile.y = tile.y - self._Dist
                    tile.rect.y = tile.rect.y - self._Dist
                elif Player.up:
                    tile.y = tile.y + self._Dist
                    tile.rect.y = tile.rect.y + self._Dist
                if Player.right:
                    tile.x = tile.x - self._Dist
                    tile.rect.x = tile.rect.x - self._Dist
                elif Player.left:
                    tile.x = tile.x + self._Dist
                    tile.rect.x = tile.rect.x + self._Dist
                self._display.blit(tile.image,(tile.x,tile.y))
        if Player.down:
           for enemy in Enemy_Group:
                enemy.y = enemy.y - self._Dist
           Boss._y = Boss._y - self._Dist
        elif Player.up:
            for enemy in Enemy_Group:
                enemy.y = enemy.y + self._Dist
            Boss._y = Boss._y + self._Dist
        if Player.right:
            for enemy in Enemy_Group:
                enemy.x = enemy.x - self._Dist
            Boss._x = Boss._x - self._Dist
        elif Player.left:
            for enemy in Enemy_Group:
                enemy.x = enemy.x + self._Dist
            Boss._x = Boss._x + self._Dist



    def __get_tile_map(self):
        self._tilemap = []
        for row in range(self._MapHeight):
            self._tilemap.append([])
            for column in range(self._MapWidth):
                self._tilemap[row].append(None)
        for row in range(self._MapHeight):
            for column in range(self._MapWidth):
                self._tilemap[row][column] = Square_Type()
        self.__Start_room()
        self.__Boss_room()
        self.__Connect_Start_Rooms()
        self.__Create_Map()
        for loop in range(Enemy_Count):
            valid = True
            while valid:
                self.__randrow = random.randint(3,self._MapHeight-3)
                self.__randcol = random.randint(3,self._MapWidth-3)
                if self._tilemap[self.__randrow][self.__randcol].Square != None and self._tilemap[self.__randrow][self.__randcol] not in Enemy_Spawn_Group:
                    Enemy_Spawn_Group.add(self._tilemap[self.__randrow][self.__randcol])
                    valid = False
                                          
    ## Placing the boss room
    def __Boss_room(self):
        valid = True
        while valid:
            self.__randrow = random.randint(15,self._MapHeight-4)
            self.__randcol = random.randint(10,self._MapWidth-4)
            if self.__randrow > ((self._MapWidth - self._MapWidth) + 2) and self.__randcol > ((self._MapHeight - self._MapHeight) + 2):
                if self._tilemap[self.__randrow][self.__randcol].Empty:
                    for space in range(0,3):
                        if self._tilemap[self.__randrow+space][self.__randcol].Empty and self._tilemap[self.__randrow+space][self.__randcol+space].Empty and self._tilemap[self.__randrow][self.__randcol+space].Empty:
                            if self._tilemap[self.__randrow-space][self.__randcol].Empty and self._tilemap[self.__randrow-space][self.__randcol-space].Empty and self._tilemap[self.__randrow][self.__randcol-space].Empty:
                                if self._tilemap[self.__randrow-space][self.__randcol+space].Empty and self._tilemap[self.__randrow+space][self.__randcol-space].Empty:
                                    if space == 2:
                                        valid = False
                                else:
                                    break
                            else:
                                break
                        else:
                            break

        self._tilemap[self.__randrow][self.__randcol].Boss_Spawn = Boss_Spawn()
        self._tilemap[self.__randrow+1][self.__randcol+1].Boss_Room = Square()
        self._tilemap[self.__randrow+1][self.__randcol-1].Boss_Room = Square()
        self._tilemap[self.__randrow-1][self.__randcol+1].Boss_Room = Square()
        self._tilemap[self.__randrow-1][self.__randcol-1].Boss_Room = Square()
        valid = True
        while valid:
            self.__randside = random.randint(1,4)
            if self.__randside == 1:
                if self.__randcol - 3 != 0:
                    self._tilemap[self.__randrow][self.__randcol-1].Boss_Door = Door()
                    self._tilemap[self.__randrow][self.__randcol+1].Boss_Room = Square()
                    self._tilemap[self.__randrow-1][self.__randcol].Boss_Room = Square()
                    self._tilemap[self.__randrow+1][self.__randcol].Boss_Room = Square()
                    break
            elif self.__randside == 2:
                if self.__randrow - 3 != 0:
                    self._tilemap[self.__randrow][self.__randcol-1].Boss_Room = Square()
                    self._tilemap[self.__randrow][self.__randcol+1].Boss_Room = Square()
                    self._tilemap[self.__randrow-1][self.__randcol].Boss_Door = Door()
                    self._tilemap[self.__randrow+1][self.__randcol].Boss_Room = Square()
                    break
            elif self.__randside == 3:
                if self.__randcol + 3 != self._MapWidth:
                    self._tilemap[self.__randrow][self.__randcol-1].Boss_Room = Square()
                    self._tilemap[self.__randrow+1][self.__randcol].Boss_Room = Square()
                    self._tilemap[self.__randrow-1][self.__randcol].Boss_Room = Square()
                    self._tilemap[self.__randrow][self.__randcol+1].Boss_Door = Door()
                    break
            elif self.__randside == 4:
                if self.__randcol + 3 != self._MapHeight:
                    self._tilemap[self.__randrow][self.__randcol-1].Boss_Room = Square()
                    self._tilemap[self.__randrow+1][self.__randcol].Boss_Door = Door()
                    self._tilemap[self.__randrow-1][self.__randcol].Boss_Room = Square()
                    self._tilemap[self.__randrow][self.__randcol+1].Boss_Room = Square()
                    break
    ## Placing the player start room
    def __Start_room(self):
        self._tilemap[3][3].Player_Spawn = Player_Spawn()
        self._tilemap[3][4].Player_Door = Door()
        self._tilemap[3][2].Boss_Room = Square()
        self._tilemap[2][3].Boss_Room = Square()
        self._tilemap[2][4].Boss_Room = Square()
        self._tilemap[2][2].Boss_Room = Square()
        self._tilemap[4][3].Boss_Room = Square()
        self._tilemap[4][4].Boss_Room = Square()
        self._tilemap[4][2].Boss_Room = Square()
    ## Connecting the boss and player start rooms
    def __Connect_Start_Rooms(self):
        for row in range(0,self._MapHeight):
            for square in range(0,self._MapWidth):
                if self._tilemap[row][square].Player_Door != None:
                    self.__Player_Door = (row,square)
                if self._tilemap[row][square].Boss_Door != None:
                    self.__Boss_Door = (row,square)
                if self._tilemap[row][square].Player_Spawn != None:
                    self._Player_Spawn = (row,square)
                if self._tilemap[row][square].Boss_Spawn != None:
                    self._Boss_Spawn = (row,square)
        if self.__randside == 4:
            self._tilemap[self.__Boss_Door[0]+1][self.__Boss_Door[1]].Boss_Room = Square()
            self._tilemap[self.__Boss_Door[0]+2][self.__Boss_Door[1]].Square = Square()
            self.__Last_Square_Location = [self.__Boss_Door[0]+2,self.__Boss_Door[1]]
            if self.__Player_Door[1] >= self.__Last_Square_Location[1]:
                for loop in range(3):
                    self._tilemap[self.__Last_Square_Location[0]][self.__Last_Square_Location[1]+1].Square = Square()
                    self.__Last_Square_Location = [self.__Last_Square_Location[0],self.__Last_Square_Location[1]+1]
            elif self.__Player_Door[1] < self.__Last_Square_Location[1]:
                for loop in range(3):
                    self._tilemap[self.__Last_Square_Location[0]][self.__Last_Square_Location[1]-1].Square = Square()
                    self.__Last_Square_Location = [self.__Last_Square_Location[0],self.__Last_Square_Location[1]-1]
        elif self.__randside == 3:
            self._tilemap[self.__Boss_Door[0]][self.__Boss_Door[1]+1].Square = Square()
            self._tilemap[self.__Boss_Door[0]][self.__Boss_Door[1]+2].Square = Square()
            self.__Last_Square_Location = [self.__Boss_Door[0],self.__Boss_Door[1]+2]
            if self.__Player_Door[1] >= self.__Last_Square_Location[1]:
                for loop in range(3):
                    self._tilemap[self.__Last_Square_Location[0]+1][self.__Last_Square_Location[1]].Square = Square()
                    self.__Last_Square_Location = [self.__Last_Square_Location[0]+1,self.__Last_Square_Location[1]]
        elif self.__randside == 2:
            self._tilemap[self.__Boss_Door[0]-1][self.__Boss_Door[1]].Square = Square()
            self._tilemap[self.__Boss_Door[0]-2][self.__Boss_Door[1]].Square = Square()
            self.__Last_Square_Location = [self.__Boss_Door[0]-2,self.__Boss_Door[1]]
            if self.__Player_Door[1] >= self.__Last_Square_Location[1]:
                for loop in range(3):
                    self._tilemap[self.__Last_Square_Location[0]][self.__Last_Square_Location[1]+1].Square = Square()
                    self.__Last_Square_Location = [self.__Last_Square_Location[0],self.__Last_Square_Location[1]+1]
        elif self.__randside == 1:
            self._tilemap[self.__Boss_Door[0]][self.__Boss_Door[1]-1].Square = Square()
            self._tilemap[self.__Boss_Door[0]][self.__Boss_Door[1]-2].Square = Square()
            self.__Last_Square_Location = [self.__Boss_Door[0],self.__Boss_Door[1]-2]
            if self.__Player_Door[1] >= self.__Last_Square_Location[1]:
                for loop in range(3):
                    self._tilemap[self.__Last_Square_Location[0]+1][self.__Last_Square_Location[1]].Square = Square()
                    self.__Last_Square_Location = [self.__Last_Square_Location[0]+1,self.__Last_Square_Location[1]]
                for loop in range(6):
                    self._tilemap[self.__Last_Square_Location[0]][self.__Last_Square_Location[1]+1].Square = Square()
                    self.__Last_Square_Location = [self.__Last_Square_Location[0],self.__Last_Square_Location[1]+1]
        while self.__Last_Square_Location[0] != self.__Player_Door[0] or self.__Last_Square_Location[1] != self.__Player_Door[1]:
            if self.__Player_Door[0] < self.__Last_Square_Location[0]:
                self._tilemap[self.__Last_Square_Location[0]-1][self.__Last_Square_Location[1]].Square = Square()
                self.__Last_Square_Location = [self.__Last_Square_Location[0]-1,self.__Last_Square_Location[1]]
            elif self.__Player_Door[1] < self.__Last_Square_Location[1]:
                self._tilemap[self.__Last_Square_Location[0]][self.__Last_Square_Location[1]-1].Square = Square()
                self.__Last_Square_Location = [self.__Last_Square_Location[0],self.__Last_Square_Location[1]-1]

    def __Create_Map(self):
        for loop in range(self._MapComplexity):
            valid = True
            while valid:
                self.__randrow = random.randint(3,self._MapHeight-3)
                self.__randcol = random.randint(3,self._MapWidth-3)
                if self._tilemap[self.__randrow][self.__randcol].Square != None: 
                    self.__Last_Square_Location = [self.__randrow,self.__randcol]
                    valid = False
            self.__randside = random.randint(1,4)
            for loop2 in range(30):
                if loop2 % 5 == 0:
                    self.__randside = random.randint(1,4)
                valid2 = True
                while valid2:
                    if self.__randside == 1:
                        if self.__Last_Square_Location[1]-3 != 0:
                            if self._tilemap[self.__Last_Square_Location[0]][self.__Last_Square_Location[1]-2].Boss_Room != None:
                                valid = True
                                while valid:
                                    self.__randside = random.randint(1,4)
                                    if self.__randside != 1:
                                        valid = False
                            else:
                                valid2 = False
                        else:
                            valid = True
                            while valid:
                                self.__randside = random.randint(1,4)
                                if self.__randside != 1:
                                    valid = False
                    if self.__randside == 2:
                        if self.__Last_Square_Location[0]-3 != 0:
                            if self._tilemap[self.__Last_Square_Location[0]+2][self.__Last_Square_Location[1]].Boss_Room != None:
                                valid = True
                                while valid:
                                    self.__randside = random.randint(1,4)
                                    if self.__randside != 2:
                                        valid = False
                            else:
                                valid2 = False
                        else:
                            valid = True
                            while valid:
                                self.__randside = random.randint(1,4)
                                if self.__randside != 2:
                                    valid = False
                    if self.__randside == 3:
                        if self.__Last_Square_Location[1]+3 != self._MapWidth:
                            if self._tilemap[self.__Last_Square_Location[0]][self.__Last_Square_Location[1]+2].Boss_Room != None:
                                valid = True
                                while valid:
                                    self.__randside = random.randint(1,4)
                                    if self.__randside != 3:
                                        valid = False
                            else:
                                valid2 = False
                        else:
                            valid = True
                            while valid:
                                self.__randside = random.randint(1,4)
                                if self.__randside != 3:
                                    valid = False
                    if self.__randside == 4:
                        if self.__Last_Square_Location[0]+3 != self._MapHeight:
                            if self._tilemap[self.__Last_Square_Location[0]+2][self.__Last_Square_Location[1]].Boss_Room != None:
                                valid = True
                                while valid:
                                    self.__randside = random.randint(1,4)
                                    if self.__randside != 4:
                                        valid = False
                            else:
                                valid2 = False
                        else:
                            valid = True
                            while valid:
                                self.__randside = random.randint(1,4)
                                if self.__randside != 4:
                                    valid = False
                if self.__randside == 1:
                    self._tilemap[self.__Last_Square_Location[0]][self.__Last_Square_Location[1]-1].Square = Square()
                    self.__Last_Square_Location = [self.__Last_Square_Location[0],self.__Last_Square_Location[1]-1]
                elif self.__randside == 2:
                    self._tilemap[self.__Last_Square_Location[0]-1][self.__Last_Square_Location[1]].Square = Square()
                    self.__Last_Square_Location = [self.__Last_Square_Location[0]-1,self.__Last_Square_Location[1]]
                elif self.__randside == 3:
                    self._tilemap[self.__Last_Square_Location[0]][self.__Last_Square_Location[1]+1].Square = Square()
                    self.__Last_Square_Location = [self.__Last_Square_Location[0],self.__Last_Square_Location[1]+1]
                elif self.__randside == 4:
                    self._tilemap[self.__Last_Square_Location[0]+1][self.__Last_Square_Location[1]].Square = Square()
                    self.__Last_Square_Location = [self.__Last_Square_Location[0]+1,self.__Last_Square_Location[1]]
            
        
            
            
Map = Map(display,TileSize,30,30,MapComplexity)
Player = Player(display,TileSize,30,30,MapComplexity)
Boss = Boss(display,TileSize,30,30,MapComplexity)
for loop in range(Enemy_Count):
    Enemy_Group.add(Enemy(display,TileSize,30,30,MapComplexity))
for enemy in Enemy_Group:
    for spawn in Enemy_Spawn_Group:
        if spawn.spawned == False:
            enemy.x = spawn.x
            enemy.y = spawn.y
            spawn.spawned = True
            break
Player_Group.add(Player)
Boss_Group.add(Boss)
Running = True
while Running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Running = False
    if Player.dead:
        pygame.display.set_caption("You died!")
        pygame.time.wait(1000)
        pygame.quit()
        running = False
    elif Boss.dead and Enemy_Count == 0:
        pygame.display.set_caption("You win!")
        pygame.time.wait(1000)
        pygame.quit()
        running = False
    Map.re_draw()
    Player.Move()
    Boss.Move()
    for enemy in Enemy_Group:
        enemy.Move()
        if enemy.dead_sign:
            Enemy_Count = Enemy_Count - 1
            enemy.dead_sign = False
        if pygame.sprite.collide_rect(Player,enemy):
            Damage(Player,enemy)
    if pygame.sprite.collide_rect(Player,Boss):
        Damage(Player,Boss)
    pygame.display.update()
    Clock.tick(40)
