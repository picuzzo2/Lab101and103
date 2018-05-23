import os,sys
import pygame  #lazy but responsible (avoid namespace flooding)

class Character:
    def __init__(self,rect):
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.image.fill((255,255,255))

    def update(self,surface):
        self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image,self.rect)

def main(Surface,Player):
    game_event_loop(Player)
    Surface.fill(0)
    Player.update(Surface)


def game_event_loop(Player):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Player.rect.collidepoint(event.pos):
                Player.click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            Player.click = False
        elif event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    Screen = pygame.display.set_mode((1000,600))
    MyClock = pygame.time.Clock()
    MyPlayer = Character((0,0,10,10))
    MyPlayer.rect.center = Screen.get_rect().center
    while 1:
        main(Screen,MyPlayer)
        pygame.display.update()
        MyClock.tick(60)