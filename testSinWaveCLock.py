import SinWaveClock
import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()
    testScreen = pygame.display.set_mode((1000, 300))
    testScreen.fill((0,0,0))
    sin = SinWaveClock.SinWaveClock(1000, 300)
    testScreen.blit(sin,(0,0))
    pygame.display.update()
    run = True
    while(run):
        clock.tick(26)
        testScreen.blit(sin.Update(), (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    run = False
            elif event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()


